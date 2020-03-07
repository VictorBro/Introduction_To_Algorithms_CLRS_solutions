def find_max_cross_sub(A, low, mid, high):
    left_sum = sum = A[mid]
    left = mid
    for i in range(mid-1, low-1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            left = i
    right_sum = sum = A[mid+1]
    right = mid + 1
    for i in range(mid+2, high+1):
        sum += A[i]
        if sum > right_sum:
            right_sum = sum
            right = i
    return left, right, left_sum + right_sum


def find_max_sub(A, low, high):
    if low == high:
        if A[low] > 0:
            return low, high, A[low]
        else:
            return -1, -1, 0
    mid = (low + high) // 2
    l_low, l_high, l_max = find_max_sub(A, low, mid)
    r_low, r_high, r_max = find_max_sub(A, mid+1, high)
    c_low, c_high, c_max = find_max_cross_sub(A, low, mid, high)
    if l_max >= r_max and l_max >= c_max:
        return l_low, l_high, l_max
    elif r_max >= l_max and r_max >= c_max:
        return r_low, r_high, r_max
    else:
        return c_low, c_high, c_max


arr = [-25, -7, -10, -7, -10]
# arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
low_idx, high_idx, max_sum = find_max_sub(arr, 0, len(arr) - 1)
print(arr[low_idx:high_idx + 1], max_sum)
