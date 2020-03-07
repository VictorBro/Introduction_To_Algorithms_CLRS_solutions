def partition(A, start, end):
    pivot = A[end]
    i = start - 1
    for j in range(start, end):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    i += 1
    A[i], A[end] = A[end], A[i]
    return i


def quick_sort(A, start, end):
    if start < end:
        pivot_idx = partition(A, start, end)
        quick_sort(A, start, pivot_idx - 1)
        quick_sort(A, pivot_idx + 1, end)


def main():
    A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    quick_sort(A, 0, len(A) - 1)
    print(A)


if __name__ == "__main__":
    main()
