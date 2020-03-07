def merge(A, left, mid, right):
    L = A[left:mid+1]
    R = A[mid+1:right+1]
    i = j = 0
    k = left
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1


def merge_sort(A, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(A, low, mid)
        merge_sort(A, mid + 1, high)
        merge(A, low, mid, high)


arr = [6, 4, 5, 3, 4]
merge_sort(arr, 0, len(arr) - 1)
print(arr)


def check_sum_existence(A, x):
    merge_sort(A, 0, len(A)-1)  #O(nlogn)
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] + A[j] == x:
            return True
        elif A[i] + A[j] < x:
            i += 1
        else:
            j -= 1
    return False


arr = [6, 4, 5, 3, 4]
print(check_sum_existence(arr, 7))
