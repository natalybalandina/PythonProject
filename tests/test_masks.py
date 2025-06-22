from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7000792289606362", "7000 79** **** 6362"),
        ("7200792289606361", "7200 79** **** 6361"),
        ("7100792289606362", "7100 79** **** 6362"),
    ],
)
def test_get_mask_card_numbers(card_number: Any, expected: Any) -> Any:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        (12345678901234567890, "**7890"),
        (12345678901234567891, "**7891"),
        (12345678901234567892, "**7892"),
        (12345678901234567893, "**7893"),
    ],
)
def test_get_mask_account(account_number: Any, expected: Any) -> Any:
    assert get_mask_account(account_number) == expected
