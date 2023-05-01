def majority_element_naive(elements):
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element_dnc(elements):

    if not elements:
        return -1

    def majority_element_rec(left, right):

        if left == right:
            return elements[left]

        mid = left + (right - left) // 2

        left_partition = majority_element_rec(left, mid)
        right_partition = majority_element_rec(mid + 1, right)

        if left_partition == right_partition:
            return left_partition

        left_partition_count = sum(
            1 for i in range(left, right + 1) if elements[i] == left_partition
        )
        right_partition_count = sum(
            1 for i in range(left, right + 1) if elements[i] == right_partition
        )

        if left_partition_count > right_partition_count:
            return left_partition
        elif right_partition_count > left_partition_count:
            return right_partition

    return 1 if majority_element_rec(0, len(elements) - 1) else 0


if __name__ == "__main__":
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    # print(majority_element_naive(input_elements))
    print(majority_element_dnc(input_elements))
