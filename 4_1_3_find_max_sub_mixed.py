import time
import timeit


def find_max_sub_brute(A, low, high):
    local_max_sum = A[low]
    local_low = local_high = low
    for i in range(low, high + 1):
        temp_sum = 0
        for j in range(i, high + 1):
            temp_sum += A[j]
            if temp_sum > local_max_sum:
                local_max_sum = temp_sum
                local_low = i
                local_high = j
    return local_low, local_high, local_max_sum


def find_max_cross_sub(A, low, mid, high):
    left_sum = temp_sum = A[mid]
    left_low = mid
    for i in range(mid - 1, low - 1, -1):
        temp_sum += A[i]
        if temp_sum > left_sum:
            left_sum = temp_sum
            left_low = i

    right_sum = temp_sum = A[mid + 1]
    right_high = mid + 1
    for j in range(mid + 2, high + 1):
        temp_sum += A[j]
        if temp_sum > right_sum:
            right_sum = temp_sum
            right_high = j

    return left_low, right_high, left_sum + right_sum


def find_max_sub(A, low, high):
    if low == high:
        return low, high, A[low]

    mid = (low + high) // 2
    left_low, left_high, left_sum = find_max_sub(A, low, mid)
    right_low, right_high, right_sum = find_max_sub(A, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_cross_sub(A, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


arr = [20, -21, 43, -23, -92, 45, -56, -5, 34, -17,
       34, 65, 89, -109, 125, 2, -10, 89, 46, 65, -49,
       3, -45, 34, 76, 32, -76, -2, 3, -45, 44, 34, 67,
       -67, 99, -104, 11, -37, 44, 76, -90, 89, -32, 34,
       88, 56, -6, -89, -90, -34, -56, 23, 29, 2, 6, 9,
       2, -34, -45, 34, 22, -177, 44, 90, -45, -36, 55,
       23, 56, -56, -167, -54, 23, 45, 14, 62, -46, -56,
       -34, 45, 32, 20, -87, 39, 82, 95, -67, -45, 88,
       -36, 21, 18, 16, 81, -102, 99, -45, -67, -45, -76]
# arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
low_idx, high_idx, max_sum = find_max_sub_brute(arr, 0, len(arr) - 1)
print(arr[low_idx:high_idx + 1], max_sum)

low_idx, high_idx, max_sum = find_max_sub(arr, 0, len(arr) - 1)
print(arr[low_idx:high_idx + 1], max_sum)

time_brute = time_recursive = 0
i = 0

while time_brute <= time_recursive and i < len(arr):
    start = time.time()
    low_idx, high_idx, max_sum = find_max_sub_brute(arr, 0, i)
    end = time.time()
    time_brute = end - start
    print("time_brute:", time_brute)

    start = time.time()
    low_idx, high_idx, max_sum = find_max_sub(arr, 0, i)
    end = time.time()
    time_recursive = end - start
    print("time_recursive:", time_recursive)
    i += 1

print(i)
