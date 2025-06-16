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

from typing import Any


def get_mask_card_number(card_number: Any) -> Any:
    """Принимает на вход номер карты и возвращает её маску."""
    card_number = str(card_number)
    mask_card_number = card_number.replace(card_number[6:-4], "*" * len(card_number[6:-4]))
    # разбиваем замаскированный номер на блоки по 4 символа
    return f"{mask_card_number[:4]} {mask_card_number[4:6]}** **** {mask_card_number[12:]}"


def get_mask_account(account_number: Any) -> Any:
    """
    Принимает на вход номер счёта и возвращает в виде ** и 4 последние цифры.
    """
    account_number = str(account_number)
    return f'{" **" + account_number[-4:]}'


# print(get_mask_account("Счет 32145698741236985421"))
# print(get_mask_card_number("Maestro 1596837868705199"))
# print(get_mask_account("Счет 64686473678894779589"))
# print(get_mask_card_number("Master Card 7158300734726758"))
# print(get_mask_card_number("Visa Classic 6831982476737658"))
# print(get_mask_card_number("Visa Gold 5999414228426353"))
