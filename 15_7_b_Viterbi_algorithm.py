# https://webdocs.cs.ualberta.ca/~mreza/courses/CSC364/tut-notes/tut3.pdf


def print_path(path_seq, i, j):
    if i == 0:
        print(j, end="->")
    else:
        print_path(path_seq, i - 1, path_seq[i][j])
        print(j, end="->")


def veterbi_helper(graph, prob, v0, s, path, path_seq, v_n, i, v):
    if i == 0:
        if v == v0:
            path[i][v] = 1
        else:
            path[i][v] = 0
        return path[i][v]

    if path[i][v] != -1:
        return path[i][v]

    path[i][v] = 0
    for u in range(v_n):
        path_prob = veterbi_helper(graph, prob, v0, s, path, path_seq, v_n, i - 1, u)
        if path_prob > 0 and graph[u][v] == s[i - 1]:
            if path_prob * prob[u][v] > path[i][v]:
                path[i][v] = path_prob * prob[u][v]
                path_seq[i][v] = u

    return path[i][v]


def viterbi(graph, prob, v0, s):  # O(s_n * (v_n ^ 2))
    v_n = len(graph)
    s_n = len(s)
    path = []
    path_seq = []
    for i in range(s_n + 1):
        path.append([-1] * v_n)
        path_seq.append([-1] * v_n)

    max_prob = 0
    max_v = -1
    for v in range(v_n):
        temp_prob = veterbi_helper(graph, prob, v0, s, path, path_seq, v_n, s_n, v)
        if temp_prob > max_prob:
            max_v = v
            max_prob = temp_prob

    for row in path:
        print(row)
    print()
    for row in path_seq:
        print(row)

    if max_prob == 0:
        print("NO—SUCH—PATH")
    else:
        print(max_prob)
        print_path(path_seq, s_n, max_v)
        print()


def main():  # path[i, v] = (path[i-1, u] and graph[u, v] == s[i]) or i == 0
    graph = [['*', 'a', '*', 'b', 'a', '*'],
             ['*', '*', 'b', '*', '*', 'd'],
             ['*', '*', '*', '*', '*', '*'],
             ['*', 'c', '*', '*', '*', '*'],
             ['*', '*', '*', 'b', '*', '*'],
             ['a', '*', '*', '*', '*', '*']]
    prob = [[0.0, 0.3, 0.0, 0.5, 0.2, 0.0],
            [0.0, 0.0, 0.5, 0.0, 0.0, 0.5],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
            [1.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

    viterbi(graph, prob, 0, "ab")


if __name__ == "__main__":
    main()
