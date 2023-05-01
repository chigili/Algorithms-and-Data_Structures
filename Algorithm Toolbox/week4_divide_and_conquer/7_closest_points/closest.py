from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple("Point", "x y")


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared, distance_squared(p, q))

    return min_distance_squared


def closest_pair_sol(input_points):

    sorted_x = sorted(input_points, key=lambda x: x.x)
    sorted_y = sorted(input_points, key=lambda x: x.y)
    d = closest_distance_pair(sorted_x, sorted_y)
    return d


def closest_distance_pair(sorted_x, sorted_y):
    n = len(sorted_x)

    ## base classes
    if n == 2:
        return distance_squared(sorted_x[0], sorted_x[1])

    if n == 3:
        return minimum_distance_squared_naive(sorted_x)

    ## divide
    mid = n // 2

    x_sorted_left = sorted_x[:mid]
    x_sorted_right = sorted_x[mid:]

    y_sorted_left = [x for x in sorted_y if x in x_sorted_left]
    y_sorted_right = [x for x in sorted_y if x in x_sorted_right]

    dl = closest_distance_pair(x_sorted_left, y_sorted_left)
    dr = closest_distance_pair(x_sorted_right, y_sorted_right)
    d = min(dl, dr)

    ## combine
    mx_x = sorted_x[mid][0]
    S = [x for x in sorted_y if mx_x - d <= x.x <= mx_x + d]
    len_S = len(S)

    for i in range(len_S - 1):
        for j in range(i + 1, min(i + 5, len_S)):
            d = min(d, distance_squared(S[i], S[j]))
    return d


if __name__ == "__main__":
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))
    print("{0:.9f}".format(sqrt(closest_pair_sol(input_points))))
