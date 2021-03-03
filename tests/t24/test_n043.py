from ege_problem_solution.t24.n043 import solve
from tests.config import ASSETS_FOLDER


def test_solve():
    with open(ASSETS_FOLDER / "24data" / "k7data" / "k7-m5.txt", "r") as f:
        line = f.readline().strip()
    result = solve(line)
    assert result.total == 18
    assert result.original == "AAACCAAABBBCBBB BBBCCCCCCABCCCC"
    assert result.modified == "AAA2ccAAABBB1cB B6ccccccAB4cccc"
