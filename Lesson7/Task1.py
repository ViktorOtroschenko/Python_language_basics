# Task1.
'''Реализовать класс ​ Matrix ​ (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()​ ), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — ​ система некоторых математических величин, расположенных в виде
прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
Следующий шаг — реализовать перегрузку метода ​ __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода ​ __add__() для реализации операции сложения двух
объектов класса ​ Matrix ​ (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.'''

class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        return '\n'.join(str(s) for s in self.matr)

    def __add__(self, other):
        return Matrix([[j[0] + j[1] for j in zip(i[0], i[1])] for i in zip(self.matr, other.matr)])

matrix_1 = Matrix([[41, 13], [27, 43], [51, 101]])
matrix_2 = Matrix([[14, -35], [-27, 42], [32, -2]])

print('matrix_1:', matrix_1, end='\n\n', sep='\n')
print('matrix_2:', matrix_2, end='\n\n', sep='\n')

print('Sum matrix:', matrix_1 + matrix_2, sep='\n')