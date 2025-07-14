"""
Функция get_mask_card_number принимает на вход номер карты и возвращает ее маску.
Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX, где X — это цифра номера.
То есть видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками,
номер разбит по блокам по 4 цифры, разделенным пробелами. Пример работы функции:

7000792289606361 # входной аргумент

7000 79** **** 6361 # выход функции

Функция get_mask_account принимает на вход номер счета и возвращает его маску.
Номер счета замаскирован и отображается в формате **XXXX, где X — это
цифра номера. То есть видны только последние 4 цифры номера, а перед ними
— две звездочки.
Пример работы функции:
73654108430135874305 # входной аргумент
**4305 # выход функции
"""

import logging
import os

# Создание папки logs, если она не существует
if not os.path.exists('logs'):
    os.makedirs('logs')

# Настройка логирования для модуля masks
logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler('logs/masks.log', mode='w')
file_handler.setLevel(logging.DEBUG)

# Форматирование логов
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """
    Функция принимает на вход номер карты и возвращает его маску
    в формате XXXX XX** **** XXXX, где X - это цифры
    """
    logger.debug(f"Получение маски для номера карты: {card_number}")

    # Преобразуем номер карты в строку
    card_number_str = str(card_number)

    # Проверка, что номер карты составляет 16 цифр.
    if len(card_number_str) != 16 or not card_number_str.isdigit():
        logger.error("Ошибка: Номер карты должен содержать 16 цифр.")
        raise ValueError("Номер карты должен содержать 16 цифр.")

    # Создание маски карты, видны первые 6 и последние 4 цифры
    mask_card = f"{card_number_str[:6]}******{card_number_str[-4:]}"
    logger.info(f"Маска карты успешно создана: {mask_card}")

    return mask_card


def get_mask_account(account_number: int) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску в формате **XXXX,
    где X - это цифры
    """
    logger.debug(f"Получение маски для номера счета: {account_number}")

    # Преобразуем номер счета в строку
    account_number_str = str(account_number)

    # Проверяем, что номер счета состоит как минимум из 4 цифр
    if len(account_number_str) != 20 or not account_number_str.isdigit():
        logger.error("Ошибка: Номер счета должен содержать 20 цифр.")
        raise ValueError("Номер счета должен содержать 20 цифр.")

    # Создаем маску, видны последние 4 цифры
    mask_account = f"**{account_number_str[-4:]}"
    logger.info(f"Маска счета успешно создана: {mask_account}")

    return mask_account
