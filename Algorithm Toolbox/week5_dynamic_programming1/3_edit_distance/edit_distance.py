def edit_distance(first_string, second_string):
    n = len(first_string)
    m = len(second_string)

    dp = [[0 for i in range(m + 1)] for i in range(n + 1)]

    for index, _ in enumerate(dp):
        dp[index][0] = index

    for index, _ in enumerate(dp[0]):
        dp[0][index] = index

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if first_string[i - 1] == second_string[j - 1]:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1])
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

    return dp[n][m]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
