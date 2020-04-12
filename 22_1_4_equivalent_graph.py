class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class UndirectedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [None] * self.vertices

    def add_edge(self, u, v):
        new_node = Node(v)
        new_node.next = self.adj_list[u]
        self.adj_list[u] = new_node
        if u != v:
            new_node = Node(u)
            new_node.next = self.adj_list[v]
            self.adj_list[v] = new_node

    def transform(self):
        visited_nodes = [-1] * self.vertices

        for i in range(self.vertices):
            prev = None
            curr = self.adj_list[i]
            while curr is not None:
                if visited_nodes[curr.data] == i or i == curr.data:
                    if prev is not None:
                        prev.next = curr.next
                    else:
                        self.adj_list[i] = curr.next
                else:
                    visited_nodes[curr.data] = i
                    prev = curr

                curr = curr.next

    def print_graph(self):
        for u in range(self.vertices):
            v = self.adj_list[u]
            while v is not None:
                print("(", u, ",", v.data, ")")
                v = v.next


def main():  # O(E + V)
    adj = UndirectedGraph(7)
    adj.add_edge(0, 1)
    adj.add_edge(0, 2)
    adj.add_edge(1, 2)
    adj.add_edge(0, 1)
    adj.add_edge(1, 2)
    adj.add_edge(2, 2)
    adj.add_edge(1, 2)
    adj.print_graph()
    adj.transform()
    print()
    adj.print_graph()


if __name__ == "__main__":
    main()
