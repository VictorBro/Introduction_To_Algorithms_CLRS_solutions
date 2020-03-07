class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
        self.parent = None


def in_order(node, arr):
    if node is not None:
        in_order(node.left, arr)
        arr.append(node.key)
        in_order(node.right, arr)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, node):
        parent = None
        curr = self.root
        while curr is not None:
            parent = curr
            if node.key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node
        node.parent = parent

    def insert_recursive(self, curr, new_node):
        if curr is None:
            self.root = new_node
            return
        if new_node.key < curr.key:
            if curr.left is None:
                curr.left = new_node
                new_node.parent = curr
            else:
                self.insert_recursive(curr.left, new_node)
        else:
            if curr.right is None:
                curr.right = new_node
                new_node.parent = curr
            else:
                self.insert_recursive(curr.right, new_node)

    def __str__(self):
        node = self.root
        arr = []
        in_order(node, arr)
        return str(arr)


def main():
    bst = BST()
    new_node = Node(5)
    bst.insert_recursive(bst.root, new_node)
    new_node = Node(7)
    bst.insert_recursive(bst.root, new_node)
    new_node = Node(6)
    bst.insert_recursive(bst.root, new_node)
    new_node = Node(10)
    bst.insert_recursive(bst.root, new_node)
    new_node = Node(8)
    bst.insert_recursive(bst.root, new_node)
    new_node = Node(9)
    bst.insert_recursive(bst.root, new_node)
    print(bst)


if __name__ == "__main__":
    main()
