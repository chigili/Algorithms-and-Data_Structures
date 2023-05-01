from sys import stdin
from itertools import chain


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover_fast(starts, ends, points):
    assert len(starts) == len(ends)
    start_cat, point_cat, end_cat = 0, 1, 2

    start_cor = zip(starts, [start_cat] * len(points), range(len(points)))
    point_cor = zip(points, [point_cat] * len(points), range(len(points)))
    end_cor = zip(ends, [end_cat] * len(points), range(len(points)))

    flat_array = chain(start_cor, point_cor, end_cor)
    sorted_array = sorted(flat_array, key=lambda x: (x[0], x[1]))

    segment = 0
    count = [0] * len(points)

    for cor, cat, index in sorted_array:
        if cat == 0:
            segment += 1
        elif cat == 2:
            segment -= 1
        else:
            count[index] = segment

    return count


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2 : 2 * n + 2 : 2], data[3 : 2 * n + 2 : 2]
    input_points = data[2 * n + 2 :]

    # output_count = points_cover_naive(input_starts, input_ends, input_points)
    # print(*output_count)
    print(*points_cover_fast(input_starts, input_ends, input_points))
