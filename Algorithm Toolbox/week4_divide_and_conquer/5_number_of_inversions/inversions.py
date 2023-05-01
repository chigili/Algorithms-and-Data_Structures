from itertools import combinations


def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def merge(left_array, right_array):
    result = []
    i, j = 0, 0
    inv_count = 0

    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            result.append(left_array[i])
            i += 1
        else:
            result.append(right_array[j])
            j += 1
            inv_count += len(left_array) - i
    result += left_array[i:]
    result += right_array[j:]
    return result, inv_count


def merge_sort(array):
    if len(array) < 2:
        return array, 0
    else:
        middle = len(array) // 2
        left_array, inv_left = merge_sort(array[:middle])
        right_array, inv_right = merge_sort(array[middle:])
        merged, count = merge(left_array, right_array)
        count += inv_left + inv_right
        return merged, count


if __name__ == "__main__":
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions_naive(elements))
    print(merge_sort(elements)[1])
