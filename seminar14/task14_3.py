# pytest

from task14_1 import Matrix
import pytest

'''  проверка сложения двух матриц '''
def test_sum():

   assert (str(Matrix([[1, -2], [25, -5]]) + Matrix([[11, -8], [15, 0]]))) == '[12, -10][40, -5]', "Неверная сумма"

'''проверка произведение двух матриц '''
def test_mult():

    assert (str(Matrix([[1, -2], [25, -5]]) * Matrix([[11, -8], [15, 0]]))) == '[-19, -8][200, -200]', "Неверное произведение"

if __name__ == '__main__':
    pytest.main([-v])