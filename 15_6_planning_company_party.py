# https://docs.google.com/file/d/0B8Xe-7jQARRnaGZiMlZmQld2UTQ/edit


class Node:
    def __init__(self, employ_id, score):
        self.id = employ_id
        self.score = score
        self.left_child = None
        self.right_sibling = None


class ScoreNode(Node):
    def __init__(self, employ_id, score, include_score, exclude_score):
        super().__init__(employ_id, score)
        self.include_score = include_score
        self.exclude_score = exclude_score
        self.left_child = None
        self.right_sibling = None


def tree_traverse(node, result_list):
    if node is not None:
        result_list.append((node.id, node.score))
        tree_traverse(node.left_child, result_list)
        tree_traverse(node.right_sibling, result_list)


class Tree:
    def __init__(self):
        self.root = None

    def __str__(self):
        result_list = []
        tree_traverse(self.root, result_list)
        return str(result_list)


def init_score_tree(node, score_tree, prev_new_node, is_left_child):
    if node is not None:
        new_node = ScoreNode(node.id, node.score, node.score, 0)
        if score_tree.root is None:
            score_tree.root = new_node
        if prev_new_node is not None:
            if is_left_child:
                prev_new_node.left_child = new_node
            else:
                prev_new_node.right_sibling = new_node
        init_score_tree(node.left_child, score_tree, new_node, True)
        init_score_tree(node.right_sibling, score_tree, new_node, False)


def find_max_conviviality(node):
    if node is not None:
        find_max_conviviality(node.left_child)
        find_max_conviviality(node.right_sibling)

        temp_node = node.left_child
        while temp_node is not None:
            node.include_score += temp_node.exclude_score
            if temp_node.left_child is not None:
                node.exclude_score += max(temp_node.include_score, temp_node.exclude_score)
            else:
                node.exclude_score += temp_node.include_score
            temp_node = temp_node.right_sibling


def score_tree_traverse(node):
    if node is not None:
        print("(", node.id, node.score, node.include_score, node.exclude_score, ")", end=" ")
        score_tree_traverse(node.left_child)
        score_tree_traverse(node.right_sibling)


def construct_guest_list(node, party_guest_list):
    if node is not None:
        if node.left_child is not None:
            if node.include_score >= node.exclude_score:
                party_guest_list.append((node.id, node.score))
                child_node = node.left_child
                while child_node is not None:
                    grandchild_node = child_node.left_child
                    while grandchild_node is not None:
                        construct_guest_list(grandchild_node, party_guest_list)
                        grandchild_node = grandchild_node.right_sibling
                    child_node = child_node.right_sibling
            else:
                child_node = node.left_child
                while child_node is not None:
                    construct_guest_list(child_node, party_guest_list)
                    child_node = child_node.right_sibling
        else:
            party_guest_list.append((node.id, node.score))


def guest_list(root):
    score_tree = Tree()
    init_score_tree(root, score_tree, None, False)
    print(score_tree)
    find_max_conviviality(score_tree.root)
    score_tree_traverse(score_tree.root)
    print()
    party_guest_list = []
    construct_guest_list(score_tree.root, party_guest_list)
    print(party_guest_list)


def main():  # O(n)
    t = Tree()
    t.root = Node(11, 2)
    t.root.left_child = Node(12, 1)
    t.root.left_child.right_sibling = Node(13, 3)
    t.root.left_child.right_sibling.right_sibling = Node(14, 5)
    t.root.left_child.right_sibling.left_child = Node(15, 7)
    t.root.left_child.right_sibling.left_child.right_sibling = Node(16, -1)
    t.root.left_child.right_sibling.right_sibling.left_child = Node(17, 6)
    print(t)
    guest_list(t.root)


if __name__ == "__main__":
    main()
