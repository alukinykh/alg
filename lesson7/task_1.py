# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random

size = 10
new_arr = [random.randint(-100, 99) for _ in range(size)]
print(new_arr)


def reverse_bubble_sort(arr):
    n = 0
    while n < len(arr):
        updated = False
        for i in range(1, len(arr) - n):
            if arr[i] > arr[i - 1]:
                updated = True
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        if not updated:
            break
        n += 1
    return arr


print(reverse_bubble_sort(new_arr))

