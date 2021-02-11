import cProfile


def prime(n):
    arr = {1: 2, 2: 3}
    if n in arr:
        return arr[n]

    primes = [2, 3]

    j = 2
    while len(primes) < n:
        num = primes[-1] + j
        is_prime = True
        for el in primes:
            if num % el == 0:
                is_prime = False
                break

        if is_prime:
            j = 2
            primes.append(num)
        else:
            j += 2
    return primes[-1]


# for i in range(1, 10):
#     print(prime(i))
# print(prime(123))

# cProfile.run('prime(996)')
#          4937 function calls in 0.032 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.032    0.032 <string>:1(<module>)
#         1    0.031    0.031    0.032    0.032 task_2_2.py:4(prime)
#         1    0.000    0.000    0.032    0.032 {built-in method builtins.exec}
#      3939    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       994    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# n = 9: 1000 loops, best of 5: 4.19 usec per loop
# n = 50: 1000 loops, best of 5: 81.9 usec per loop
# n = 996: 1000 loops, best of 5: 25 msec per loop
