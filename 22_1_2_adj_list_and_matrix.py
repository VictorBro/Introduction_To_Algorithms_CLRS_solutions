class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class UndirectedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.list_graph = [None] * self.vertices
        self.matrix = []
        for i in range(self.vertices):
            self.matrix.append([0] * self.vertices)

    def add_edge(self, u, v):
        new_node = Node(v)
        new_node.next = self.list_graph[u - 1]
        self.list_graph[u - 1] = new_node

        new_node = Node(u)
        new_node.next = self.list_graph[v - 1]
        self.list_graph[v - 1] = new_node

        self.matrix[u - 1][v - 1] = 1
        self.matrix[v - 1][u - 1] = 1

    def print_graph(self):
        for i in range(self.vertices):
            curr_node = self.list_graph[i]
            while curr_node is not None:
                print("(", i + 1, ",", curr_node.data, ")")
                curr_node = curr_node.next
        for row in self.matrix:
            print(row)


def main():
    adj = UndirectedGraph(7)
    adj.add_edge(1, 2)
    adj.add_edge(1, 3)
    adj.add_edge(2, 4)
    adj.add_edge(2, 5)
    adj.add_edge(3, 6)
    adj.add_edge(3, 7)
    adj.print_graph()


if __name__ == "__main__":
    main()
