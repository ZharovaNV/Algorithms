# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

n = 5
m = 6
matrix = [[random.randint(0, 10) for _ in range(n)] for _ in range(m)]
for line in matrix:
    print(line)

max_num = 0
for i in range(n):
    min_num_col = matrix[0][i]
    for j in range(m):
        if matrix[j][i] < min_num_col:
            min_num_col = matrix[j][i]

    if min_num_col > max_num or i == 0:
        max_num = min_num_col

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_num}')
