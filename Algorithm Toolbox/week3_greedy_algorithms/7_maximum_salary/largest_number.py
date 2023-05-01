from itertools import permutations
import math


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def is_greater_or_equal(digit, max_digit):
    return int(digit + max_digit) >= int(max_digit + digit)


def largest_number_opt(numbers):
    res = ""

    while numbers:
        max_digit = 0
        for digit in numbers:
            if is_greater_or_equal(digit, str(max_digit)):
                max_digit = digit
                res += str(max_digit)
                numbers.remove(digit)
    return res


if __name__ == "__main__":
    _ = int(input())
    input_numbers = input().split()
    # print(largest_number_naive(input_numbers))
    print(largest_number_opt(input_numbers))
