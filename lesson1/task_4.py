# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

letter1 = input('Введите первую букву:')
letter2 = input('Введите вторую букву:')

pos1 = ord(letter1) - 97
pos2 = ord(letter2) - 97

distance = abs(pos1 - pos2)

if distance > 0:
    distance -= 1
print(f'Позиция первой буквы: {pos1}')
print(f'Позиция второй буквы: {pos2}')
print(f'Количество букв {distance} между {letter1} и {letter2}')
