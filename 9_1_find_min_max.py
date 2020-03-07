def find_min_max(A):  # O(3 * n/2)
    n = len(A)
    min_val = max_val = A[0]
    start = 1
    if n % 2 == 0:
        start = 2
        if A[0] > A[1]:
            min_val = A[1]
            max_val = A[0]
        else:
            max_val = A[1]
    for i in range(start, n - 1, 2):
        if A[i] > A[i + 1]:
            if min_val > A[i + 1]:
                min_val = A[i + 1]
            if max_val < A[i]:
                max_val = A[i]
        else:
            if min_val > A[i]:
                min_val = A[i]
            if max_val < A[i + 1]:
                max_val = A[i + 1]
    return min_val, max_val


def main():
    # A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(find_min_max(A))


if __name__ == "__main__":
    main()
