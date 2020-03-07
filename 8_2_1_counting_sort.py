def counting_sort(A, k):
    n = len(A)
    B = [0] * n
    C = [0] * (k+1)
    for i in range(n):
        C[A[i]] += 1
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    return B


def main():
    A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
    B = counting_sort(A, max(A))
    print(B)


if __name__ == "__main__":
    main()
