from typing import Any, Dict, List
import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def filter_state():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}    ]

def test_filter_by_state_executed(bank_base: Any):
    assert (filter_by_state(bank_base, state = 'EXECUTED') ==
    [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ])

def test_filter_by_state_canceled(bank_base):
    assert (filter_by_state(bank_base, state = 'CANCELED') ==
    [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ])


@pytest.mark.parametrize ("bank_base, date",
[
    {"2019-07-03T18:35:29.512364", "03.07.2019"},
    {"2018-10-14T08:21:33.419441", "14.10.2018"},
    {"2018-09-12T21:27:25.241689", "12.09.2018"},
    {"2018-06-30T02:08:58.425572", "30.06.2018"}
])


def test_sort_by_date(bank_base: Any, date: Any) -> Any:
    # сортировка по убыванию даты
    assert sort_by_date(bank_base) == date
