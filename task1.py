'''
Вычмат дз 1 часть 1
Вариант 6
Первая задача

Изучение методов Хаусхолдера, Гивенса и Гаусса
'''


from numpy import linalg
from matrix_func import *
from var6_lr1 import *
from git_gauss import *


a = [
        [-150,  -8,   7,    8],
        [   7, -77,  -0,   -2],
        [   4,   3, 146,   -4],
        [   8,  -2,  -1, -112]
    ]
b = [
        [ 3],
        [ 5],
        [ 7],
        [-5]
    ]

ab = [
        [-150,  -8,   7,    8, 3],
        [   7, -77,  -0,   -2, 5],
        [   4,   3, 146,   -4, 7],
        [   8,  -2,  -1, -112,-5]
]

tmp = []
for elem in gauss(ab):
    tmp1 = [elem]
    tmp.append(tmp1)

print(matrix_print(tmp))

matrix_print(linalg.solve(a, b), 'solve')