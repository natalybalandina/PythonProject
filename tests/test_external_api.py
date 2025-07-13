from src.external_api import convert_to_rub


def test_currency_exchange_rate():
    # """
    # функция Mock для API обращение к серверу обмена валют для RUB
    # """
    assert convert_to_rub("RUB") == 1


def test_currency_exchange_rate_1():
    # """
    # функция Mock для API обращение к серверу обмена валют для RUB
    # """
    assert convert_to_rub(5) == 0
