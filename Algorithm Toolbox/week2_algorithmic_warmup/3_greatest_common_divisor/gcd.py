def gcd(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_fast(a, b):

    if b == 0:
        return a

    a_1 = a % b

    return gcd_fast(b, a_1)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_fast(a, b))
