from random import randint


def partition(A, start, end):
    pivot_idx = randint(start, end)
    A[end], A[pivot_idx] = A[pivot_idx], A[end]
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
    while start < end:
        pivot_idx = partition(A, start, end)
        quick_sort(A, start, pivot_idx - 1)
        start = pivot_idx + 1


def stack_depth_quick_sort(A, start, end):
    while start < end:
        pivot_idx = partition(A, start, end)
        if pivot_idx <= (start + end) // 2:
            quick_sort(A, start, pivot_idx - 1)
            start = pivot_idx + 1
        else:
            quick_sort(A, pivot_idx + 1, end)
            end = pivot_idx - 1


def main():
    A = [5, 6, 3, 4, 8]
    quick_sort(A, 0, len(A) - 1)
    print(A)

    A = [5, 6, 3, 4, 8]
    stack_depth_quick_sort(A, 0, len(A) - 1)
    print(A)


if __name__ == "__main__":
    main()
