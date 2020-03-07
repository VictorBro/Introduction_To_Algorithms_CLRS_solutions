from random import randint


def partition(A, start, end):
    pivot_idx = randint(start, end)
    pivot = A[pivot_idx]
    A[pivot_idx], A[end] = A[end], A[pivot_idx]

    i = start
    for j in range(start, end):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[end] = A[end], A[i]
    return i


def select(A, start, end, k):
    if k < start or k > end:
        raise Exception("Illegal index")
    if start == end:
        return start
    pivot_idx = partition(A, start, end)
    if pivot_idx == k:
        return pivot_idx
    elif pivot_idx > k:
        return select(A, start, pivot_idx - 1, k)
    else:
        return select(A, pivot_idx + 1, end, k)


def k_closest(A, k):
    n = len(A)
    mid = (n - 1) // 2
    mid_idx = select(A, 0, n - 1, mid)
    low = mid_idx - ((k - 1) // 2)
    low_idx = select(A, 0, mid_idx, low)
    high = -(-(k - 1) // 2) + mid_idx
    high_idx = select(A, mid_idx, n - 1, high)
    print(A[low_idx:high_idx + 1])


def main():
    A = [8, 4, 1, 2, 3]
    k_closest(A, 3)
    k_closest(A, 4)
    k_closest(A, 1)
    k_closest(A, 2)


if __name__ == "__main__":
    main()
