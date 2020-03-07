def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = A[p:q+1]
    R = A[q+1:r+1]
    k = p
    i = j = 0
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1


arr = [3, 9, 41, 52, 38, 41, 41, 58]
merge(arr, 0, 3, len(arr)-1)
print(arr)
