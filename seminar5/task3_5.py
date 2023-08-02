# Создайте функцию генератор чисел Фибоначчи 

def number(text: str, error: str): 
    while(True):
        try:
            number = int(input(text))
            return number
        except:
            print(error)


def fibo(number: int) -> (iter, int):
    fibo_list = [0, 1, 1]
    current = 0
    while current < number:
        while len(fibo_list) < number:
            fibo_list.append(sum(fibo_list[-2:]))
        yield fibo_list[current]
        current += 1

a = number('Введите целое число: ', 'Введено некорректное значение')

print(*(fibo(a)))