# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def sift_down(arr, N, i, swaps):
    minimum = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < N and arr[l] < arr[minimum]:
        minimum = l

    if r < N and arr[r] < arr[minimum]:
        minimum = r

    if i != minimum:
        arr[i], arr[minimum] = arr[minimum], arr[i]
        swaps.append((i, minimum))
        sift_down(arr, N, minimum, swaps)
    return arr, swaps


def build_heap_fast(data):
    N = len(data)
    start_index = (N // 2) - 1
    swaps = []

    for i in range(start_index, -1, -1):
        data, swaps_ = sift_down(data, N, i, [])
        swaps.extend(swaps_)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap_fast(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
