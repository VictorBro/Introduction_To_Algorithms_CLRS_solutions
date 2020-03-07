def left(i):
    return (i * 2) + 1


def right(i):
    return (i * 2) + 2


def min_heapify(A, n, i):
    l = left(i)
    r = right(i)
    smallest = i
    if l < n and A[i] > A[l]:
        smallest = l
    if r < n and A[smallest] > A[r]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, n, smallest)


arr = [1, 8, 7, 9, 14, 4, 5, 10, 11, 16]
min_heapify(arr, len(arr), 2)
print(arr)
