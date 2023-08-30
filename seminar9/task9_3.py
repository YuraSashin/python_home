# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
import csv
from pathlib import Path
from typing import Callable
from functools import wraps


def from_csv_wrap(file_name: str):
    def deco(func: Callable):
        # Декоратор @wraps() модуля functools это удобная функция для вызова @functools.update_wrapper() в качестве
        # декоратора при определении функции-обертки
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(file_name, 'r', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file)
                for i, row in enumerate(reader):
                    if i == 0:
                        continue
                    args = (complex(j) for j in row)
                    result = func(*args, **kwargs)
                    yield result
        return wrapper
    return deco