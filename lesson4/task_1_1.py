# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint
import cProfile

array_numbers = [randint(1, 99) for _ in range(1000000)]


# len 10: 100 loops, best of 5: 1.29 usec per loop
# len 100: 100 loops, best of 5: 7.39 usec per loop
# len 1000: 100 loops, best of 5: 68.4 usec per loop

# Размер массива: 1000000
#          4 function calls in 0.071 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.071    0.071 <string>:1(<module>)
#         1    0.071    0.071    0.071    0.071 task_1_1.py:11(change_max_and_min)
#         1    0.000    0.000    0.071    0.071 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
def change_max_and_min(arr_numbers):
    max_num = array_numbers[0]
    min_num = array_numbers[0]
    max_index = 0
    min_index = 0

    for key, num in enumerate(array_numbers):
        if num > max_num:
            max_num = num
            max_index = key
        if num < min_num:
            min_num = num
            min_index = key

    array_numbers[max_index], array_numbers[min_index] = array_numbers[min_index], array_numbers[max_index]
    return arr_numbers


# len 10: 100 loops, best of 5: 1.32 usec per loop
# len 100: 100 loops, best of 5: 5.99 usec per loop
# len 1000: 100 loops, best of 5: 39.3 usec per loop

# Размер массива: 1000000
#       8 function calls in 0.037 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.037    0.037 <string>:1(<module>)
#      1    0.000    0.000    0.037    0.037 task_1_1.py:32(change_max_and_min)
#      1    0.000    0.000    0.037    0.037 {built-in method builtins.exec}
#      1    0.019    0.019    0.019    0.019 {built-in method builtins.max}
#      1    0.018    0.018    0.018    0.018 {built-in method builtins.min}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
def change_max_and_min(arr_numbers):
    max_num = max(arr_numbers)
    min_num = min(arr_numbers)

    max_index = arr_numbers.index(max_num)
    min_index = array_numbers.index(min_num)

    array_numbers[max_index], array_numbers[min_index] = array_numbers[min_index], array_numbers[max_index]
    return arr_numbers


# len 10: 100 loops, best of 5: 1.3 usec per loop
# len 100: 100 loops, best of 5: 6.53 usec per loop
# len 1000: 100 loops, best of 5: 99.1 usec per loop

# Размер массива: 1000000
#       8 function calls in 0.136 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.002    0.002    0.136    0.136 <string>:1(<module>)
#      1    0.000    0.000    0.135    0.135 task_1_1.py:61(change_max_and_min)
#      1    0.000    0.000    0.136    0.136 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.134    0.134    0.134    0.134 {built-in method builtins.sorted}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
def change_max_and_min(arr_numbers):
    sorted_arr = sorted(arr_numbers)
    min_index = array_numbers.index(sorted_arr[0])
    max_index = array_numbers.index(sorted_arr[len(sorted_arr)-1])
    array_numbers[max_index], array_numbers[min_index] = array_numbers[min_index], array_numbers[max_index]
    return arr_numbers


# change_max_and_min(array_numbers)

cProfile.run('change_max_and_min(array_numbers)')
