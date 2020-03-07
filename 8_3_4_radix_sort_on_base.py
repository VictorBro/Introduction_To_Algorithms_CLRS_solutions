def get_digit(num, base, digit_idx):
    for i in range(digit_idx):
        num //= base
    num %= base
    return num


def count_sort(A, d, k, digit_idx):
    n = len(A)
    B = [0] * n
    C = [0] * k
    for i in range(n):  # O(n)
        digit = get_digit(A[i], k, digit_idx)
        print(digit)
        C[digit] += 1
    for i in range(1, k):  # O(n)
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):  # O(n)
        digit = get_digit(A[i], k , digit_idx)
        B[C[digit] - 1] = A[i]
        C[digit] -= 1
    for i in range(n):  # O(n)
        A[i] = B[i]


# Sort n numbers in range from 0 to n^3 – 1 in linear time
def radix_sort(A):
    n = len(A)
    d = 3
    k = n
    for i in range(d):  # O(n)
        count_sort(A, d, k, i)


def main():
    A = [0, 123, 114, 112, 90]
    radix_sort(A)
    print(A)


if __name__ == "__main__":
    main()
