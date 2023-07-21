# Напишите программу, которая принимает две строки вида “a/b”
# - дробь с числителем и знаменателем. Программа должна возвращать сумму и
# произведение* дробей. Для проверки своего кода используйте модуль fractions.

import fractions
def number(text: str, error: str):
    while(True):
        try:
            number = int(input(text))
            return number
        except:
            print(error)

def sum(numerator_1: str, denominator_1: str, numerator_2: str, denominator_2: str ):
    if(int(denominator_1) != int(denominator_2)):
        numerator_1: int = int(numerator_1) * int(denominator_2)
        numerator_2: int = int(numerator_2) * int(denominator_1)
        denominator_1: int = int(denominator_1) * int(denominator_2)
        res: str = f'{numerator_1 + numerator_2}/{denominator_1}'
        return res
    else:
        res: str = f'{int(numerator_1) + int(numerator_2)}/{denominator_1}'
        return res

def multiplication(numerator_1: str, denominator_1: str, numerator_2: str, denominator_2: str ):
    res: str = f'{int(numerator_1) * int(numerator2)}/{int(denominator_1) * int(denominator2)}'
    return res

numerator1 = str(number('Введите числитель первой дроби: ','Введено некорректное значение'))
denominator1 = str(number('Введите знаминатель первой дроби: ','Введено некорректное значение'))
numerator2 = str(number('Введите числитель второй дроби: ','Введено некорректное значение'))
denominator2 = str(number('Введите знаминатель второй дроби: ','Введено некорректное значение'))

fraction1: str = f'{numerator1}/{denominator1}'
fraction2: str = f'{numerator2}/{denominator2}'

resul_sum = sum(numerator1,denominator1,numerator2,denominator2)
resul_mult = multiplication(numerator1,denominator1,numerator2,denominator2)

print(f'Сумма дробей {fraction1} и {fraction2} равна {resul_sum}')
print(f'Произведение этих дробей равно {resul_mult}')

# firstfraction = fractions.Fraction(int(numerator1), int(denominator1))
# secondfraction = fractions.Fraction(int(numerator2), int(denominator2))
# result1 = firstfraction + secondfraction
# result2 = firstfraction * secondfraction
# print(result1)
# print(result2)