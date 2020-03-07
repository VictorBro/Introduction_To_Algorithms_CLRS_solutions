def binary_search_leftmost(A, target):
    n = len(A)
    left = 0
    right = n - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] >= target:
            right = mid
        else:
            left = mid + 1
    if A[right] == target:
        return right
    else:
        return -1


def binary_search_rightmost(A, target):
    n = len(A)
    left = 0
    right = n - 1
    while left < right:
        mid = -(-(left + right) // 2)
        if A[mid] <= target:
            left = mid
        else:
            right = mid - 1
    if A[left] == target:
        return left
    else:
        return -1


arr = [1,2,4,4,4,5,6]
print(binary_search_leftmost(arr, 4))
print(binary_search_rightmost(arr, 4))
