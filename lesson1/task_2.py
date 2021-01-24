# 2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.

x1 = float(input('x1: '))
x2 = float(input('x2: '))
y1 = float(input('y1: '))
y2 = float(input('y2: '))

if x1 == x2:
    print(f'x = {x1}')
else:
    k = (y2 - y1) / (x2 - x1)
    b = y1 - x1 * k
    print(f"y = {k}x + {b}")
