class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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

    def transpose(self):
        for i in range(self.vertices - 1):
            for j in range(i + 1, self.vertices):
                self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]

        new_adj_list = [None] * self.vertices
        for u in range(self.vertices):
            v = self.adj_list[u]
            while v is not None:
                new_node = Node(u)
                new_node.next = new_adj_list[v.data]
                new_adj_list[v.data] = new_node
                v = v.next

        self.adj_list = new_adj_list

    def print_graph(self):
        for row in self.matrix:
            print(row)
        for u in range(self.vertices):
            v = self.adj_list[u]
            while v is not None:
                print("(", u, ",", v.data, ")")
                v = v.next


def main():
    adj = Graph(7)
    adj.add_edge(0, 1)
    adj.add_edge(0, 2)
    adj.add_edge(1, 3)
    adj.add_edge(1, 4)
    adj.add_edge(2, 5)
    adj.add_edge(2, 6)
    adj.print_graph()
    adj.transpose()
    adj.print_graph()


if __name__ == "__main__":
    main()
