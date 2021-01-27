# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

count = int(input('Enter count of numbers: '))
max_sum = 0
max_number = 0

for i in range(count):
    number = int(input('Enter number: '))
    current_number = number
    current_sum = 0
    while number > 0:
        current_sum += number % 10
        number //= 10
    if current_sum > max_sum:
        max_sum = current_sum
        max_number = current_number

print(f'Number {max_number} has total sum {max_sum}')

