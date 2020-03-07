# https://github.com/bephrem1/backtobackswe/blob/master/Dynamic%20Programming%2C%20Recursion%2C%20%26%20Backtracking/LongestIncreasingSubsequence/LongestIncreasingSubsequence.java


def LIS_length(arr):
    n = len(arr)
    max_length = [1] * n
    path = [-1] * n
    max_overall = 0
    max_overall_idx = -1
    for i in range(n):
        for j in range(i):
            if arr[i] >= arr[j]:
                if max_length[j] + 1 > max_length[i]:
                    max_length[i] = max_length[j] + 1
                    path[i] = j
        if max_length[i] > max_overall:
            max_overall = max_length[i]
            max_overall_idx = i
    print(max_length)
    print(path)
    return max_overall, max_overall_idx, path


def print_solution(arr, path, idx):
    if idx != -1:
        print_solution(arr, path, path[idx])
        print(arr[idx], end=" ")


def main():
    arr = [5, 1, 2, 3, 3, 4, 2, 1, 2, 2, 3, 1]
    # arr = [8, 9, 1, 2, 3, 4]
    max_overall, max_overall_idx, path = LIS_length(arr)
    print(max_overall)
    print(max_overall_idx)
    print_solution(arr, path, max_overall_idx)
    print()


if __name__ == "__main__":
    main()
