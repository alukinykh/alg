# 4. Определить, какое число в массиве встречается чаще всего.
from random import randint
import cProfile

array_nums = [randint(1, 10) for _ in range(1000000)]


# len 20: 100 loops, best of 5: 6.58 usec per loop
# len 100: 100 loops, best of 5: 23.1 usec per loop
# len 1000: 100 loops, best of 5: 183 usec per loop

# 18 function calls in 0.195 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.195    0.195 <string>:1(<module>)
#         1    0.012    0.012    0.195    0.195 task_1_2.py:23(repeated_number)
#         1    0.000    0.000    0.195    0.195 {built-in method builtins.exec}
#        14    0.183    0.013    0.183    0.013 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
def repeated_number(array_numbers):
    count = 0
    repeat_number = 0

    for num in set(array_numbers):
        if array_numbers.count(num) > count:
            repeat_number = num
            count = array_numbers.count(num)
    return repeat_number


# len 20: 100 loops, best of 5: 2.75 usec per loop
# len 100: 100 loops, best of 5: 12.8 usec per loop
# len 1000: 100 loops, best of 5: 105 usec per loop

#          5 function calls in 0.116 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.116    0.116 <string>:1(<module>)
#         1    0.116    0.116    0.116    0.116 task_1_2.py:46(repeated_number)
#         1    0.000    0.000    0.116    0.116 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
def repeated_number(array_numbers):
    arr = {}

    for num in array_numbers:
        if num in arr:
            arr[num] += 1
        else:
            arr[num] = 1
    return max(arr, key=arr.get)


# len 20: 100 loops, best of 5: 4.54 usec per loop
# len 100: 100 loops, best of 5: 20.3 usec per loop
# len 1000: 100 loops, best of 5: 145 usec per loop

#          5 function calls in 0.157 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.157    0.157 <string>:1(<module>)
#         1    0.013    0.013    0.157    0.157 task_1_2.py:59(repeated_number)
#         1    0.000    0.000    0.157    0.157 {built-in method builtins.exec}
#         1    0.144    0.144    0.144    0.144 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
def repeated_number(array_numbers):
    return max(set(array_numbers), key=array_numbers.count)


cProfile.run('repeated_number(array_nums)')
