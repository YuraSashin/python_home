# Создайте класс МояСтрока где будут доступны все возможности str и дополнительно хранится имя автора строки и время
# создания (time.time)

from datetime import time


class MyString(str):
    """Расширяемый класс str."""

    def __new__(cls, value: str, author: str):
        """Расширяем метод new параметрами value и name."""
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time()
        return instance


def run_mystring():
    mystring = MyString('сама строка', 'доп. параметр')
    print(mystring.author)
    print(mystring.time)
    print(mystring)
    print(mystring.upper())
    print(mystring.title())
    help(mystring)
    help(MyString)