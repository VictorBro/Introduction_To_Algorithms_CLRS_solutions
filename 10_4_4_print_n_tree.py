class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.sibling = None


def print_tree(node):
    if node is not None:
        print_tree(node.left)
        print(node.key)
        print_tree(node.sibling)


def main():
    root = Node(1)
    root.left = Node(2)
    root.left.sibling = Node(3)
    root.left.sibling.sibling = Node(4)
    root.left.left = Node(10)
    root.left.left.sibling = Node(5)
    root.left.left.sibling.left = Node(6)
    root.left.sibling.left = Node(7)
    root.left.sibling.left.sibling = Node(8)
    root.left.sibling.left.sibling.sibling = Node(9)
    print_tree(root)


if __name__ == "__main__":
    main()
