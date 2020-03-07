class TreeNode:
    def __init__(self, k, parent=None):
        self.key = k
        self.left = None
        self.right = None
        self.parent = parent


class BST:
    def __init__(self):
        self.root = None


def tree_min(node):
    while node.left is not None:
        node = node.left
    return node


def successor(node):
    if node.right is not None:
        return tree_min(node.right)
    parent = node.parent
    while parent is not None and parent.left != node:
        node = parent
        parent = node.parent
    return parent


def print_tree(root):
    node = tree_min(root)
    if node is not None:
        print(node.key)
    while node is not None:
        node = successor(node)
        if node is not None:
            print(node.key)


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
