"""
(Е. Джобс) Исполнитель Вычислитель преобразует число на экране.
У исполнителя есть две команды, которым присвоены номера:
    1. Прибавить 2
    2. Сделать простое
Первая команда увеличивает число на экране на 2, вторая – получает ближайшее бóльшее простое число.
Сколько существует программ, для которых при исходном числе 2 результатом является число 45 и при этом траектория
вычислений содержит число 14 и не содержит числа 33?
"""
from bisect import bisect_left
from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def closest(arr: List[int], n: int):
    pos = bisect_left(arr, n)
    return arr[pos]


def gen_primes(limit: int):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False

    for i, is_prime in enumerate(sieve):
        if sieve[i]:
            yield i
            for j in range(i ** 2, limit, i):
                sieve[j] = False


def solve(src: int, dst: int, contains: List[int], not_contains: List[int]):
    contains = set(contains)
    to_discover = []
    primes = list(gen_primes(dst * 2))
    root = Node(src)

    # note (вторая команда): если число простое, то нужно взять следующее, иначе далее дерево будет создаваться
    # бесконечно
    commands = [
        lambda x: x + 2,
        lambda x: closest(primes, x)
        if x not in primes
        else primes[primes.index(x) + 1],
    ]

    to_discover.append(root)

    while to_discover:
        node = to_discover.pop()
        precalculated = set([c(node.value) for c in commands])
        precalculated = list(
            filter(lambda x: x <= dst and x not in not_contains, precalculated)
        )
        node.children = [Node(x) for x in precalculated]
        to_discover.extend(node.children)
    counter = 0
    for e in get_lists(root, []):
        if contains.intersection(set(e)) == contains and e[-1] == dst:
            counter += 1
    return counter


def get_lists(node: Node, values):
    lst = []
    if not node.children:
        return [[*values, node.value]]
    for child in node.children:
        lst.extend(get_lists(child, values + [node.value]))
    return lst
