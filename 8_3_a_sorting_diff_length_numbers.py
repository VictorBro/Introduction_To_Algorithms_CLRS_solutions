def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count


def get_digit(num, digit_idx):
    for i in range(digit_idx):
        num //= 10
    num %= 10
    return num


def counting_sort(A, digit_idx):
    n = len(A)
    k = 10
    C = [0] * k
    B = [0] * n
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


def radix_sort(A):
    digits_num = count_digits(A[0])
    for digit_idx in range(digits_num):
        counting_sort(A, digit_idx)


def get_max_length(A, n):
    max_length = 0
    for i in range(n):
        current_len = count_digits(A[i])
        if current_len > max_length:
            max_length = current_len
    return max_length


def bucket_sort(A):
    n = len(A)
    if n == 0:
        return

    max_length = get_max_length(A, n)
    if max_length == 0:
        return

    buckets = []
    for i in range(max_length + 1):
        buckets.append([])

    for i in range(n):
        digits_num = count_digits(A[i])
        buckets[digits_num].append(A[i])
    print(buckets)
    for i in range(max_length + 1):
        if len(buckets[i]) > 0:
            radix_sort(buckets[i])
    k = 0
    for i in range(max_length + 1):
        for j in range(len(buckets[i])):
            A[k] = buckets[i][j]
            k += 1


def main():
    A = [700, 5678, 23, 23, 44, 3]
    bucket_sort(A)
    print(A)


if __name__ == "__main__":
    main()
