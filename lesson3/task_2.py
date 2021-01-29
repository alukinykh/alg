# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.

from random import randint


array_numbers = [randint(1, 99) for _ in range(10)]
array_index = [key for key, num in enumerate(array_numbers) if num % 2 == 0]

print(array_numbers)
print(array_index)
