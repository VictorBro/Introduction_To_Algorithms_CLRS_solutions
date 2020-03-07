def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        left = 0
        right = i - 1
        mid = (left + right) // 2
        while left <= right:
            if A[mid] > key:
                right = mid - 1
            elif A[mid] < key:
                left = mid + 1
            else:
                break
            mid = (left + right) // 2

        j = i - 1
        while j > mid:
            A[j+1] = A[j]
            j -= 1
        A[mid + 1] = key


arr = [6, 4, 5, 3, 4]
insertion_sort(arr)
print(arr)
