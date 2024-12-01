def log(filename):
    def logging(func):
        def wrapper(*args, **kwargs):
            start = f"Function {func} started"
            if filename:
                result = func(*args, **kwargs)
                with open(filename, 'a', encoding='utf-8') as file:
                    file.write(f"{start}\n{func.__name__} ok\n{result}\nFunction {func} finished\n")
                return result
            else:
                result = func(*args, **kwargs)
                print(f"{func.__name__} ok")
                return f"{result}\nFunction {func} finished"

        return wrapper

    return logging


@log(filename="mylog.txt")
def my_function(x, y):

    return x + y


print(my_function(1, 2))

# Ожидаемый вывод в лог-файл mylog.txt при успешном выполнении:
# my_function ok
# Ожидаемый вывод при ошибке:
# my_function error: тип ошибки. Inputs: (1, 2), {}
# Где тип ошибки заменяется на текст ошибки.
