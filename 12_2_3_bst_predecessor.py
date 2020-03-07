class TreeNode:
    def __init__(self, k, parent=None):
        self.key = k
        self.left = None
        self.right = None
        self.parent = parent


class BST:
    def __init__(self):
        self.root = None


def tree_max(node):
    while node.right is not None:
        node = node.right
    return node


def predecessor(node):
    if node.left is not None:
        return tree_max(node.left)
    parent = node.parent
    while parent is not None and parent.right != node:
        node = parent
        parent = node.parent
    return parent


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
    node = predecessor(bst.root.left.right.left)
    print(node.key)
    node = predecessor(bst.root.right)
    print(node.key)
    node = predecessor(bst.root.left.left)
    if node is None:
        print("None")
    else:
        print(node.key)
    node = predecessor(bst.root.right.left)
    print(node.key)
    node = predecessor(bst.root)
    print(node.key)


if __name__ == "__main__":
    main()
