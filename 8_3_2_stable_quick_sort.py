def partition(A, start, end):
    pivot = A[end]
    i = start - 1
    for j in range(start, end):
        if A[j][0] < pivot[0] or (A[j][0] == pivot[0] and A[j][1] < pivot[1]):
            i += 1
            A[i], A[j] = A[j], A[i]
    i += 1
    A[i], A[end] = A[end], A[i]
    return i


def stable_quick_sort(A, start, end):
    if start < end:
        pivot_idx = partition(A, start, end)
        stable_quick_sort(A, start, pivot_idx - 1)
        stable_quick_sort(A, pivot_idx + 1, end)


def quick_sort(A, start, end):
    n = len(A)
    new_arr = []
    for i in range(n):
        new_arr.append([A[i], i])
    stable_quick_sort(new_arr, start, end)
    # regular result would be [[0, 1], [0, 3], [1, 4], [1, 8], [2, 2], [2, 10], [3, 9], [3, 5], [4, 6], [6, 0], [6, 7]]
    print(new_arr)


def main():
    A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
    quick_sort(A, 0, len(A) - 1)


if __name__ == "__main__":
    main()
