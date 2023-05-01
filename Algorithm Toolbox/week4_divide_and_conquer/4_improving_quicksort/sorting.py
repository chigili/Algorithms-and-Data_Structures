from random import randint


def partition3(array, left, right):
    # write your code here
    m1 = left
    i = left
    m2 = right
    pivot = array[left]

    while i <= m2:
        if array[i] < pivot:
            array[m1], array[i] = array[i], array[m1]
            m1 += 1
            i += 1
        elif array[i] > pivot:
            array[m2], array[i] = array[i], array[m2]
            m2 -= 1
        else:
            i += 1
    return [m1, m2]


def partition2(array, left, right):
    i = left
    j = right
    pivot = array[left]

    while i < j:
        while i < right and array[i] <= pivot:
            i += 1
        while j > left and array[j] > pivot:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]

    array[left], array[j] = array[j], array[left]
    return j


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    # k = 0
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    # m = partition2(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == "__main__":
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
