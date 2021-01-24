# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random

rand_type = input('Введите тип данных (int, str, float): ')
start = input('Диапазон от: ')
end = input('Диапазон до: ')

if rand_type == 'int':
    result = random.randint(int(start), int(end))
elif rand_type == 'float':
    result = random.uniform(float(start), float(end))
else:
    result = chr(random.randint(ord(start.lower()), ord(end.lower())))
print(f'Случайное значение от {start} до {end}: {result}')
