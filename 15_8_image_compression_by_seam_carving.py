def seam_disruptions(d, m, n):
    seam_sum = []
    seam_path = []
    for i in range(m):
        seam_sum.append([float("inf")] * n)
        seam_path.append(['*'] * n)

    for j in range(n):
        seam_sum[0][j] = d[0][j]

    for i in range(1, m):
        for j in range(n):
            if j > 0:
                if seam_sum[i][j] > seam_sum[i - 1][j - 1] + d[i][j]:
                    seam_sum[i][j] = seam_sum[i - 1][j - 1] + d[i][j]
                    seam_path[i][j] = '\\'

            if seam_sum[i][j] > seam_sum[i - 1][j] + d[i][j]:
                seam_sum[i][j] = seam_sum[i - 1][j] + d[i][j]
                seam_path[i][j] = '|'

            if j < n - 1:
                if seam_sum[i][j] > seam_sum[i - 1][j + 1] + d[i][j]:
                    seam_sum[i][j] = seam_sum[i - 1][j + 1] + d[i][j]
                    seam_path[i][j] = '/'

    return seam_sum, seam_path


def print_seam_path(seam_path, i, j):
    if seam_path[i][j] == '*':
        print("[", i, j, "]", end="->")
    else:
        new_j = j
        if seam_path[i][j] == '\\':
            new_j = j - 1
        elif seam_path[i][j] == '/':
            new_j = j + 1
        print_seam_path(seam_path, i - 1, new_j)
        print("[", i, j, "]", end="->")


def print_min_seam_path(seam_sum, seam_path, m, n):
    min_sum = seam_sum[m - 1][0]
    min_idx = 0
    for j in range(1, n):
        if min_sum > seam_sum[m - 1][j]:
            min_sum = seam_sum[m - 1][j]
            min_idx = j
    print_seam_path(seam_path, m - 1, min_idx)
    print()


def main():
    d = [[1, 3, 1, 3, 2],
         [7, 1, 1, 2, 2],
         [2, 3, 4, 5, 3],
         [1, 1, 2, 3, 4],
         [5, 4, 3, 2, 1]]
    m = len(d)
    n = len(d[0])
    seam_sum, seam_path = seam_disruptions(d, m, n)
    for row in seam_sum:
        print(row)
    print()
    for row in seam_path:
        print(row)
    print_min_seam_path(seam_sum, seam_path, m, n)


if __name__ == "__main__":
    main()
