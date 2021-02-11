"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в
рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным
использованием памяти.
Задача №2 из урока №2:
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число
34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

import sys

# Python 3.9.0
# OS 64bit


def get_variable_size(var):
    """Calculate variable's size."""
    size = sys.getsizeof(var)
    if hasattr(var, 'iter'):
        if hasattr(var, 'items'):
            for key, value in var.items():
                size += sys.getsizeof(key)
                size += sys.getsizeof(value)
        elif not isinstance(var, str):
            for item in var:
                size += sys.getsizeof(item)
    return size


# Вариант 1

number = 34560
odd = 0
even = 0
while number != 0:
    if (number % 10) % 2 == 0:
        even += 1
    else:
        odd += 1
    number //= 10

v_size = get_variable_size(number)
v_size += get_variable_size(odd)
v_size += get_variable_size(even)
print(f"Вариант 1. Переменные занимают {v_size} байт.")
# Вариант 1. Переменные занимают 80 байт.


# Вариант 2

number = 34560
odd = even = 0
evens = ("0", "2", "4", "6", "8")
for digit_str in str(number):
    if digit_str in evens:
        even += 1
    else:
        odd += 1

v_size = get_variable_size(number)
v_size += get_variable_size(odd)
v_size += get_variable_size(even)
v_size += get_variable_size(evens)
print(f"Вариант 2. Переменные занимают {v_size} байт.")
# Вариант 2. Переменные занимают 164 байт.


# Вариант 3

number = 34560
number_str = str(number)
odd = sum(int(i) % 2 for i in number_str)
even = len(number_str) - odd

v_size = get_variable_size(number)
v_size += get_variable_size(number_str)
v_size += get_variable_size(odd)
v_size += get_variable_size(even)
print(f"Вариант 3. Переменные занимают {v_size} байт.")
# Вариант 3. Переменные занимают 138 байт.


# Вывод:
# Первый вариант расходует меньше памяти, т.к. использует только int переменные.
# Второй вариант расходует больше всего памяти, т.к. кроме int переменных использует
# кортеж со строками.
# Третий вариант расходует больше памяти, чем первый, т.к. ипользует строку.
