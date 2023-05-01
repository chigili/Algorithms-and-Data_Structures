def majority_element(input_elements):
    if not input_elements:
        return -1

    def majority_element_rec(left, right):
        if left == right:
            return input_elements[left]

        middle = left + (right - left) // 2

        left_partition = majority_element_rec(left, middle)
        right_partition = majority_element_rec(middle + 1, right)

        if left_partition == right_partition:
            return left_partition

        left_count = input_elements.count(left_partition)
        right_count = input_elements.count(right_partition)

        if left_count > right_count:
            return left_partition
        elif right_count > right_count:
            return right_partition

    return 1 if majority_element_rec(0, len(input_elements) - 1) is not None else 0


if __name__ == "__main__":
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
