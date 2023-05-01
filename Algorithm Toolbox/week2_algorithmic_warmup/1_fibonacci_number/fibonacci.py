def fibonacci_number(n):
    if n <= 1:
        return n

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)


def fibonacci_number_array(n):

    f = [0, 1]

    if n == 0:
        return f[0]

    elif n == 1:
        return f[1]

    elif n >= 2:
        for i in range(2, n + 1):
            f.append(f[i - 1] + f[i - 2])

    return f[i]


if __name__ == "__main__":
    input_n = int(input())
    print(fibonacci_number_array(input_n))
