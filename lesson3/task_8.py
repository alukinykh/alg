# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = []

for _ in range(4):
    line = input('Enter matrix line separated by a space: ').split()
    line_sum = 0
    for num in line:
        line_sum += int(num)
    line.append(str(line_sum))
    matrix.append(line)

for line in matrix:
    [print(f'{num:>5}', end='') for num in line]
    print()
