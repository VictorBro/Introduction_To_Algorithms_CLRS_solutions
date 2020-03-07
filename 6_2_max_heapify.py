def parent(i):
    return (i - 1) // 2


def left(i):
    return (i * 2) + 1


def right(i):
    return (i * 2) + 2


def max_heapify(A, n, i):
    l = left(i)
    r = right(i)
    largest = i
    if l < n and A[i] < A[l]:
        largest = l
    if r < n and A[largest] < A[r]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)


arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
max_heapify(arr, len(arr), 1)
print(arr)
