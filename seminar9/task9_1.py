# Нахождение корней квадратного уравнения

from cmath import sqrt

def quadratic_equation(a: complex, b: complex, c: complex):
    discriminant: complex = b * b - 4 * a * c
    if discriminant > 0:
        x1: complex = (-b + sqrt(discriminant)) / (2 * a)
        x2: complex = (-b - sqrt(discriminant)) / (2 * a)
        return [x1, x2]
    elif discriminant == 0:
        x: complex = -b / 2 * a
        return x
    else:
        return "Нет корней"
    
# 5x ** 2 + 4x + 3 = 0
# result = quadratic_equation(5, 4, 3)
# print(result)

# 5x ** 2 + 4x + 1 = 0
result = quadratic_equation(5, -4, -1)
print(result)