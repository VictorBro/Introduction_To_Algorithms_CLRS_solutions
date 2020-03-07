def inversions_count(A, left, mid, right):
    L = A[left:mid+1]
    R = A[mid+1:right+1]
    i = j = 0
    k = left
    count = 0
    while i < len(L) and j < len(R):
        if L[i] > R[j]:
            count += len(L) - i
            A[k] = R[j]
            j += 1
        else:
            A[k] = L[i]
            i += 1
        k += 1
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1
    return count


def inversions_helper(A, low, high):
    count = 0
    if low < high:
        mid = (low + high) // 2
        count += inversions_helper(A, low, mid)
        count += inversions_helper(A, mid+1, high)
        count += inversions_count(A, low, mid, high)
    return count


def inversions(A):
    return inversions_helper(A, 0, len(A)-1)


arr = [2, 3, 8, 6, 1]
# arr = [5, 4, 3, 2, 1]
print(inversions(arr))
