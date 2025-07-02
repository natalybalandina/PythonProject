import functools


def log(filename):
    """
    Декоратор для автоматической регистрации деталей выполнения функций (время вызова, имя функции, передаваемые
    аргументы, результат выполнения и информация об ошибках.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                with open(filename, "a") as file:
                    file.write(f"Запуск функции: {func.__name__} с аргументами: {args}, {kwargs}\n")
                    file.write(f"Функция: {func.__name__} вернула: {result}\n")
                return result
            except Exception as e:
                with open(filename, "a") as file:
                    file.write(f"Ошибка в функции: {func.__name__} с аргументами: {args}, {kwargs}\n")
                raise e

        return wrapper

    return decorator
