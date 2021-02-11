# 7. Написать программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n — любое натуральное число.

n = int(input('Enter number: '))

i = 1
left = 0

for i in range(1, n + 1):
    left += i

right = int(n * (n + 1) / 2)

if left == right:
    print(f'proof is true: {left} = {right}')
else:
    print(f'proof is false: {left} = {right}')
