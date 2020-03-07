def merge(A, start, mid, end):
    L = A[start:mid + 1]
    R = A[mid + 1:end + 1]
    L_size = len(L)
    R_size = len(R)
    i = j = 0
    k = start
    while i < L_size and j < R_size:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < L_size:
        A[k] = L[i]
        i += 1
        k += 1
    while j < R_size:
        A[k] = R[j]
        j += 1
        k += 1


def merge_sort(A, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(A, start, mid)
        merge_sort(A, mid + 1, end)
        merge(A, start, mid, end)


def weighted_median(A):
    n = len(A)
    merge_sort(A, 0, n - 1)
    print(A)
    s = 0
    for i in range(n):
        if s + A[i] < 0.5:
            s += A[i]
        else:
            break
    return A[i], i


def main():
    A = [0.1, 0.35, 0.05, 0.1, 0.15, 0.05, 0.2]
    print(weighted_median(A))


if __name__ == "__main__":
    main()
