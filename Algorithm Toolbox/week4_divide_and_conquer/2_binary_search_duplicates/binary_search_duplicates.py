def binary_search(keys, query):
    if not keys:
        return -1

    high = keys.index(max(keys))
    low = keys.index(min(keys))

    while high >= low:

        middle = (low + high) // 2

        if keys[middle] > query:
            high = middle - 1
        elif keys[middle] < query:
            low = middle + 1
        else:
            if middle - 1 < 0:
                return middle
            if keys[middle - 1] != query:
                return middle
            high = middle - 1
    return -1


if __name__ == "__main__":
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=" ")
