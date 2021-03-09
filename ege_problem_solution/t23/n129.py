"""
(Е. Джобс) Исполнитель ЛенивыйСчетовод преобразует число, записанное на экране. У исполнителя есть три команды,
которым присвоены номера:
    1. Прибавить 2
    2. Прибавить 3
    3. Дописать к числу справа 1
Первая команда увеличивает число на 2, вторая – на 3, третья – приписывает к текущему значению цифру 1 (например, для
10 результатом выполнения данной команды будет 101). Сколько существует таких программ, которые исходное число 3
преобразуют в число 25, при этом траектория вычислений содержит число 12?
"""
from typing import List


def solve(src: int, dst: int, points: List[int]):
    commands = [lambda x: x + 2, lambda x: x + 3, lambda x: 10 * x + 1]
    dp = [[] for _ in range(dst + 1)]
    dp[src] = [[]]
    for i in range(src, dst + 1):
        precalculated_values = [c(i) for c in commands]
        for cmd in dp[i]:
            for k, v in enumerate(precalculated_values):
                if v > dst:
                    continue
                dp[v].append(cmd + [k])
    out = dp[dst]
    counter = 0
    for sol in out:
        for point in points:
            counter += sum([sol[: len(x)] == x for x in dp[point]])
    return counter
