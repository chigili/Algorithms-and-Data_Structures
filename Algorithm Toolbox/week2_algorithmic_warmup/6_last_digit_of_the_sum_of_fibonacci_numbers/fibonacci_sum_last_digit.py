def fibonacci_sum(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

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


def get_fibonacci_huge_mod(n):

    period = pisano_period(10)
    last_digit = fibonacci_mod((n + 2) % period)

    if last_digit == 0:
        return 9
    return last_digit - 1


if __name__ == "__main__":
    n = int(input())
    print(get_fibonacci_huge_mod(n))
