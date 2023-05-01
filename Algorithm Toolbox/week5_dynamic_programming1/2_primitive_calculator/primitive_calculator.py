from typing import List


def compute_operations(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 0

    for i in range(2, n + 1):
        dp[i] = 1 + dp[i - 1]
        if i % 2 == 0:
            dp[i] = min(dp[i], 1 + dp[i // 2])
        if i % 3 == 0:
            dp[i] = min(dp[i], 1 + dp[i // 3])
    return dp[n], get_path(n, [])


def get_path(n: int, path: List) -> List:
    if n == 1:
        path.append(n)
        return path

    elif n % 3 == 0:
        path = get_path(n // 3, path)

    elif n % 2 == 0:
        path = get_path(n // 2, path)

    else:
        path = get_path(n - 1, path)

    path.append(n)

    return path


if __name__ == "__main__":
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(output_sequence[0])
    print(*output_sequence[1])
