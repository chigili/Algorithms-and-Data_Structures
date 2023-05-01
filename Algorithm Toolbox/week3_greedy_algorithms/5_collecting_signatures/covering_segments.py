from sys import stdin
from collections import namedtuple

Segment = namedtuple("Segment", "start end")


def optimal_points(segments):
    points = []
    segments.sort(key=lambda x: x.end)
    right_point = segments[0].end
    points.append(right_point)
    i = 1

    while i < len(segments):
        if segments[i].start > right_point:
            right_point = segments[i].end
            points.append(right_point)
        i += 1
    return points


if __name__ == "__main__":
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
