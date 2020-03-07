from random import randint


def partition(A, start, end):
    pivot_idx = randint(start, end)
    A[pivot_idx], A[end] = A[end], A[pivot_idx]
    pivot = A[end]
    q = start
    for j in range(start, end):
        if A[j] < pivot:
            A[q], A[j] = A[j], A[q]
            q += 1
    t = q - 1
    for j in range(q, end + 1):
        if A[j] == pivot:
            t += 1
            A[t], A[j] = A[j], A[t]
    return q, t


def quick_sort(A, start, end):
    if start < end:
        q, t = partition(A, start, end)
        quick_sort(A, start, q - 1)
        quick_sort(A, t + 1, end)


def main():
    A = [7, 0, 7, 2, 0, 7, 7, 2, 2, 0]
    # A = [3, 2, 4, 5]
    q, t = partition(A, 0, len(A) - 1)
    print(A)
    print(q, t)

    A = [7, 0, 7, 2, 0, 7, 7, 2, 2, 0]
    quick_sort(A, 0, len(A) - 1)
    print(A)


if __name__ == "__main__":
    main()
