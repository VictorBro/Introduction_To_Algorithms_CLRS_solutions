class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.key = val
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.nil = Node()
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def insert(self, val):
        new_node = Node(val)
        new_node.next = self.nil.next
        new_node.next.prev = new_node
        self.nil.next = new_node
        new_node.prev = self.nil

    def search(self, val):
        x = self.nil.next
        self.nil.key = val
        while x.key != val:
            x = x.next
        self.nil.key = None
        return x

    def __str__(self):
        L = []
        x = self.nil.next
        while x != self.nil:
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
    x = L.search(6)
    print(x.key)


if __name__ == "__main__":
    main()




