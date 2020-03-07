# https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
# def LIS(arr):  # only length
#     n = len(arr)
#     tails = [0] * n
#     size = 0
#     for i in range(n):
#         left = 0
#         right = size
#         while left < right:
#             mid = (left + right) // 2
#             if tails[mid] <= arr[i]:
#                 left = mid + 1
#             else:
#                 right = mid
#         tails[right] = arr[i]
#         size = max(right + 1, size)
#     return size


# https://en.wikipedia.org/wiki/Longest_increasing_subsequence#Efficient_algorithms
# def LIS(arr):
#     n = len(arr)
#     tails = [0] * n
#     path = [-1] * n
#     size = 0
#     for i in range(n):
#         left = 0
#         right = size
#         while left < right:
#             mid = (left + right) // 2
#             if arr[tails[mid]] <= arr[i]:
#                 left = mid + 1
#             else:
#                 right = mid
#         tails[right] = i
#         if right > 0:
#             path[i] = tails[right - 1]
#
#         size = max(right + 1, size)
#     print(tails)
#
#     solution = []
#     k = tails[size - 1]
#     while k != -1:
#         solution.append(arr[k])
#         k = path[k]
#     print(list(reversed(solution)))
#     return size


def LIS(arr):
    n = len(arr)
    tails = [0] * n
    size = 0
    path = []
    for i in range(n):
        path.append([0])
    for i in range(n):
        if arr[i] < tails[0]:
            tails[0] = arr[i]
            path[0][0] = arr[i]
        else:
            left = 1
            right = size
            while left < right:
                mid = (left + right) // 2
                if tails[mid] <= arr[i]:
                    left = mid + 1
                else:
                    right = mid
            tails[right] = arr[i]
            if right > 0:
                path[right] = path[right - 1][:]
                path[right].append(arr[i])
            else:
                path[0][0] = arr[i]
        size = max(right + 1, size)
        print(size)
        print(path)
    print(tails)
    return size


def main():
    arr = [5, 1, 2, 3, 3, 4, 2, 1, 2, 2, 3, 1]
    # arr = [8, 9, 1, 2, 3, 4]
    lis_legth = LIS(arr)
    print(lis_legth)


if __name__ == "__main__":
    main()
