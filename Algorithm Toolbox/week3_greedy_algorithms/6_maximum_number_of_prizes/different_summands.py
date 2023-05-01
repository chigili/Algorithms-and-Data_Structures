def optimal_summands(n):
    summands = []
    if n == 0:
        return 0

    i = 1
    while n > 0:
        if n == i:
            summands.append(i)
            break
        if n - i <= i:
            i += 1
        else:
            summands.append(i)
            n -= i
            i += 1

    return summands


if __name__ == "__main__":
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
