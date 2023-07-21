# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

def number(text: str, error: str):
    while(True):
        try:
            number = int(input(text))
            return number
        except:
            print(error)

def translation16(a):
    res = ''
    i = a
    while(a > 0):
        if (a % 16 == 10):
            res += 'A'
            a //= 16
        elif (a % 16 == 11):
            res += 'B'
            a //= 16
        elif (a % 16 == 12):
            res += 'C'
            a //= 16
        elif (a % 16 == 13):
            res += 'D'
            a //= 16
        elif (a % 16 == 14):
            res += 'E'
            a //= 16
        elif (a % 16 == 15):
            res += 'F'
            a //= 16
        else:
            res += str(a % 16)
            a //= 16
    res = res[::-1]
    print(res, hex(i))

num = number('Введите число: ','Введено некорректное значение')
translation16(num)
            

