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


arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
max_heapify(arr, len(arr), 1)
print(arr)
