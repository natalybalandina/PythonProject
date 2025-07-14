from datetime import datetime

import src.masks  # type: ignore


def mask_account_card(input_string: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа.
    """
    parts = input_string.split()
    card_type = " ".join(parts[:-1])  # Слова через пробел, указывающие тип карты или счета (кроме последнего)
    card_number_str = parts[-1]  # Последнее - номер карты или счета

    try:
        card_number = int(card_number_str)
        if "счет" in card_type.lower():  # Проверка на слово "Счет"
            masked_number = src.masks.get_mask_account(card_number)
        elif len(card_number_str) == 16:  # Проверка длины номера карты
            masked_number = src.masks.get_mask_card_number(card_number)
        else:
            raise ValueError("Неверный формат номера счета или карты")
        return f"{card_type} {masked_number}"
    except ValueError as e:
        return f"Ошибка: {e}"


def get_date(input_string: str) -> str:
    """
    Преобразует строку с датой в формате 'YYYY-MM-DDTHH:MM:SS.ssssss' в формат 'DD.MM.YYYY'.
    Возвращает пустую строку при неверном формате или невалидной дате.
    """
    input_string = input_string.strip()

    if not input_string:
        return ""

    try:
        # Парсим дату из строки
        date_object = datetime.fromisoformat(input_string[:-7])  # Убираем последние 7 символов
        return date_object.strftime("%d.%m.%Y")
    except ValueError:
        # Если произошла ошибка при парсинге, возвращаем пустую строку
        return ""


# Примеры использования
if __name__ == "__main__":
    card_examples = [
        "Visa Platinum 7000792289606361",
        "Счет 73654108430135874305",
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
    ]

    for card_data in card_examples:
        print(f"Входной аргумент: {card_data}")
        print(f"Выход функции: {mask_account_card(card_data)}")
        print("---")

    date_examples = ["2024-03-11T02:26:18.671407", "2023-12-25T15:45:30.123456", "invalid date"]

    for date_data in date_examples:
        print(f"Входной аргумент: {date_data}")
        print(f"Выход функции: {get_date(date_data)}")
        print("---")
