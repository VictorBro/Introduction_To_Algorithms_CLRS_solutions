class Node:
    def __init__(self, val, parent=None):
        self.key = val
        self.left = None
        self.right = None
        self.parent = parent


def print_tree(root):
    if root is None:
        return
    tmp = root
    while tmp is not None:
        prev = tmp
        while tmp.left is not None:
            prev = tmp
            tmp = tmp.left
        print(tmp.key)
        if prev != tmp:
            if tmp.parent is not None:
                tmp = tmp.parent
                print(tmp.key)
        if tmp.right is not None and tmp.right != prev:
            tmp = tmp.right
        else:
            while tmp is not None and (tmp.right is None or tmp.right == prev):
                prev = tmp
                tmp = tmp.parent
            if tmp is not None and tmp.right is not None and tmp.right != prev:
                print(tmp.key)
                tmp = tmp.right


def main():
    root = Node(18)
    root.left = Node(12, root)
    root.left.left = Node(7, root.left)
    root.left.right = Node(4, root.left)
    root.left.right.left = Node(5, root.left.right)
    root.right = Node(10, root)
    root.right.left = Node(2, root.right)
    root.right.right = Node(21, root.right)
    print_tree(root)


if __name__ == "__main__":
    main()
