class Node:
    def __init__(self, val, next=None):
        self.key = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def __str__(self):
        L = []
        x = self.head
        while x is not None:
            L.append(x.key)
            x = x.next
        return str(L)


def main():
    L = LinkedList()
    L.insert(1)
    L.insert(2)
    L.insert(3)
    L.insert(4)
    L.insert(5)
    print(L)
    L.reverse()
    print(L)


if __name__ == "__main__":
    main()
