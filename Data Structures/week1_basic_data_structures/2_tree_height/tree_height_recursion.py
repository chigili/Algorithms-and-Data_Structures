from collections import deque
from dataclasses import dataclass


@dataclass
class Node:
    val: int = None
    left: "Node" = None
    right: "Node" = None


class Solution:
    def height(self, root: Node, H: int = 0):
        if not root:
            return 0

        queue = deque([])
        queue.append(root)

        while queue:
            H += 1
            _next = deque([])
            while queue:
                node = queue.popleft()
                if node.left is not None:
                    _next.append(node.left)
                if node.right is not None:
                    _next.append(node.right)
            queue = _next
        return H


class RecursiveSolution:
    def height(self, root: Node):
        return self.recur_height(root)

    def recur_height(self, root: Node, H: int = 0):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))


if __name__ == "__main__":
    n = int(input())
    parents = list(map(int, input().split()))
    B = [Node(i) for i in range(n)]

    for child, parent in enumerate(parents):
        if 0 <= parent:
            if B[parent].left == None:
                B[parent].left = B[child]
            else:
                B[parent].right = B[child]
        else:
            root = B[child]

sol = Solution()
r_sol = RecursiveSolution()
print(sol.height(root))
print(r_sol.height(root))
