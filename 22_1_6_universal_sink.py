class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matrix = []
        for i in range(self.vertices):
            self.matrix.append([0] * self.vertices)

    def add_edge(self, u, v):
        self.matrix[u][v] = 1

    def print_graph(self):
        for row in self.matrix:
            print(row)

    def is_has_universal_sink(self):
        i = j = 0
        while i < self.vertices and j < self.vertices:
            if self.matrix[i][j] == 1:
                i += 1
            else:
                j += 1
        for k in range(self.vertices):
            if self.matrix[i][k] != 0:
                return False
            if k != i and self.matrix[k][i] != 1:
                return False
        print("universal sink is", i)
        return True


def main():  # O(V)
    adj = Graph(4)
    adj.add_edge(0, 1)
    adj.add_edge(1, 3)
    adj.add_edge(0, 3)
    adj.add_edge(2, 1)
    adj.add_edge(2, 3)
    adj.print_graph()
    print(adj.is_has_universal_sink())


if __name__ == "__main__":
    main()
