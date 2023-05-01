import math


def change(n):
    # write your code here
    coins = [1, 3, 4]
    dp = [0 for i in range(n + 1)]
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = math.inf
        for k in coins:
            if i - k < 0:
                continue
            dp[i] = min(dp[i], 1 + dp[i - k])
    return dp[n]


if __name__ == "__main__":
    m = int(input())
    print(change(m))
