import pytest

from src.masks import get_mask_account, get_mask_card_number


# Параметризованные тесты для функции get_mask_card_number
@pytest.mark.parametrize(
    "card_number, expected",
    [
        (7000792289606361, "700079******6361"),
        (1234567890123456, "123456******3456"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


# Параметризованные тесты для исключений
@pytest.mark.parametrize(
    "card_number",
    [
        123456,
        12345678901234567,
        "abcdefabcdefghijklmno",
    ],
)
def test_get_mask_card_number_exceptions(card_number):
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр."):
        get_mask_card_number(card_number)


# Параметризованные тесты для функции get_mask_account
@pytest.mark.parametrize(
    "account_number, expected",
    [
        (73654108430135874305, "**4305"),
        (12345678901234567890, "**7890"),
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


# Параметризованные тесты для исключений
@pytest.mark.parametrize(
    "account_number",
    [
        1234567890123456,
        1234567890123456789012345,
        "abcdefabcdefabcdefghij",
    ],
)
def test_get_mask_account_exceptions(account_number):
    with pytest.raises(ValueError, match="Номер счета должен содержать 20 цифр."):
        get_mask_account(account_number)
