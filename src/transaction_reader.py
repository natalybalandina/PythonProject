import logging
import os
from typing import Dict, List

import pandas as pd

# Создание папки logs, если она не существует
if not os.path.exists("logs"):
    os.makedirs("logs")

# Настройка логирования
log_file_path = "logs/transactions.log"
logging.basicConfig(filename=log_file_path, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("TransactionLogger")


def read_transactions_from_csv(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV файла.
    """
    logger.info(f"Попытка прочитать данные из CSV файла: {file_path}")
    if not os.path.exists(file_path):
        logger.error(f"Файл {file_path} не найден.")
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    try:
        df = pd.read_csv(file_path)
        transactions = df.to_dict(orient="records")
        logger.info(f"Успешно считано {len(transactions)} транзакций из файла: {file_path}")
        return transactions
    except Exception as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {e}")
        raise


def read_transactions_from_excel(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel файла.
    """
    logger.info(f"Попытка прочитать данные из Excel файла: {file_path}")
    if not os.path.exists(file_path):
        logger.error(f"Файл {file_path} не найден.")
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient="records")
        logger.info(f"Успешно считано {len(transactions)} транзакций из файла: {file_path}")
        return transactions
    except Exception as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {e}")
        raise
