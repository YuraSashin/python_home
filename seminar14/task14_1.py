# - doctest

class Matrix:
    """ Класс матрица для математических операций с ним """
    _rows: int = None
    _colm: int = None
    _a_matrix: list[list[int, float]] = None


    def __init__(self, a_matrix: list[list[int, float]]) -> None:
        """
        Ининциализация матрицы
        :param colm: int    -- a number of columns
        :param rows: int    -- a number of rows
        """
        self._rows = len(a_matrix)
        self._colm = len(a_matrix[0])
        self._a_matrix = a_matrix


    def __add__(self, other) -> 'Matrix':
        """
        Вычисление суммы матриц
        :param other: Matrix    -- other Matrix object
        :return: Matrix         -- new Matrix object
        """
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Matrix'-type object")
        if self._rows != other._rows or self._colm != other._colm:
            raise ValueError("Operation not permitted for different-dimensional matrices")
        new_matrix = [[0 for _ in range(self._colm)] for _ in range(self._rows)]
        for j in range(self._rows):
            for i in range(self._colm):
                new_matrix[j][i] = self._a_matrix[j][i] + other._a_matrix[j][i]
        return Matrix(new_matrix)

    # noinspection PyTypeChecker
    def __mul__(self, other) -> 'Matrix':
        """
        Умножение матрицы на число
        :param other: [int, float, Matrix]    -- other Matrix object
        :return: Matrix                       -- new Matrix object
        """
        if isinstance(other, self.__class__):
            return self.__rmul__(other)
        elif isinstance(other, int) or isinstance(other, float):
            new_matrix = [[0 for _ in range(self._colm)] for _ in range(self._rows)]
            for i in range(self._rows):
                j: int
                for j in range(self._colm):
                    new_matrix[i][j] = self._a_matrix[i][j] * other
            return Matrix(new_matrix)
        else:
            raise TypeError("Unsupported operation")
        

    def __rmul__(self, other) -> 'Matrix':
        """
        Умножение матриц
        :param other: Matrix    -- other Matrix object
        :return: Matrix         -- new Matrix object
        """
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Matrix'-type object")
        if self._colm != other._rows:
            raise ValueError("Operation not permitted if rows amount of first matrix "
                             "is not equal to columns amount of other one")
        new_matrix = [[0 for _ in range(other._rows)] for _ in range(self._rows)]
        for i in range(self._rows):
            for j in range(other._rows):
                new_matrix[i][j] = self._a_matrix[i][j] * other._a_matrix[j][i]
        return Matrix(new_matrix)
    

    def __eq__(self, other) -> bool:
        """Сравнение матриц, возвращает истину, если равны """
        if self is other:
            return True
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Matrix'-type object")
        if self._rows != other._rows or self._colm != other._colm:
            return False
        for i in range(self._rows):
            for j in range(self._colm):
                if self._a_matrix[i][j] != other._a_matrix[i][j]:
                    return False
        return True
    

    def __ne__(self, other) -> bool:
        """Сравнение матриц, возвращает ложь, если не равны"""
        return self.__eq__(other)
    

    def __str__(self) -> str:
        """User-readable representation method"""
        return '\n'.join(['\t'.join(map(str, row)) for row in self._a_matrix]) + '\n'
    

    def __repr__(self):
        """String object representation method"""
        return f'Matrix({self._a_matrix})'
    
    
def test_matrix():
    """
    >>> print(repr(Matrix([[1, 2, 3], [3, 2, 1], [4, 5, 6]])))
    Matrix([[1, 2, 3], [3, 2, 1], [4, 5, 6]])
    >>> print(repr(Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) * Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])))
    Matrix([[1, 8, 21, 40], [10, 30, 56, 88], [27, 60, 99, 144]])
    >>> print(repr(Matrix([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]]) + Matrix([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]])))
    Matrix([[2, 4, 6, 8], [8, 10, 12, 14], [16, 18, 20, 22]])
    >>> print(repr(Matrix([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]]) * 2))
    Matrix([[2, 4, 6, 8], [8, 10, 12, 14], [16, 18, 20, 22]])
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)