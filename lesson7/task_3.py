# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

# from statistics import median
import random

size = 5
new_arr = [random.randint(1, 99) for _ in range(2 * size + 1)]
print(new_arr)
print(sorted(new_arr))


def find_median(arr, index=None):
    if index is None:
        index = len(arr) // 2
    median = arr[index]
    less = [el for el in arr if el < median]
    if len(less) > index:
        return find_median(less, index)
    index -= len(less)
    count = arr.count(median)
    if index < count:
        return median
    more = [el for el in arr if el > median]
    index -= count
    return find_median(more, index)


print(find_median(new_arr))


# for _ in range(1000):
#     new_arr = [random.randint(1, 99) for _ in range(2 * size + 1)]
#     assert find_median(new_arr) == median(new_arr)
# print("Test OK.")
