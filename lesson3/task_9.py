# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint

matrix = [[randint(1, 100) for _ in range(4)] for _ in range(5)]

for line in matrix:
    [print(f'{num:>5}', end='') for num in line]
    print()

max_in_mins = 0
for col in range(len(matrix[0])):
    min_val = matrix[0][col]
    for row in range(1, len(matrix)):
        if min_val > matrix[row][col]:
            min_val = matrix[row][col]
    if min_val > max_in_mins:
        max_in_mins = min_val

print(max_in_mins)
