# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
from math import ceil, log
import cProfile


def prime(n):
    n = int(n)
    if n == 1:
        return 2
    limit = 3 + ceil(n * log(n * log(n)))
    primary_arr = [True] * limit
    count = 1
    for el in range(3, limit, 2):
        if primary_arr[el]:
            count += 1
            if count == n:
                return el
            for i in range(el*2, limit, el):
                primary_arr[i] = False


# for i in range(1, 10):
#     print(prime(i))
# print(prime(996))


#          7 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 task_2_1.py:8(prime)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method math.ceil}
#         2    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile.run('prime(996)')

# n = 9: 1000 loops, best of 5: 3.97 usec per loop
# n = 50: 1000 loops, best of 5: 26 usec per loop
# n = 996: 1000 loops, best of 5: 1.12 msec per loop
