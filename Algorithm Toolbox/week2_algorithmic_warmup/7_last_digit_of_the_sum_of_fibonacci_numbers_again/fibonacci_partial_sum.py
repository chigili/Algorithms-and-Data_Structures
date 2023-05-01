# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10


def fibonacci_mod(n):

    if n <= 1:
        return n

    a, b = 0, 1

    for i in range(n):
        a, b = b % 10, (a + b) % 10
    return a


def pisano_period(m):
    a, b = 0, 1
    for i in range(m * m):
        a, b = b % m, (a + b) % m
        if a == 0 and b == 1:
            return i + 1


def get_fibonacci_huge_mod(n, m):

    period = pisano_period(10)
    first_sum = fibonacci_mod(((n - 1) + 2) % period)
    last_sum = fibonacci_mod((m + 2) % period)

    if first_sum == 0:
        first_sum = 9
    first_sum = first_sum - 1

    if last_sum == 0:
        last_sum = 9
    last_sum = last_sum - 1

    sum_required = last_sum - first_sum
    return sum_required % 10


if __name__ == "__main__":
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_mod(n, m))
