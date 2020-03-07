class Node:
    def __init__(self, flag=False):
        self.flag = flag
        self.left = None
        self.right = None


def print_tree(node, sorted_arr, char_arr):
    if node is not None:
        if node.flag:
            sorted_arr.append("".join(char_arr))
        print_tree(node.left, sorted_arr, char_arr + ["0"])
        print_tree(node.right, sorted_arr, char_arr + ["1"])


class BST:
    def __init__(self):
        self.root = Node()

    def insert(self, s):
        curr = self.root
        for ch in s:
            if ch == "0":
                next_node = curr.left
            else:
                next_node = curr.right

            if next_node is None:
                next_node = Node()
                if ch == "0":
                    curr.left = next_node
                else:
                    curr.right = next_node
            curr = next_node
        next_node.flag = True

    def __str__(self):
        sorted_arr = []
        char_arr = []
        print_tree(self.root, sorted_arr, char_arr)
        return str(sorted_arr)


def build_radix_tree(arr):
    bst = BST()
    for s in arr:
        bst.insert(s)
    return bst


def lexicographic_sort(arr):
    bst = build_radix_tree(arr)
    print(bst)


def main():
    arr = ["100", "10", "1011", "0", "011"]
    lexicographic_sort(arr)


if __name__ == "__main__":
    main()
