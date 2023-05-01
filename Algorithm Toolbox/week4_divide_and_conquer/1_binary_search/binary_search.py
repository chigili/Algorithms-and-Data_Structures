def binary_search(keys, query):

    if not keys:
        return -1

    high = keys.index(max(keys))
    low = keys.index(min(keys))

    if high < low:
        return low - 1

    middle = (low + high) // 2

    if keys[middle] == query:
        return middle
    elif keys[middle] > query:
        return binary_search(keys[:middle], query)
    else:
        return binary_search(keys[middle + 1 :], query)


if __name__ == "__main__":
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=" ")
