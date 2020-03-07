def left(i):
    return (2 * i) + 1


def right(i):
    return (2 * i) + 2


def max_heapify(A, n, i):
    while True:
        l = left(i)
        r = right(i)
        largest = i
        if l < n and A[i] < A[l]:
            largest = l
        if r < n and A[largest] < A[r]:
            largest = r
        if largest == i:
            break
        A[largest], A[i] = A[i], A[largest]
        i = largest


def build_max_heap(A, n):
    start = (n // 2) - 1
    for i in range(start, -1, -1):
        max_heapify(A, n, i)


def heapsort(A, n):
    build_max_heap(A, n)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A, i, 0)


arr = [5, 13, 2, 25, 7, 17, 20, 8, 4]
heapsort(arr, len(arr))
print(arr)
