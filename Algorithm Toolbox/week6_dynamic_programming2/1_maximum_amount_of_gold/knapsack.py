import numpy as np

from sys import stdin


def maximum_gold(capacity, weights):
    n = len(weights)
    dp = np.zeros((n + 1, capacity + 1))

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            dp[i][j] = dp[i - 1][j]

            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - weights[i - 1]] + weights[i - 1])
    return dp[n][capacity]


if __name__ == "__main__":
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
