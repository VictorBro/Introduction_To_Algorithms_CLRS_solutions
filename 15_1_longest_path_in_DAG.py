# http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/11-Graph/Docs/longest-path-in-dag.pdf


def longest_path_helper(graph, n, s, t, path_lengths, parents):
    print("longest_path_helper", s, t)
    if s == t:
        print("0:", s, t, path_lengths)
        return 0
    if path_lengths[t] > 0:
        print("1:", s, t, path_lengths)
        return path_lengths[t]
    for u in range(n):
        if graph[u][t] != 0:
            temp = graph[u][t] + longest_path_helper(graph, n, s, u, path_lengths, parents)
            if temp > path_lengths[t]:
                path_lengths[t] = temp
                parents[t] = u
                print("2:", s, t, path_lengths)
    print("3:", s, t, path_lengths)
    return path_lengths[t]


def print_solution(parents, s, t):
    if s == t:
        print(s, end=" ")
        return
    print_solution(parents, s, parents[t])
    print(t, end=" ")


def longest_path(graph, s, t):  # dist[v] = max{w(u,v) + dist[u]}
    n = len(graph)
    path_lengths = [0] * n
    parents = [-1] * n
    longest_path_helper(graph, n, s, t, path_lengths, parents)
    print()
    print(path_lengths)
    print(parents)
    print_solution(parents, s, t)
    print()


def main():
    graph = [[0, 1, 0, 2, 0, 3],
             [0, 0, 6, 0, 0, 0],
             [0, 0, 0, 0, 1, 2],
             [0, 4, 0, 0, 3, 0],
             [0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0]]

    # graph = {'S': [['A', 1], ['C', 2]],
    #          'A': [['B', 6]],
    #          'B': [['T', 2], ['D', 1]],
    #          'C': [['D', 3], ['A', 4]],
    #          'D': [['T', 1]]}

    # longest_path(graph, 'S', 'T')
    longest_path(graph, 0, 5)


if __name__ == "__main__":
    main()
