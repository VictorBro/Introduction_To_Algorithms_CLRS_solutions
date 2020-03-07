class Node:
    def __init__(self, val=None, next=None):
        self.key = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        if self.head is not None:
            self.head.next = self.head

    def insert(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            new_node.next = self.head.next
            self.head.next = new_node

    def delete(self, del_node):
        if self.head is None:
            raise Exception("Underflow")
        del_node_prev = del_node.next
        while del_node_prev.next != del_node:
            del_node_prev = del_node_prev.next

        if del_node_prev == del_node:
            self.head = None
            return
        if del_node == self.head:
            self.head = del_node_prev
        del_node_prev.next = del_node.next
        del_node.next = None

    def search(self, val):
        x = self.head
        if self.head is None or x.key == val:
            return x
        x = x.next
        while x != self.head and x.key != val:
            x = x.next
        if x.key != val:
            x = None
        return x

    def __str__(self):
        L = []
        if self.head is not None:
            x = self.head
            L.append(x.key)
            x = x.next
            while x != self.head:
                L.append(x.key)
                x = x.next
        return str(L)


def main():
    L = LinkedList()
    L.insert(1)
    x = L.search(1)
    L.delete(x)
    print(L)
    L.insert(2)
    L.insert(3)
    L.insert(4)
    L.insert(5)
    print(L)
    x = L.search(3)
    L.delete(x)
    print(L)
    x = L.search(6)
    print(x)


if __name__ == "__main__":
    main()

