import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "bank_number, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(bank_number, expected):
    assert mask_account_card(bank_number) == expected

@pytest.mark.parametrize(
    "date, expected",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2019-08-12T03:22:18.671407", "12.08.2019"),
        ("2019-07-12T02:26:18.671407", "12.07.2019"),
        ("2020-08-12T03:22:18.671407", "12.08.2020"),
    ],
)
def test_get_date(date, expected):
    assert get_date(date) == expected

