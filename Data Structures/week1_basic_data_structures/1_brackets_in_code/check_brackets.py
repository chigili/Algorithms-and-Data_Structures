# python3

from collections import namedtuple, deque

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = deque()
    for i, next in enumerate(text):
        if next in "([{":
            #     # Process opening bracket, write your code here
            stack.append(Bracket(next, i + 1))

        if next in ")]}":
            # Process closing bracket, write your code here
            pop_item = stack.pop()
            if are_matching(pop_item.char, next):
                continue
            return i + 1
    return "success" if len(stack) == 0 else stack[-1].position
    # return stack


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
