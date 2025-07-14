import json
import logging
import os

# Создание папки logs, если она не существует
if not os.path.exists('logs'):
    os.makedirs('logs')

# Настройка логирования
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)  # Уровень логирования не ниже DEBUG

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_handler.setLevel(logging.DEBUG)

# Создание и установка форматера
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def load_transactions(file_path):
    """Загрузить транзакции из JSON-файла."""
    if not os.path.isfile(file_path):
        logger.error(f"Файл не найден: {file_path}")
        return []  # Если файл не существует, вернуть пустой список

    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)  # Попытка загрузить данные из файла
            if isinstance(data, list):  # Проверка, является ли загруженные данные списком
                logger.info(f"Транзакции успешно загружены из файла: {file_path}")
                return data
            else:
                logger.warning(f"Данные в файле {file_path} не являются списком.")
                return []  # Если данные не список, вернуть пустой список
        except json.JSONDecodeError as e:
            logger.error(f"Ошибка при декодировании JSON из файла {file_path}: {e}")
            return []  # Если ошибка при декодировании JSON, вернуть пустой список
