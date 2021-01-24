# 1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

res_and = 5 & 6
res_or = 5 | 6
res_xor = 5 ^ 6
res_left = 5 << 2
res_right = 5 >> 2

print(f'5 & 6 = {res_and}')
print(f'5 | 6 = {res_or}')
print(f'5 ^ 6 = {res_xor}')
print(f'5 << 6 = {res_left}')
print(f'5 >> 6 = {res_right}')
