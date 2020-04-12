class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def add_edge_to_list(u, v, adj):
    new_node = Node(v)
    new_node.next = adj[u]
    adj[u] = new_node


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [None] * self.vertices

        self.matrix = []
        for i in range(self.vertices):
            self.matrix.append([0] * self.vertices)

    def add_edge(self, u, v):
        new_node = Node(v)
        new_node.next = self.adj_list[u]
        self.adj_list[u] = new_node

        self.matrix[u][v] = 1

    def print_graph(self):
        for i in range(self.vertices):
            curr = self.adj_list[i]
            while curr is not None:
                print("(", i, ",", curr.data, ")")
                curr = curr.next

        for row in self.matrix:
            print(row)

    def remove_duplicates(self):
        seen_nodes = [-1] * self.vertices
        for u in range(self.vertices):
            prev = None
            curr = self.adj_list[u]
            while curr is not None:
                if seen_nodes[curr.data] == u:
                    if prev is not None:
                        prev.next = curr.next
                    else:
                        self.adj_list[u] = curr.next
                else:
                    seen_nodes[curr.data] = u
                    prev = curr
                curr = curr.next

    def square_graph(self): # list O(EV), matrix O(V^3)
        adj2_list = [None] * self.vertices
        for u in range(self.vertices):
            v = self.adj_list[u]
            while v is not None:
                add_edge_to_list(u, v.data, adj2_list)
                w = self.adj_list[v.data]
                while w is not None:
                    add_edge_to_list(u, w.data, adj2_list)
                    w = w.next
                v = v.next
        self.adj_list = adj2_list
        self.remove_duplicates()

        matrix2 = []
        for i in range(self.vertices):
            matrix2.append([0] * self.vertices)
        for u in range(self.vertices):
            for v in range(self.vertices):
                if self.matrix[u][v] == 1:
                    matrix2[u][v] = 1
                    for w in range(self.vertices):
                        if self.matrix[v][w] == 1:
                            matrix2[u][w] = 1
        self.matrix = matrix2


def main():
    adj = Graph(5)
    adj.add_edge(0, 1)
    adj.add_edge(1, 2)
    adj.add_edge(2, 4)
    adj.add_edge(1, 3)
    adj.add_edge(2, 1)
    adj.print_graph()
    print()
    adj.square_graph()
    adj.print_graph()


if __name__ == "__main__":
    main()
