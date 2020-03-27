from random import randint


def partition(L, start, end):
    pivot_idx = randint(start, end)
    L[pivot_idx], L[end] = L[end], L[pivot_idx]
    i = j = start
    for j in range(start, end):
        if L[j] <= L[end]:
            L[i], L[j] = L[j], L[i]
            i += 1
    L[i], L[end] = L[end], L[i]
    return i


def quick_sort(L, start, end):
    if start < end:
        pivot_idx = partition(L, start, end)
        quick_sort(L, start, pivot_idx - 1)
        quick_sort(L, pivot_idx + 1, end)


def break_string_helper(L, B, path, i, j, first_break, last_break):
    if B[i][j] != float("inf"):
        return B[i][j]
    if first_break > last_break:
        B[i][j] = 0

    break_cost = j - i + 1
    for k in range(first_break, last_break + 1):
        part_1 = break_string_helper(L, B, path, i, L[k] - 1, first_break, k - 1)
        part_2 = break_string_helper(L, B, path, L[k], j, k + 1, last_break)
        if B[i][j] > part_1 + part_2 + break_cost:
            B[i][j] = part_1 + part_2 + break_cost
            path[i][j] = L[k] - 1
    return B[i][j]


def print_break_sequence(path, i, j):
    if path[i][j] == -1:
        return
    print(path[i][j] + 1, end="->")
    print_break_sequence(path, i, path[i][j])
    print_break_sequence(path, path[i][j] + 1, j)


def break_string(s, L):
    n = len(s)
    n_l = len(L)
    B = []
    path = []
    for i in range(n):
        B.append([float("inf")] * n)
        path.append([-1] * n)
    quick_sort(L, 0, n_l - 1)
    break_string_helper(L, B, path, 0, n - 1, 0, n_l - 1)
    for row in B:
        print(row)
    print()
    for row in path:
        print(row)
    print(B[0][n - 1])
    print_break_sequence(path, 0, n - 1)
    print()


def main():
    s = "aaaaabbbbbcccccddddd"
    L = [10, 2, 8]
    break_string(s, L)


if __name__ == "__main__":
    main()
