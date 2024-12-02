import os
from functools import wraps


def log(filename=''):
    """ Декоратор, логирующий состояние функции в файл либо в консоль"""
    def logging(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = f"Function {func.__name__} started"

            if filename == "":
                print(start)
                print(func(*args, **kwargs))
                print(f"{func.__name__} ok")
                print(f"Function {func.__name__} finished")

            elif not filename.endswith(".txt"):
                raise NameError("Файл с неверным расширением")

            else:
                result = func(*args, **kwargs)
                os.makedirs(os.path.dirname(filename), exist_ok=True)
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(f"{start}\n{func.__name__} ok\n{result}\nFunction {func} finished\n")
                return result

        return wrapper

    return logging


@log("../logs/my_log.txt")
def my_function(x, y):

    return x + y


my_function(1, 2)

# Ожидаемый вывод в лог-файл mylog.txt при успешном выполнении:
# my_function ok
# Ожидаемый вывод при ошибке:
# my_function error: тип ошибки. Inputs: (1, 2), {}
# Где тип ошибки заменяется на текст ошибки.
