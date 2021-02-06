# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque

numbers_list = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']


def hex_sum(a, b):
    first = deque(a)
    second = deque(b)
    third = deque()
    if len(b) > len(a):
        first, second = second, first

    k = 0

    for item in range(len(first)):
        one = numbers_list.index(first.pop())
        try:
            two = numbers_list.index(second.pop())
        except IndexError:
            two = 0
        index_sum = one + two + k
        third.appendleft(numbers_list[index_sum % 16])
        k = index_sum // 16
    if k == 1:
        third.appendleft('1')

    return list(third)


# print(hex_sum(['A', '2'], ['C', '4', 'F']))
# print(hex_sum(['E', '2'], ['C', 'E', 'F']))
# print(hex_sum(['F', 'F', 'F'], ['F', 'F', 'F']))
# ['C', 'F', '1']
# ['D', 'D', '1']
# ['1', 'F', 'F', 'E']


def hex_mul(a, b):
    first = deque(a)
    second = deque(b)
    third = deque('0')

    if len(b) > len(a):
        first, second = second, first

    i = 0
    while len(second):
        current_num = second.pop()
        n = numbers_list.index(current_num)
        sum_nums = first
        for _ in range(n - 1):
            sum_nums = hex_sum(first, sum_nums)
        sum_nums.extend('0' * i)
        third = hex_sum(third, sum_nums)

        i += 1
    return third


# print(hex_mul(['A', '2'], ['C', '4', 'F']))
# print(hex_mul(['F', 'F', 'F'], ['F', 'F', 'F']))

a = list(input('Enter a: ').upper())
b = list(input('Enter b: ').upper())
print(f'Sum: {hex_sum(a, b)}')
print(f'Mul: {hex_mul(a, b)}')
