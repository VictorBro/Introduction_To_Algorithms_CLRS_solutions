def insertion_sort(A):
    n = len(A)

    if n < 2:
        return

    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key


arr = [6, 4, 5, 3]
insertion_sort(arr)
print(arr)
