# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.
from functools import reduce

n = 10
graph = []
sum_all = 0

for i in range(n):
    graph.append([1 if j != i else 0 for j in range(n)])

for i in graph:
    sum_all += reduce((lambda x, y: x + y), i)

for row in graph:
    print(row)
print(sum_all)
