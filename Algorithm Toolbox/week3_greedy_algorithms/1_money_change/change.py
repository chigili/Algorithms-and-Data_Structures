def change(money):

    denom = [10, 5, 1]
    coins = 0

    for i in denom:
        if money >= i:
            coins = coins + (money // i)
            money = money % i
    return coins


if __name__ == "__main__":
    m = int(input())
    print(change(m))
