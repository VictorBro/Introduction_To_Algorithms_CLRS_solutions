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


arr = [5, 3, 17, 10, 84, 19, 6, 22, 9]
build_max_heap(arr, len(arr))
print(arr)
