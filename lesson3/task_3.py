# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint

array_numbers = [randint(1, 99) for _ in range(10)]
max_num = array_numbers[0]
min_num = array_numbers[0]
max_index = 0
min_index = 0

print(array_numbers)

for key, num in enumerate(array_numbers):
    if num > max_num:
        max_num = num
        max_index = key
    if num < min_num:
        min_num = num
        min_index = key

array_numbers[max_index], array_numbers[min_index] = array_numbers[min_index], array_numbers[max_index]

print(min_num, min_index)
print(max_num, max_index)
print(array_numbers)
