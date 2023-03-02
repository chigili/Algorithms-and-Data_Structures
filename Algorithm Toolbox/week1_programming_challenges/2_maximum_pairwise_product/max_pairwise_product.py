from random import randrange


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast(numbers):
    n = len(numbers)

    max_index1 = -1
    for i in range(n):
        if max_index1 == -1 or numbers[i] > numbers[max_index1]:
            max_index1 = i

    max_index2 = -1
    for j in range(n):
        if (j != max_index1) and (max_index2 == -1 or numbers[j] > numbers[max_index2]):
            max_index2 = j

    return numbers[max_index1] * numbers[max_index2]


def stress_test(n):
    """Stress test for MaX Pairwise Product

    Args:
        n (int): input size end boundary
    """
    while True:
        input_size = randrange(2, n)
        inputs = [randrange(0, 9) for i in range(input_size)]

        print(f"n = {input_size}")
        print(f"A = {inputs}")

        naive_pro = max_pairwise_product(inputs)
        fast_pro = max_pairwise_product_fast(inputs)

        if naive_pro != fast_pro:
            print(f"naive_pro = {naive_pro}")
            print(f"fast_pro = {fast_pro}")
            break

        elif naive_pro == fast_pro:
            print(f"naive_pro = {naive_pro}")
            print(f"fast_pro = {fast_pro}")
            print("OK")


if __name__ == "__main__":
    # _ = int(input())
    # input_numbers = list(map(int, input().split()))
    # print(max_pairwise_product_fast(input_numbers))
    input_size = int(input())
    stress_test(input_size)
