def counting_sort(A, k):
    n = len(A)
    C = [0] * (k+1)
    for i in range(n):
        C[A[i]] += 1
    j = 0
    for i in range(k + 1):
        while C[i] > 0:
            A[j] = i
            C[i] -= 1
            j += 1


def main():
    A = [7, 5, 7, 8, 4, 2, 7, 4, 4, 4]
    counting_sort(A, max(A))
    print(A)


if __name__ == "__main__":
    main()
