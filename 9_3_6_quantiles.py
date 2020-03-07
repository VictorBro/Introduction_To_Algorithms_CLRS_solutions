from random import randint


def partition(A, start, end):  # O(n)
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


def selection(A, start, end, k):  # O(n)
    print("selection(", start, end, k, ")")
    if k < start or k > end:
        raise Exception("Illegal index")
    if start == end:
        return start
    pivot_idx = partition(A, start, end)
    print("pivot_idx", pivot_idx, "pivot", A[pivot_idx])
    print(A[start:end + 1])
    if pivot_idx == k:
        return pivot_idx
    elif pivot_idx > k:
        return selection(A, start, pivot_idx - 1, k)
    else:
        return selection(A, pivot_idx + 1, end, k)


def quantiles(A, n, start, end, i, j, k, Q):
    print("quantile(", start, end, i, j, ")")
    if k == 1:
        for x in A:
            Q.append(x)
        return
    if i > j:
        return
    mid = (i + j) // 2
    idx = mid * (n // k) - 1
    print("quantile_idx ", idx)
    pivot_idx = selection(A, start, end, idx)  # O(n)
    Q.append(A[pivot_idx])
    quantiles(A, n, start, pivot_idx - 1, i, mid - 1, k, Q)
    quantiles(A, n, pivot_idx + 1, end, mid + 1, j, k, Q)


def main():
    A = [35, 5, 11, 24, 37, 8, 10, 12, 51, 23, 14, 43]
    Q = []
    n = len(A)
    k = 1
    quantiles(A, n, 0, n - 1, 1, k - 1, k, Q)
    print(Q)

    B = [35, 5]
    n = len(B)
    k = 2
    Q = []
    print()
    quantiles(B, n, 0, n - 1, 1, k - 1, k, Q)
    print(Q)


if __name__ == "__main__":
    main()


