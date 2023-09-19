# Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации. 
# Также реализуйте возможность запуска из командной строки с передачей параметров.

import logging
from random import randint
import  argparse

logging.basicConfig(filename='Log.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


class Matrix:

    def __init__(self, matr):
        self._matr = matr


    def get_matrix(self):
        return self._matr
    

    def __add__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            logger.error(f'Не возможно выполнить сложение матриц, размерности матриц несовместимы:  [{len(self._matr)}][{len(self._matr[0])}] !=  [{len(other._matr)}][{len(other._matr[0])}] ')
            #raise ValFormatError

        else:
            new_matr = Matrix([[self._matr[i][j] + other._matr[i][j] for j in range(len(self._matr[0]))] for i in range(len(self._matr))])
            logger.info(f' СЛОЖЕНИЕ:  {self._matr} + {other._matr} = {new_matr}  ')
            return new_matr


    def __mul__(self, other):
        if len(self._matr[0]) != len(other._matr):
            logger.error(f'Не возможно выполнить умножение матриц, размерности матриц несовместимы: [{len(self._matr)}][{len(self._matr[0])}] !=  [{len(other._matr)}][{len(other._matr[0])}]')
            #raise ValFormatError
        else:
            new_matr = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matr)] for i_row in self._matr]
            logger.info(f' УМНОЖЕНИЕ:  {self._matr} * {other._matr} = {new_matr}  ')
            return Matrix(new_matr)
        

    def __eq__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            raise ValFormatError
        else:
            for i in range(len(self._matr)):
                for j in range(len(self._matr[0])):
                    if self._matr[i][j] != other._matr[i][j]:
                        return False
            logger.info(f' РАВЕНСТВО:  {self._matr} = {other._matr} ')
            return True


    def __repr__(self):
        s = ''
        for i in range(len(self._matr)):
            s += str(self._matr[i])
        return s


def convert_format(input: list[str] = None) -> list[float]:
    '''Преобразования входных данных в терминале в матрицу'''
    if len(input) == 1:
        j = 0
    else:
        j = 1
    m_1 = []
    m_2 = []
    input[j].append(' ')
    for i in input[j]:
        if i == ' ':
            m_2.append(list(m_1))
            m_1.clear()
        else:
            m_1.append(float(i))
    return m_2


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Получаем операцию над двумя матрицами")
    parser.add_argument('-m_1',  type = list, action='append', default = [['1', '1', '1', ' ', '1', '1', '1',' ', '1', '1', '1', ' ', '1', '1', '1']])
    parser.add_argument('-m_2',  type = list, action='append', default = [['1', '1', '1', ' ', '1', '1', '1',' ', '1', '1', '1', ' ', '1', '1', '1']]  )
    parser.add_argument('-operation', type=str, default='+')
    args = parser.parse_args()
    m_1 = convert_format(args.m_1)
    m_2 = convert_format(args.m_2)

    if args.operation == '+':
        print(f'СЛОЖЕНИЕ: {m_1} {args.operation} {m_2} = ', (f'{Matrix(m_1) + Matrix(m_2)} '))
    elif  args.operation == '*':
        print(f'УМНОЖЕНИЕ: {m_1} {args.operation} {m_2} = ', (f'{Matrix(m_1) * Matrix(m_2)} '))
    elif args.operation == '=':
        print(f'РАВЕНСТВО: {m_1} {args.operation} {m_2} = ', (f'{Matrix(m_1) == Matrix(m_2)} '))
    else:
        print(f'Такая операция {args.operation} над матрицами не предусмотрена!')