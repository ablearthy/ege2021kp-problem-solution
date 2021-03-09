from ege_problem_solution.t23.n125 import closest, solve


def test_closest():
    primes = [2, 3, 5, 7, 9, 11, 13, 17, 19]
    assert closest(primes, 2) == 2
    assert closest(primes, 4) == 5
    assert closest(primes, 3) == 3
    assert closest(primes, 14) == 17
    assert closest(primes, 15) == 17
    assert closest(primes, 18) == 19


def test_solve():
    assert solve(2, 45, [14], [33]) == 65
