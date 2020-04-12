class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * self.vertices

    def add_edge(self, u, v):
        new_node = Node(v)
        new_node.next = self.graph[u]
        self.graph[u] = new_node

    def print_graph(self):
        for i in range(self.vertices):
            curr_node = self.graph[i]
            while curr_node is not None:
                print("(", i, ",", curr_node.data, ")")
                curr_node = curr_node.next

    def out_degrees(self):
        for i in range(self.vertices):
            cnt = 0
            curr_node = self.graph[i]
            while curr_node is not None:
                cnt += 1
                curr_node = curr_node.next
            print("out degree for", i, "is", cnt)

    def in_degrees(self):
        in_counts = [0] * self.vertices
        for i in range(self.vertices):
            curr_node = self.graph[i]
            while curr_node is not None:
                in_counts[curr_node.data] += 1
                curr_node = curr_node.next
        for i in range(self.vertices):
            print("in degree for", i, "is", in_counts[i])


def main():
    v = 6
    adj = Graph(v)
    adj.add_edge(0, 1)
    adj.add_edge(0, 3)
    adj.add_edge(3, 1)
    adj.add_edge(1, 4)
    adj.add_edge(4, 3)
    adj.add_edge(2, 4)
    adj.add_edge(2, 5)
    adj.add_edge(5, 5)
    adj.print_graph()
    adj.in_degrees()
    adj.out_degrees()


if __name__ == "__main__":
    main()
