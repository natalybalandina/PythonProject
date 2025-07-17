from unittest.mock import patch, MagicMock
import pandas as pd
import os
import pytest
import unittest

from src.transaction_reader import read_transactions_from_csv, read_transactions_from_excel


class TestTransactionFunctions(unittest.TestCase):

    @patch('pandas.read_csv')
    @patch('os.path.exists')
    def test_read_transactions_from_csv_success(self, mock_exists, mock_read_csv):

        mock_exists.return_value = True
        mock_read_csv.return_value = pd.DataFrame({'amount': [100, 200], 'date': ['2023-01-01', '2023-01-02']})

        # Вызов функции
        result = read_transactions_from_csv('dummy_path.csv')

        # Проверка результатов
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['amount'], 100)
        self.assertEqual(result[1]['date'], '2023-01-02')

    @patch('pandas.read_csv')
    @patch('os.path.exists')
    def test_read_transactions_from_csv_file_not_found(self, mock_exists, mock_read_csv):

        mock_exists.return_value = False

        # Проверка на исключение
        with self.assertRaises(FileNotFoundError):
            read_transactions_from_csv('dummy_path.csv')

    @patch('pandas.read_excel')
    @patch('os.path.exists')
    def test_read_transactions_from_excel_success(self, mock_exists, mock_read_excel):

        mock_exists.return_value = True
        mock_read_excel.return_value = pd.DataFrame({'amount': [150, 250], 'date': ['2023-01-03', '2023-01-04']})

        # Вызов функции
        result = read_transactions_from_excel('dummy_path.xlsx')

        # Проверка результатов
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['amount'], 150)
        self.assertEqual(result[1]['date'], '2023-01-04')

    @patch('pandas.read_excel')
    @patch('os.path.exists')
    def test_read_transactions_from_excel_file_not_found(self, mock_exists, mock_read_excel):

        mock_exists.return_value = False

        # Проверка на исключение
        with self.assertRaises(FileNotFoundError):
            read_transactions_from_excel('dummy_path.xlsx')

if __name__ == '__main__':
    unittest.main()
