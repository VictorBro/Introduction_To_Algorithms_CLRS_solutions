def median_of_2n(A, a_start, a_end, B, b_start, b_end):
    if a_start == a_end or b_start == b_end:
        return min(A[a_end], B[b_end])
    a_mid = (a_start + a_end) // 2
    b_mid = (b_start + b_end) // 2
    if A[a_mid] < B[b_mid]:
        return median_of_2n(A, a_mid, a_end, B, b_start, b_mid)
    elif A[a_mid] > B[b_mid]:
        return median_of_2n(A, a_start, a_mid, B, b_mid, b_end)
    else:
        return A[a_mid]


def main():
    A = [1, 3, 5]
    B = [2, 4, 6]
    print(median_of_2n(A, 0, len(A) - 1, B, 0, len(B) - 1))

    A = [15, 26, 38]
    B = [2, 13, 17]
    print(median_of_2n(A, 0, len(A) - 1, B, 0, len(B) - 1))

    A = [2, 6, 9, 10, 11]
    B = [1, 5, 7, 12, 15]
    print(median_of_2n(A, 0, len(A) - 1, B, 0, len(B) - 1))

    A = [7]
    B = [2]
    print(median_of_2n(A, 0, len(A) - 1, B, 0, len(B) - 1))

    A = [1, 3, 5]
    B = [1, 3, 5]
    print(median_of_2n(A, 0, len(A) - 1, B, 0, len(B) - 1))


if __name__ == "__main__":
    main()
