from random import randint


def partition(arr, start, end):
    pivot_idx = randint(start, end)
    arr[pivot_idx], arr[end] = arr[end], arr[pivot_idx]
    idx = start
    for i in range(start, end):
        if arr[i] <= arr[end]:
            arr[idx], arr[i] = arr[i], arr[idx]
            idx += 1
    arr[idx], arr[end] = arr[end], arr[idx]
    return idx


def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)


def LCS(arr, sorted_arr):
    n = len(arr)
    c = []
    path = []
    for i in range(n + 1):
        c.append([0] * (n + 1))
        path.append(['*'] * (n + 1))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i - 1] == sorted_arr[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                path[i][j] = '\\'
            elif c[i][j - 1] >= c[i - 1][j]:
                c[i][j] = c[i][j - 1]
                path[i][j] = '-'
            else:
                c[i][j] = c[i - 1][j]
                path[i][j] = "|"
    return c, path


def print_LCS(arr, path, i, j):
    if i == 0 or j == 0:
        return
    if path[i][j] == '\\':
        print_LCS(arr, path, i - 1, j - 1)
        print(arr[i - 1], end=" ")
    elif path[i][j] == '|':
        print_LCS(arr, path, i - 1, j)
    else:
        print_LCS(arr, path, i, j - 1)


def main():
    arr = [5, 1, 2, 3, 3, 4, 2, 1, 2, 2, 3, 1]
    # arr = [8, 9, 1, 2, 3, 4]
    n = len(arr)
    sorted_arr = arr[:]
    quick_sort(sorted_arr, 0, n-1)
    print(arr)
    print(sorted_arr)
    c, path = LCS(arr, sorted_arr)
    for i in range(n + 1):
        for j in range(n + 1):
            print(c[i][j], end=" ")
        print()
    for i in range(n + 1):
        for j in range(n + 1):
            print(path[i][j], end=" ")
        print()
    print(c[n][n])
    print_LCS(arr, path, n, n)


if __name__ == "__main__":
    main()
