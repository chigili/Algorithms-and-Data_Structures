from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(
            first_sequence[i] * permutation[i] for i in range(len(first_sequence))
        )
        max_product = max(max_product, dot_product)

    return max_product


class Solution:
    def __init__(self, prices, clicks):
        self.prices = prices
        self.clicks = clicks

    def maxRevenue(self):
        self.prices.sort(reverse=True)
        self.clicks.sort(reverse=True)

        rev = 0

        for i in range(len(self.prices)):
            rev += self.prices[i] * self.clicks[i]

        return rev


if __name__ == "__main__":
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    solution = Solution(prices, clicks)
    print(max_dot_product(prices, clicks))
    print(solution.maxRevenue())
