# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: 
# “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def Number(text: str, error: str):
    while(True):
        try:
            number = int(input(text))
            if( number > 100_000 or number < 0):
                print(error)
            else:
                return number
        except:
            print(error)

def Prime_number(a):
    i = 2
    while(i < a):
        if (a % i == 0):
            print(f'Число {a} является составным')
            break
        else:
            i += 1
    else:
        print(f'Число {a} является простым')
        
num = Number('Введите число от 0 до 100_000: ', 'Введено некорректное значение')
Prime_number(num)