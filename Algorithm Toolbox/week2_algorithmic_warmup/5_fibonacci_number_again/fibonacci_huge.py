def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def fibonacci_mod(n, m):

    if n <= 1:
        return n

    a, b = 0, 1

    for i in range(n):
        a, b = b % m, (a + b) % m
    return a


def pisano_period(m):
    a, b = 0, 1
    for i in range(m * m):
        a, b = b % m, (a + b) % m
        if a == 0 and b == 1:
            return i + 1


def get_fibonacci_huge_mod(n, m):

    period = pisano_period(m)
    return fibonacci_mod(n % period, m)


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(get_fibonacci_huge_mod(n, m))
