import unittest
from unittest.mock import patch
from src.external_api import convert_to_rub


class TestConvertToRub(unittest.TestCase):
    @patch("requests.get")
    def test_convert_to_rub_success(self, mock_get):
        # Настраиваем имитацию ответа от API
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "success": True,
            "rates": {"RUB": 78.021461}  # Пример курса USD к RUB
        }

        transaction = {"amount": 100, "currency": "USD"}
        result = convert_to_rub(transaction)

        expected_value = round(100 * 78.021461, 2)  # Ожидаемое значение после конвертации
        self.assertEqual(result, expected_value)

    @patch("requests.get")
    def test_convert_to_rub_already_in_rub(self, mock_get):
        transaction = {"amount": 100, "currency": "RUB"}
        result = convert_to_rub(transaction)

        expected_value = 100.0  # Ожидаемое значение, если валюта уже в рублях
        self.assertEqual(result, expected_value)

    @patch("requests.get")
    def test_convert_to_rub_api_failure(self, mock_get):
        # Настраиваем имитацию неуспешного ответа от API
        mock_get.return_value.status_code = 500

        transaction = {"amount": 100, "currency": "USD"}
        result = convert_to_rub(transaction)

        expected_value = 0.0  # Ожидаемое значение при неуспешном запросе к API
        self.assertEqual(result, expected_value)

if __name__ == "__main__":
    unittest.main()
