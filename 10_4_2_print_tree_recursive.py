class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


def print_tree(node):
    if node is None:
        return
    print_tree(node.left)
    print(node.key)
    print_tree(node.right)


def main():
    root = Node(18)
    root.left = Node(12)
    root.left.left = Node(7)
    root.left.right = Node(4)
    root.left.right.left = Node(5)
    root.right = Node(10)
    root.right.left = Node(2)
    root.right.right = Node(21)
    print_tree(root)


if __name__ == "__main__":
    main()
