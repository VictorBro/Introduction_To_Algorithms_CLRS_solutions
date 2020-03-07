def insertion_sort(A, start, end):
    for i in range(start + 1, end + 1):
        j = i
        while j > start and A[j - 1][0] > A[j][0]:
            A[j - 1], A[j] = A[j], A[j - 1]
            j -= 1


def partition(A, start, end, index):
    A[index], A[end] = A[end], A[index]
    pivot = A[end]
    i = start
    for j in range(start, end):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[end] = A[end], A[i]
    return i


def selection_median_of_medians(A, start, end):
    if start + 5 > end:
        insertion_sort(A, start, end)
        median_idx = (start + end) // 2
        return A[median_idx][1]

    medians = []
    for i in range(start, end + 1, 5):
        inner_end = i + 5 - 1
        if inner_end > end:
            inner_end = end
        insertion_sort(A, i, inner_end)
        median_idx = (i + inner_end) // 2
        medians.append(A[median_idx])
    return selection_median_of_medians(medians, 0, len(medians) - 1)


def linear_selection(A, start, end, k):
    if k < start + 1 or k > end + 1:
        raise Exception("Illegal search index")
    elif start == end:
        return A[start]

    temp_array = []
    for i in range(start, end + 1):
        temp_array.append([A[i], i])
    median_of_medians_idx = selection_median_of_medians(temp_array, 0, len(temp_array) - 1)
    pivot_idx = partition(A, start, end, median_of_medians_idx)
    if pivot_idx + 1 == k:
        return A[pivot_idx]
    elif k < pivot_idx + 1:
        return linear_selection(A, start, pivot_idx - 1, k)
    else:
        return linear_selection(A, pivot_idx + 1, end, k)


def main():
    A = [1, 2, 3, 4, 5, 1000, 8, 9, 99]
    B = [1, 2, 3, 4, 5, 6]
    print(linear_selection(A, 0, len(A) - 1, 1))  # should be 1
    print(linear_selection(A, 0, len(A) - 1, 8))  # should be 99
    print(linear_selection(B, 0, len(B) - 1, 5))  # should be 5


if __name__ == "__main__":
    main()
