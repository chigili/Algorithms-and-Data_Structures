# python3
from collections import deque

# def max_sliding_window_naive(sequence, m):
#     maximums = []
#     for i in range(len(sequence) - m + 1):
#         maximums.append(max(sequence[i:i + m]))

#     return maximums


def max_sliding_window(sequence, m):
    maximums = []
    deq = deque(maxlen=m)

    for i in range(len(sequence)):
        deq.append(sequence[i])
        if i >= m - 1:
            maximums.append(max(deq))
    return maximums


if __name__ == "__main__":
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))
