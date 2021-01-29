# 4. Определить, какое число в массиве встречается чаще всего.
from random import randint

array_numbers = [randint(1, 10) for _ in range(20)]
repeat_number = 0
count = 0

print(array_numbers)

for num in set(array_numbers):
    if array_numbers.count(num) > count:
        repeat_number = num
        count = array_numbers.count(num)

print(f'Number {repeat_number} repeats {count} times')