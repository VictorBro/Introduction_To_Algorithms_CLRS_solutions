def extract_min(matrix, M, N, i, j):
    min_val = float("inf")
    if i == 0 and j == 0:
        min_val, matrix[0][0] = matrix[0][0], min_val
    smallest_i = i
    smallest_j = j
    if j + 1 < N and matrix[smallest_i][smallest_j] > matrix[i][j + 1]:
        smallest_j = j + 1
    if i + 1 < M and matrix[smallest_i][smallest_j] > matrix[i + 1][j]:
        smallest_i = i + 1
        smallest_j = j
    if smallest_i != i or smallest_j != j:
        matrix[i][j], matrix[smallest_i][smallest_j] = matrix[smallest_i][smallest_j], matrix[i][j]
        extract_min(matrix, M, N, smallest_i, smallest_j)
    return min_val


def insert(matrix, M, N, key):
    matrix[M - 1][N - 1] = key
    largest_i = i = M - 1
    largest_j = j = N - 1
    while True:
        if i - 1 >= 0 and matrix[largest_i][largest_j] < matrix[i - 1][j]:
            largest_i = i - 1
        if j - 1 >= 0 and matrix[largest_i][largest_j] < matrix[i][j - 1]:
            largest_i = i
            largest_j = j - 1
        if largest_i == i and largest_j == j:
            break
        matrix[i][j], matrix[largest_i][largest_j] = matrix[largest_i][largest_j], matrix[i][j]
        i = largest_i
        j = largest_j


def tableau_sort(matrix, N):
    sorted_list = []
    inf = float("inf")

    for i in range(N):  # O(n^3)
        for j in range(N):  # O(n^3)
            insert(matrix, i + 1, j + 1, matrix[i][j])  # O(n+n) = O(n)

    for row in matrix:
        print(row)

    min_val = extract_min(matrix, N, N, 0, 0)
    while min_val != inf:  # O(n^3)
        sorted_list.append(min_val)
        min_val = extract_min(matrix, N, N, 0, 0)  # O(n)

    return sorted_list


def find(matrix, M, N, x):
    i = M - 1
    j = 0
    while i >= 0 and j < N:
        if matrix[i][j] > x:
            i -= 1
        elif matrix[i][j] < x:
            j += 1
        else:
            print(i, j)
            return True
    return False


def main():
    inf = float("inf")
    matrix = [[2, 3, 12, 14],
              [4, 8, 16, inf],
              [5, 9, inf, inf],
              [inf, inf, inf, inf]]
    print(extract_min(matrix, len(matrix), len(matrix[0]), 0, 0))
    for row in matrix:
        print(row)

    insert(matrix, len(matrix), len(matrix[0]), 7)
    for row in matrix:
        print(row)

    matrix = [[9, 16, 3, 2],
              [4, 8, 5, 14],
              [12, 9, 6, 1],
              [2, 7, 11, 2]]
    sorted_list = tableau_sort(matrix, len(matrix))
    print(sorted_list)

    # matrix = [[2, 3, 12, 14],
    #           [4, 8, 16, inf],
    #           [5, 9, inf, inf],
    #           [inf, inf, inf, inf]]
    matrix = [[1, 2, 3, 5],
              [2, 2, 7, 9],
              [4, 8, 11, 14],
              [6, 9, 12, 16]]
    print(find(matrix, len(matrix), len(matrix[0]), 14))


if __name__ == "__main__":
    main()
