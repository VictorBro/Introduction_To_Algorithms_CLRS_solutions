def insertion_sort(A, r):
    if r > 0:
        insertion_sort(A, r-1)
        key = A[r]
        i = r - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key


arr = [6, 4, 5, 3, 4]
insertion_sort(arr, len(arr)-1)
print(arr)