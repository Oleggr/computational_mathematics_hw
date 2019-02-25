from numpy import linalg
from matrix_func import *


a = [[2, 3], 
     [4, 1]]

b = [[1],
     [2]]
 

matrix_print(a, 'a')
matrix_print(b, 'b')

matrix_print(linalg.solve(a, b), 'solve')
matrix_print(linalg.inv(a), 'inv a')

print('\ndet a:', int(linalg.det(a)))