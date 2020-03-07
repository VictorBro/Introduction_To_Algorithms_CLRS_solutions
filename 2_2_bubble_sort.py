def bubble_sort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]


arr = [5,3,2,1,3]
bubble_sort(arr)
print(arr)
