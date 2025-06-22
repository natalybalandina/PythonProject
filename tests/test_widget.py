from typing import Any

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "bank_number, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("MasterCard 1234 5678 9012 3456", "MasterCard 1234 56** **** 3456"),
        ("Счет №11112222333344445555", "Счет **5555"),
    ],
)
def test_mask_account_card(bank_number: Any, expected: Any) -> Any:
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
def test_get_date(date: Any, expected: Any) -> Any:
    assert get_date(date) == expected
