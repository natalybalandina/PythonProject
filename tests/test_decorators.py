import os

import pytest

from src.decorators import log


@pytest.fixture  # Удаление файла журнала после выполнения теста
def clean_up():
    """Фикстура для удаления файла журнала после выполнения тестов.
    Её используют для уверенности в том, что перед выполнением теста
    ничего не делается, но после выполнения - проверяется наличие файла `test_log.txt`
    и удаляет его, если он существует.
    """
    yield
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")


# Успешная функция
@log(filename="test_log.txt")
def norm_func(x, y):
    """Выполняет деление двух чисел x и y -> (float).
    Возвращает: float: Результат деления.
    """
    return x + y


# Пример функции с ошибкой
@log(filename="test_log.txt")
def error_func(x, y):
    return x / y


def test_norm_func(capsys):
    result = norm_func(10, 2)
    assert result == 12

    # Проверка вывода в файл
    with open("logs/test_log.txt", "r") as log_file:
        log_content = log_file.readlines()
        assert any("norm_func called at" in line for line in log_content)
        assert "norm_func result: 12" in log_content[-1]


def test_error_func(capsys):
    with pytest.raises(ZeroDivisionError):
        error_func(1, 0)

    # Проверка вывода в файл
    with open("logs/test_log.txt", "r") as log_file:
        log_content = log_file.readlines()
        assert any("error_func error: ZeroDivisionError" in line for line in log_content)
