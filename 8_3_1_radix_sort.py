def get_digit(num, digit_idx):
    for i in range(digit_idx):
        num //= 10
    num %= 10
    return num


def counting_sort(A, k, digit_idx):
    n = len(A)
    B = [0] * n
    C = [0] * k
    for i in range(n):
        digit = get_digit(A[i], digit_idx)
        C[digit] += 1
    for i in range(1, k):
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        digit = get_digit(A[i], digit_idx)
        B[C[digit] - 1] = A[i]
        C[digit] -= 1
    for i in range(n):
        A[i] = B[i]


def radix_sort(A, d):
    for i in range(d):
        counting_sort(A, 10, i)
        print(A)


def main():
    A = [329, 457, 657, 839, 436, 720, 355]
    radix_sort(A, 3)


if __name__ == "__main__":
    main()
