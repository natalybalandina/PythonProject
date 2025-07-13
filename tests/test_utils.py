import unittest
from unittest.mock import mock_open, patch

from src.external_api import convert_to_rub
from src.utils import load_transactions


class TestUtils(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    def test_load_transactions_empty_file(self, mock_file):
        result = load_transactions("data/operations.json")
        self.assertEqual(result, [])  # Проверяем, что результат пустой список

    @patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
    def test_load_transactions_valid_file(self, mock_file):
        result = load_transactions("data/operations.json")
        self.assertEqual(len(result), 1)  # Проверяем, что загружен один элемент
        self.assertEqual(result[0]["amount"], 100)  # Проверяем, что сумма равна 100

    @patch("builtins.open", new_callable=mock_open, read_data="not a json")
    def test_load_transactions_invalid_json(self, mock_file):
        result = load_transactions("data/operations.json")
        self.assertEqual(result, [])  # Проверяем, что результат пустой список при некорректном JSON

    @patch("os.path.isfile", return_value=False)
    def test_load_transactions_file_not_exist(self, mock_isfile):
        result = load_transactions("data/operations.json")
        self.assertEqual(result, [])  # Проверяем, что результат пустой список если файл не существует

    @patch("builtins.open", new_callable=mock_open, read_data='{"amount": 100, "currency": "USD"}')
    def test_load_transactions_not_a_list(self, mock_file):
        result = load_transactions("data/operations.json")
        self.assertEqual(result, [])  # Проверяем, что результат пустой список если данные не список

    @patch("requests.get")
    def test_convert_to_rub(self, mock_get):
        mock_get.return_value.status_code = 200

        # Предположим, курс 78.021461 RUB за USD, тогда 100 USD будут стоить 7802
        mock_get.return_value.json.return_value = {"rates": {"RUB": 78.02}}

        transaction = {"amount": 100, "currency": "USD"}
        result = convert_to_rub(transaction)
        expected_value = 7802
        # Ожидаемое значение
        self.assertEqual(result, expected_value)


if __name__ == "__main__":
    unittest.main()
