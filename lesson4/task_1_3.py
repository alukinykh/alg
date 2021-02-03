# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
from random import randint
import cProfile

n = ''.join([str(randint(1, 9))] + [str(randint(0, 9)) for num in range(10001)])
print(n)


# len 11: 100 loops, best of 5: 1.82 usec per loop
# len 101: 100 loops, best of 5: 38.4 usec per loop
# len 1001: 100 loops, best of 5: 1.51 msec per loop

#   для длины 10001
#          4 function calls in 0.179 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.179    0.179 <string>:1(<module>)
#         1    0.179    0.179    0.179    0.179 task_1_3.py:13(count_number)
#         1    0.000    0.000    0.179    0.179 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
def count_number(n):
    odd = 0  # нечетные
    even = 0  # четные

    while n > 0:
        if (n % 10) % 2 == 0:
            even += 1
        else:
            odd += 1
        n = n // 10

    return odd, even


# len 11: 100 loops, best of 5: 2.89 usec per loop
# len 101: 100 loops, best of 5: 31.3 usec per loop
# len 1001: 100 loops, best of 5: 247 usec per loop

#   для длины 10001
#          4 function calls in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.003    0.003    0.003    0.003 task_1_3.py:40(count_number)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
def count_number(n):
    odd = 0
    even = 0
    for item in n:
        if (int(item) % 10) % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd, even


#  len 11: 1000 loops, best of 5: 6.5 usec per loop
#  len 101: 1000 loops, best of 5: 49.7 usec per loop
#  len 1001: 1000 loops, best of 5: 481 usec per loop

#   для длины 10001
#  20010 function calls in 0.012 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.012    0.012 <string>:1(<module>)
#         1    0.005    0.005    0.012    0.012 task_1_3.py:64(count_number)
#     10002    0.004    0.000    0.004    0.000 task_1_3.py:66(<lambda>)
#     10002    0.004    0.000    0.004    0.000 task_1_3.py:67(<lambda>)
#         1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
def count_number(n):
    arr = list(n)
    odd = len(list(filter(lambda x: (int(x) % 2 != 0), arr)))
    even = len(list(filter(lambda x: (int(x) % 2 == 0), arr)))
    return odd, even

# cProfile.run('count_number(n)')


