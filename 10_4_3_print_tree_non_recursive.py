class TreeNode:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


class StackNode:
    def __init__(self, val):
        self.key = val
        self.next = None


class Stack:
    def __init__(self):
        self._top = None

    def push(self, val):
        node = StackNode(val)
        if self.empty():
            self._top = node
        else:
            node.next = self._top
            self._top = node

    def pop(self):
        if self.empty():
            raise Exception("Underflow")
        val = self._top.key
        self._top = self._top.next
        return val

    def empty(self):
        return self._top is None

    def top(self):
        return self._top.key

    def __str__(self):
        L = []
        x = self._top
        while x is not None:
            if x.key is not None:
                L.append(x.key.key)
            x = x.next
        return str(L)


def print_tree(root):
    if root is None:
        return
    S = Stack()
    S.push(root)
    while not S.empty():
        temp = S.top()
        while temp is not None:
            S.push(temp.left)
            temp = temp.left
        S.pop()
        if not S.empty():
            temp = S.pop()
            print(temp.key)
            S.push(temp.right)


def main():
    root = TreeNode(18)
    root.left = TreeNode(12)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(5)
    root.right = TreeNode(10)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(21)
    print_tree(root)


if __name__ == "__main__":
    main()
