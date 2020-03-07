class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
        self.successor = None


def tree_min(node):
    while node is not None and node.left is not None:
        node = node.left
    return node


def traverse(node, arr):
    if node is not None:
        arr.append(node.key)
        traverse(node.successor, arr)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        parent = None
        curr = self.root
        while curr is not None:
            parent = curr
            if new_node.key < curr.key:
                if new_node.successor is None or new_node.successor.key > curr.key:
                    new_node.successor = curr
                curr = curr.left
            else:
                if curr.successor is None or curr.successor.key > new_node.key:
                    curr.successor = new_node
                curr = curr.right
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    def search(self, key):
        node = self.root
        while node is not None and node.key != key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node

    def get_parent(self, node):
        prev = None
        curr = self.root
        while curr is not None and curr != node:
            prev = curr
            if node.key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return prev

    def predecessor(self, node):
        pred = None
        curr = self.root
        while curr is not None:
            if curr.key < node.key:
                if pred is None or pred.key < curr.key:
                    pred = curr
                curr = curr.right
            else:
                curr = curr.left
        return pred

    def transplant(self, u, v):
        if u is None:
            return
        u_parent = self.get_parent(u)
        if u_parent is None:
            self.root = v
        elif u_parent.left == u:
            u_parent.left = v
        else:
            u_parent.right = v

    def update_predecessor(self, node):
        predecessor = self.predecessor(node)
        if predecessor is not None:
            predecessor.successor = node.successor

    def delete(self, node):
        if node is None:
            return
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            if node.right == node.successor:
                self.transplant(node, node.right)
                node.right.left = node.left
            else:
                self.transplant(node.successor, node.successor.right)
                self.transplant(node, node.successor)
                node.successor.right = node.right
                node.successor.left = node.left
        self.update_predecessor(node)

    def __str__(self):
        arr = []
        traverse(tree_min(self.root), arr)
        return str(arr)


def main():
    bst = BST()
    new_node = Node(5)
    bst.insert(new_node)
    new_node = Node(3)
    bst.insert(new_node)
    new_node = Node(4)
    bst.insert(new_node)
    new_node = Node(9)
    bst.insert(new_node)
    new_node = Node(7)
    bst.insert(new_node)
    new_node = Node(8)
    bst.insert(new_node)
    new_node = Node(10)
    bst.insert(new_node)
    print(bst)
    node = bst.search(5)
    bst.delete(node)
    print(bst)
    node = bst.search(10)
    bst.delete(node)
    print(bst)


if __name__ == "__main__":
    main()
