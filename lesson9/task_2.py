# 2. Закодируйте любую строку по алгоритму Хаффмана.
from collections import Counter


class Node:
    left = None
    right = None

    def __init__(self, weight, symbol=None):
        self.weight = weight
        self.symbol = symbol


def huffman(current_str):
    symbols = Counter({Node(weight, symbol): weight for symbol, weight in Counter(current_str).items()})

    while len(symbols) > 1:
        left, right = symbols.most_common()[-2:]
        node = Node(left[1] + right[1])
        node.left = left[0]
        node.right = right[0]
        del symbols[left[0]]
        del symbols[right[0]]
        symbols[node] = node.weight

    root = next(iter(symbols))
    table = {}

    def create_table(node, table, code=''):
        if node.symbol is not None:
            table[node.symbol] = code
        if node.left is not None:
            create_table(node.left, table, code + '1')
        if node.right is not None:
            create_table(node.right, table, code + '0')

    create_table(root, table)

    print(table)

    return ' '.join(table[i] for i in current_str)


print(huffman('hello world'))


