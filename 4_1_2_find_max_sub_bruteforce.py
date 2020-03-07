def find_max_subarray(A):
    n = len(A)
    max_sum = A[0]
    low = high = 0
    for i in range(0, n):
        sum = 0
        for j in range(i, n):
            sum += A[j]
            if sum > max_sum:
                max_sum = sum
                low = i
                high = j
    return low, high, max_sum


arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
low_idx, high_idx, max_found_sum = find_max_subarray(arr)
print(arr[low_idx:high_idx + 1], max_found_sum)
