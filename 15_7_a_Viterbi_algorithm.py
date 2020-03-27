# https://webdocs.cs.ualberta.ca/~mreza/courses/CSC364/tut-notes/tut3.pdf


def print_path(path_seq, i, j):
    if i == 0:
        print(j, end="->")
    else:
        print_path(path_seq, i - 1, path_seq[i][j])
        print(j, end="->")


def veterbi_helper(graph, v0, s, path, path_seq, v_n, i, v):
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
        path_exists = veterbi_helper(graph, v0, s, path, path_seq, v_n, i - 1, u)
        if path_exists and graph[u][v] == s[i - 1]:
            path[i][v] = path_exists
            path_seq[i][v] = u
            break

    return path[i][v]


def viterbi(graph, v0, s):  # O(s_n * (v_n ^ 2))
    v_n = len(graph)
    s_n = len(s)
    path = []
    path_seq = []
    for i in range(s_n + 1):
        path.append([-1] * v_n)
        path_seq.append([-1] * v_n)

    path_exists = 0
    for v in range(v_n):
        path_exists = veterbi_helper(graph, v0, s, path, path_seq, v_n, s_n, v)
        if path_exists:
            print_path(path_seq, s_n, v)
            print()
            break
    if not path_exists:
        print("NO—SUCH—PATH")


def main():  # path[i, v] = (path[i-1, u] and graph[u, v] == s[i]) or i == 0
    graph = [['*', 'a', '*', 'b', 'a', '*'],
             ['*', '*', 'b', '*', '*', 'd'],
             ['*', '*', '*', '*', '*', '*'],
             ['*', 'c', '*', '*', '*', '*'],
             ['*', '*', '*', 'b', '*', '*'],
             ['a', '*', '*', '*', '*', '*']]

    viterbi(graph, 0, "abc")


if __name__ == "__main__":
    main()
