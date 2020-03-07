class TreeNode:
    def __init__(self, val, parent=None):
        self.key = val
        self.left = None
        self.right = None
        self.parent = parent


class BST:
    def __init__(self):
        self.root = None


def print_tree(node):
    prev = None
    while node is not None:
        if prev == node.left:
            print(node.key)
            if node.right is not None:
                node = node.right
            else:
                prev = node
                node = node.parent
        elif prev == node.right:
            prev = node
            node = node.parent
        else:
            while node.left is not None:
                node = node.left
            prev = node.left


def main():
    bst = BST()
    bst.root = TreeNode(5)
    bst.root.left = TreeNode(2, bst.root)
    bst.root.right = TreeNode(7, bst.root)
    bst.root.left.left = TreeNode(1, bst.root.left)
    bst.root.left.right = TreeNode(4, bst.root.left)
    bst.root.left.right.left = TreeNode(3, bst.root.left.right)
    bst.root.right.left = TreeNode(6, bst.root.right)
    bst.root.right.right = TreeNode(8, bst.root.right)
    bst.root.right.right.right = TreeNode(9, bst.root.right.right)
    print_tree(bst.root)


if __name__ == "__main__":
    main()
