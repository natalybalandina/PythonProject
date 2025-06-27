from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date

# Пример данных для тестов
data = [
    {"date": "2024-01-01T12:00:00.000000", "state": "EXECUTED", "amount": 100},
    {"date": "2024-01-05T12:00:00.000000", "state": "CANCELED", "amount": 200},
    {"date": "2024-01-03T12:00:00.000000", "state": "EXECUTED", "amount": 300},
    {"date": "2024-01-02T12:00:00.000000", "state": "EXECUTED", "amount": 400},
    {"date": "2024-01-05T12:00:00.000000", "state": "EXECUTED", "amount": 150},  # Одинаковая дата для тестирования
]


@pytest.fixture
def test_data() -> Any:
    return data


@pytest.mark.parametrize("state, expected", [("EXECUTED", 2), ("CANCELED", 2)])
def test_filter_by_state(test_data: Any, state: Any, expected: Any) -> Any:
    filtered_transactions = filter_by_state(test_data, state)
    assert len(filtered_transactions) == expected


@pytest.mark.parametrize(
    "reverse_order, expected_dates",
    [
        (
            True,
            [
                "2024-01-05T12:00:00.000000",  # Последняя по дате
                "2024-01-05T12:00:00.000000",  # Одинаковая дата
                "2024-01-03T12:00:00.000000",
                "2024-01-02T12:00:00.000000",
                "2024-01-01T12:00:00.000000",  # Первая по дате
            ],
        ),
        (
            False,
            [
                "2024-01-01T12:00:00.000000",
                "2024-01-02T12:00:00.000000",
                "2024-01-03T12:00:00.000000",
                "2024-01-05T12:00:00.000000",  # Одинаковая дата
                "2024-01-05T12:00:00.000000",  # Последняя по дате
            ],
        ),
    ],
)
def test_sort_by_date(test_data: Any, reverse_order: Any, expected_dates: Any) -> Any:
    # Тестирование сортировки по дате
    sorted_data = sort_by_date(test_data, reverse_order)
    sorted_dates = [item["date"] for item in sorted_data]
    assert sorted_dates == expected_dates


# Запуск тестов
if __name__ == "__main__":
    pytest.main()
