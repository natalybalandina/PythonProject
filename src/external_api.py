import os
import requests
from dotenv import load_dotenv


def convert_to_rub(transaction: dict) -> float:
    """Функция конвертации валюты"""

    try:
        # Загрузка переменных из .env-файла
        load_dotenv()

        # Получение значения переменной API_KEY из .env-файла
        api_key = os.getenv("API_KEY")

        # Извлечение суммы и валюты из словаря
        amount = transaction.get("amount")
        currency = transaction.get("currency")

        if currency == "RUB":
            return float(amount)  # Если валюта уже в рублях, возвращаем сумму

        # Отправка GET-запроса к API
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers)

        # Проверяем статус ответа
        if response.status_code != 200:
            print("Ошибка при получении данных с API")
            return 0.0

        response_data = response.json()

        # Проверяем наличие ключа "rates" и вычисляем результат
        if "rates" in response_data and "RUB" in response_data["rates"]:
            rate = response_data["rates"]["RUB"]
            converted_amount = amount * rate
            return round(converted_amount, 2)  # Возвращаем сумму в рублях с округлением до двух знаков
        else:
            print("Курс не найден")
            return 0.0

    except (TypeError, ValueError):
        print("Ошибка типа данных")
        return 0.0
