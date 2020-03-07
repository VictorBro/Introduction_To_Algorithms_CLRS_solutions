def partition(A, start, end):
    pivot = A[end]
    i = start - 1
    count = 1  # count values that equal to pivot
    for j in range(start, end):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
            if A[i] == pivot:
                count += 1
    i += 1
    A[i], A[end] = A[end], A[i]
    if count == end - start + 1:
        return (start + end) // 2
    else:
        return i


def main():
    A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    pivot_idx = partition(A, 0, len(A) - 1)
    print(pivot_idx)

    A = [2, 2, 2, 2, 2, 2, 2]
    pivot_idx = partition(A, 0, len(A) - 1)
    print(pivot_idx)


if __name__ == "__main__":
    main()
