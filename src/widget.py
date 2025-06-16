import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_card_details: str) -> str:
    """Функция, которая маскирует номер карты либо счета"""
    bank_card_details_name = ""
    bank_card_details_num = ""
    new_bank_card_details = 0
    for el in bank_card_details:
        if el.isalpha():
            bank_card_details_name += el
        elif el.isdigit():
            bank_card_details_num += el
            new_bank_card_details += 1
    if new_bank_card_details > 16:
        return f"{bank_card_details_name} {get_mask_account(bank_card_details_num)}"
    else:
        return f"{bank_card_details_name} {get_mask_card_number(bank_card_details_num)}"


def get_date(date: str) -> str:
    """
    Функция, которая возвращает дату в формате ДД.ММ.ГГГГ
    """
    new_date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    date_conversion = new_date.strftime("%d.%m.%Y")

    return date_conversion


print(mask_account_card("Счет 32145698741236985421"))
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("Master Card 7158300734726758"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(get_date("2024-03-11T02:26:18.671407"))
print(get_date("2025-06-08T02:26:18.671407"))
