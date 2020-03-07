class Node:
    def __init__(self, val, next=None):
        self.key = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        x = self.head
        prev = None
        while x is not None and x.key != key:
            prev = x
            x = x.next
        if x is not None:
            if prev is not None:
                prev.next = x.next
            else:
                self.head = x.next

    def __str__(self):
        L = []
        x = self.head
        while x is not None:
            L.append(x.key)
            x = x.next
        return str(L)


def main():
    L = LinkedList(Node(14))
    L.insert(Node(5))
    L.insert(Node(7))
    L.insert(Node(3))
    L.delete(5)
    L.delete(9)
    print(L)


if __name__ == "__main__":
    main()
