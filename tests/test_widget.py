import pytest

from src.widget import get_date, mask_account_card


# Фикстура для параметризованных тестов
@pytest.fixture
def card_data():
    return [
        ("Visa Platinum 7000792289606361", "Visa Platinum 700079******6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("MasterCard 5185373029202738", "MasterCard 518537******2738"),
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Invalid Card 1234", "Ошибка: Неверный формат номера счета или карты"),
    ]


# Параметризованный тест для функции mask_account_card
@pytest.mark.parametrize(
    "input_data,expected_result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 700079******6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("MasterCard 5185373029202738", "MasterCard 518537******2738"),
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Invalid Card 1234", "Ошибка: Неверный формат номера счета или карты"),
    ],
)
def test_mask_account_card(input_data, expected_result):
    assert mask_account_card(input_data) == expected_result


def test_get_date():
    # Примеры тестов для функции get_date
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2023-12-25T15:45:30.123456") == "25.12.2023"
    assert get_date("invalid date") == ""  # Проверяем возврат пустой строки на неверном формате
    assert get_date("") == ""  # Пустая строка
    assert get_date(" ") == ""  # Пробел
    assert get_date("2024-02-30T12:00:00.000000") == ""  # Неверные даты (нет 30 февраля)
