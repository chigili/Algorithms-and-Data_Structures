def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    previous, current, sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


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


def get_fibonacci_sum_sq_fast(n):

    period = pisano_period(10)
    length = fibonacci_mod(n % period) + fibonacci_mod((n - 1) % period)
    breadth = fibonacci_mod(n % period)

    return (length * breadth) % 10


if __name__ == "__main__":
    n = int(input())
    print(get_fibonacci_sum_sq_fast(n))
