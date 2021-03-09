from ege_problem_solution.t23.n129 import solve
from tests.config import ASSETS_FOLDER


def test_solve():
    assert solve(3, 25, [12]) == 80
