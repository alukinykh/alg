# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random


size = 10
new_arr = [round(random.uniform(0, 50), 2) for _ in range(size)]
print(new_arr)


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    center = len(arr) // 2
    left = merge_sort(arr[:center])
    right = merge_sort(arr[center:])
    i = 0
    j = 0
    new_array = []
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            new_array.append(right[j])
            j += 1
        else:
            new_array.append(left[i])
            i += 1
    if i != len(left):
        new_array += left[i:]
    else:
        new_array += right[j:]

    return new_array


print(merge_sort(new_arr))
