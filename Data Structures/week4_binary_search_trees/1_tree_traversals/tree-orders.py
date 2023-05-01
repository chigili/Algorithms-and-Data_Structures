# python3

import sys, threading

sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrderTraversal(self, vertex, index):
        idx = vertex[index]
        if idx == -1 or idx > len(self.key):
            return
        self.inOrderTraversal(self.left, idx)
        self.result.append(self.key[idx])
        self.inOrderTraversal(self.right, idx)

    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        if self.key:
            self.inOrderTraversal(self.left, 0)
            self.result.append(self.key[0])
            self.inOrderTraversal(self.right, 0)
        return self.result

    def preOrderTraversal(self, vertex, index):
        idx = vertex[index]
        if idx == -1 or idx > len(self.key):
            return
        self.result.append(self.key[idx])
        self.preOrderTraversal(self.left, idx)
        self.preOrderTraversal(self.right, idx)

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        if self.key:
            self.result.append(self.key[0])
            self.preOrderTraversal(self.left, 0)
            self.preOrderTraversal(self.right, 0)

        return self.result

    def postOrderTraversal(self, vertex, index):
        idx = vertex[index]
        if idx == -1 or idx > len(self.key):
            return
        self.postOrderTraversal(self.left, idx)
        self.postOrderTraversal(self.right, idx)
        self.result.append(self.key[idx])

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        if self.key:
            self.postOrderTraversal(self.left, 0)
            self.postOrderTraversal(self.right, 0)
            self.result.append(self.key[0])

        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
