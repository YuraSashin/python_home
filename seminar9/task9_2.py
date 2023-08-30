# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
import random
import csv


def gen_csv_with_nums(name: str = 'data/random', min_num: int = -1000, max_num: int = 1000):
    rows = []
    rows_count = random.randint(100, 1000)
    for _ in range(rows_count):
        a, b, c = random.sample(range(min_num, max_num), 3)
        rows.append({'a': a, 'b': b, 'c': c})
    with open(name + '.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['a', 'b', 'c']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)