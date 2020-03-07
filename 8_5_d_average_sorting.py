def merge(A, start, mid, end, k):
    L = A[start:mid+1:k]
    n_l = len(L)
    R = A[mid+k:end+1:k]
    n_r = len(R)
    i = j = 0
    p = start
    while i < n_l and j < n_r:
        if L[i] <= R[j]:
            A[p] = L[i]
            i += 1
        else:
            A[p] = R[j]
            j += 1
        p += k
    while i < n_l:
        A[p] = L[i]
        i += 1
        p += k
    while j < n_r:
        A[p] = R[j]
        j += 1
        p += k


def merge_sort(A, start, end, k):
    if start < end:
        mid = (end - start) // 2
        mid = (mid // k) * k + start
        merge_sort(A, start, mid, k)
        merge_sort(A, mid + k, end, k)
        merge(A, start, mid, end, k)


def k_sort(A, k):
    n = len(A)
    for i in range(k):
        if i < n:
            start = i
            end = start + ((n-1)//k)*k
            if end >= n:
                end -= k
            merge_sort(A, start, end, k)


def main():
    A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    k_sort(A, 3)
    print(A)


if __name__ == "__main__":
    main()
