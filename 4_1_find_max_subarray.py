def find_max_cross_subarray(A, low, mid, high):
    left_sum = sum = A[mid]
    left = mid
    for i in range(mid - 1, low - 1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            left = i

    right_sum = sum = A[mid + 1]
    right = mid + 1
    for j in range(mid + 2, high + 1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            right = j
    return left, right, left_sum + right_sum


def find_max_subarray(A, low, high):
    if low == high:
        return low, high, A[low]

    mid = (low + high) // 2

    left_low, left_high, left_sum = find_max_subarray(A, low, mid)
    right_low, right_high, right_sum = find_max_subarray(A, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_cross_subarray(A, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


# arr = [25, -7, 10, -7, 10]
# arr = [18, 20, -7, 12]
# arr = [-25, -7, -10, -7, -10]
arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
low_idx, high_idx, max_sum = find_max_subarray(arr, 0, len(arr) - 1)
print(arr[low_idx:high_idx + 1], max_sum)
