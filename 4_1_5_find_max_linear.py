def find_max_subarray(A):
    n = len(A)
    g_max = l_max = A[0]
    g_low = g_high = l_low = l_high = 0
    for i in range(1, n):
        l_high = i
        if l_max + A[i] > A[i]:
            l_max += A[i]
        else:
            l_max = A[i]
            l_low = i
        if l_max > g_max:
            g_max = l_max
            g_low = l_low
            g_high = l_high
    return g_low, g_high, g_max


# def find_max_subarray(A):
#     local_max = global_max = A[0]
#     for i in range(1, len(A)):
#         local_max = max(local_max + A[i], A[i])
#         if local_max > global_max:
#             global_max = local_max
#     return global_max


arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
# arr = [-10, -7, -3, -6, -16]
# arr = [0, 0, 0]
low_idx, high_idx, max_sum = find_max_subarray(arr)
print(arr[low_idx:high_idx + 1], max_sum)
