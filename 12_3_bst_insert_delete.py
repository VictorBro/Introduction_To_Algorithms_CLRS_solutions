class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
        self.parent = None


def in_order(node, nodes):
    if node is not None:
        in_order(node.left, nodes)
        nodes.append(node.key)
        in_order(node.right, nodes)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        prev = None
        curr = self.root
        while curr is not None:
            prev = curr
            if new_node.key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        new_node.parent = prev
        if prev is None:
            self.root = new_node
        elif new_node.key < prev.key:
            prev.left = new_node
        else:
            prev.right = new_node

    def find(self, key):
        node = self.root
        while node is not None and node.key != key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node

    def tree_min(self, node):
        if node is None:
            return node
        while node.left is not None:
            node = node.left
        return node

    def transplant(self, u, v):
        if u is None:
            return
        if u.parent is None:
            self.root = v
        elif u.parent.left == u:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def delete(self, node):
        # node has at most one child (right child)
        if node.left is None:
            self.transplant(node, node.right)
        # node has only left child
        elif node.right is None:
            self.transplant(node, node.left)
        # node has two children
        else:
            successor = self.tree_min(node.right)
            # successor is child of node
            if successor == node.right:
                self.transplant(node, successor)
                successor.left = node.left
                node.left.parent = successor
            # successor is descendant of node
            else:
                self.transplant(successor, successor.right)
                self.transplant(node, successor)
                successor.left = node.left
                node.left.parent = successor
                successor.right = node.right
                node.right.parent = successor

    def __str__(self):
        nodes = []
        in_order(self.root, nodes)
        return str(nodes)


def main():
    bst = BST()
    new_node = Node(5)
    bst.insert(new_node)
    new_node = Node(7)
    bst.insert(new_node)
    new_node = Node(6)
    bst.insert(new_node)
    new_node = Node(10)
    bst.insert(new_node)
    new_node = Node(8)
    bst.insert(new_node)
    new_node = Node(9)
    bst.insert(new_node)
    print(bst)
    node = bst.find(11)
    print(node.key) if node is not None else print("None")
    node = bst.find(10)
    print(node.key) if node is not None else print("None")
    node = bst.find(7)
    bst.delete(node)
    print(bst)
    node = bst.find(5)
    bst.delete(node)
    print(bst)


if __name__ == "__main__":
    main()
