from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0
    if capacity == 0 or not weights:
        return 0.0

    price = [v / w for v, w in zip(values, weights)]

    while capacity > 0:
        for i in range(len(weights)):
            max_price = max(price)
            max_index = price.index(max_price)
            price[max_index] = -999
            amount = min(capacity, weights[max_index])
            value += amount * max_price
            capacity -= amount
            weights[max_index] -= amount
        return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2 : (2 * n + 2) : 2]
    weights = data[3 : (2 * n + 2) : 2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
