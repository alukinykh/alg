# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

count = int(input('Enter fabric count: '))

New_fabric = namedtuple('New_fabric', 'name, income')
all = []
sum = 0

for i in range(count):
    name = input('Enter name: ')
    income = int(input('Enter income: '))
    sum += income
    all.append(New_fabric(name, income))

average = sum / count
print(all)
print(average)

higher = []
lower = []
for item in all:
    if item.income > average:
        higher.append(item.name)
    else:
        lower.append(item.name)

print('More then average')
[print(name) for name in higher]
print('Less then average')
[print(name) for name in lower]
