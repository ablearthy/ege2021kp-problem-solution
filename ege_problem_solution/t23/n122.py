"""
(А.Н. Носкин) Исполнитель Калькулятор преобразует число на экране.
У исполнителя есть три команды, которым присвоены номера:
    1. Прибавить 2
    2. Прибавить 4
    3. Прибавить 5
Определите число, для получения которого из числа 31 существует 1001 программа.
"""


def solve(src: int, limit: int):
    commands = [lambda x: x + 2, lambda x: x + 4, lambda x: x + 5]
    max_len = 10_000
    dp = [0] * max_len
    dp[src] = 1
    for i in range(src, max_len):
        precalculated = [c(i) for c in commands]
        if dp[i] == limit:
            return i
        for c in precalculated:
            dp[c] += dp[i]
