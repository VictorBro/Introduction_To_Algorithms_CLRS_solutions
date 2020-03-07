class Node:
    def __init__(self, val, next=None):
        self.key = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def empty(self):
        return self.head is None

    def __str__(self):
        L = []
        x = self.head
        while x is not None:
            L.append(x.key)
            x = x.next
        return str(L)


def union(L1, L2):
    L = LinkedList()
    if not L1.empty():
        L.head = L1.head
        L.tail = L1.tail
    if not L2.empty():
        L.tail.next = L2.head
        L.tail = L2.tail
    return L


def main():
    L1 = LinkedList()
    L1.insert(1)
    L1.insert(3)
    L1.insert(5)
    print(L1)
    L2 = LinkedList()
    L2.insert(2)
    L2.insert(4)
    print(L2)
    L = union(L1, L2)
    print(L)


if __name__ == "__main__":
    main()
