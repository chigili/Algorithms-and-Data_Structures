from sys import stdin


def partition3(values):

    lookup = {}
    total = sum(values)

    if total % 3 != 0:
        return False
    else:
        return subsetSum(
            values, len(values) - 1, total // 3, total // 3, total // 3, lookup
        )


def subsetSum(S, n, a, b, c, lookup):
    # return true if the subset is found
    if a == 0 and b == 0 and c == 0:
        return True

    # base case: no items left
    if n < 0:
        return False

    # construct a unique key from dynamic elements of the input
    key = (a, b, c, n)

    # if the subproblem is seen for the first time, solve it and
    # store its result in a dictionary
    if key not in lookup:

        # Case 1. The current item becomes part of the first subset
        A = False
        if a - S[n] >= 0:
            A = subsetSum(S, n - 1, a - S[n], b, c, lookup)

        # Case 2. The current item becomes part of the second subset
        B = False
        if not A and (b - S[n] >= 0):
            B = subsetSum(S, n - 1, a, b - S[n], c, lookup)

        # Case 3. The current item becomes part of the third subset
        C = False
        if (not A and not B) and (c - S[n] >= 0):
            C = subsetSum(S, n - 1, a, b, c - S[n], lookup)

        # return true if we get a solution
        lookup[key] = A or B or C

    # return the subproblem solution from the dictionary
    # return lookup[key]
    return lookup[key]


if __name__ == "__main__":
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    # print(1 if partition3(input_values) else 0)
    print(partition3(input_values))
