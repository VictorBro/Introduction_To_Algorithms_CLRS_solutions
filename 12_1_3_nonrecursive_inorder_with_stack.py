class Node:
    def __init__(self, val, next_node=None):
        self.key = val
        self.next = next_node


class TreeNode:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, k):
        node = Node(k)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return None
        ret = self.top
        self.top = self.top.next
        return ret.key


class BST:
    def __init__(self):
        self.root = None


# def print_tree(node):
#     s = Stack()
#     while node is not None:
#         while node.left is not None:
#             s.push(node)
#             node = node.left
#         while True:
#             print(node.key)
#             node = node.right
#             if node is None and s.top is not None:
#                 node = s.pop()
#             else:
#                 break


def print_tree(node):
    s = Stack()
    while node is not None or s.top is not None:
        while node is not None:
            s.push(node)
            node = node.left
        node = s.pop()
        print(node.key)
        node = node.right


def main():
    bst = BST()
    bst.root = TreeNode(5)
    bst.root.left = TreeNode(2)
    bst.root.right = TreeNode(7)
    bst.root.left.left = TreeNode(1)
    bst.root.left.right = TreeNode(4)
    bst.root.left.right.left = TreeNode(3)
    bst.root.right.left = TreeNode(6)
    bst.root.right.right = TreeNode(8)
    bst.root.right.right.right = TreeNode(9)
    print_tree(bst.root)


if __name__ == "__main__":
    main()
