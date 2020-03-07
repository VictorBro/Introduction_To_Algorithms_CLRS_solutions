# sort 0,1 in place in O(n) not stable
def partition(A):
    n = len(A)
    i = -1
    for j in range(n):
        if A[j] <= 0:
            i += 1
            A[i], A[j] = A[j], A[i]


def main():
    A = [1, 0, 1, 0, 1, 1, 0]
    partition(A)
    print(A)


if __name__ == "__main__":
    main()
