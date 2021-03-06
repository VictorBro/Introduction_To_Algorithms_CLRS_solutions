from random import randint


def partition(A, start, end):
    pivot_idx = randint(start, end)
    pivot = A[pivot_idx]
    A[end], A[pivot_idx] = A[pivot_idx], A[end]

    i = start
    for j in range(start, end):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[end] = A[end], A[i]
    return i


def randomized_select(A, start, end, i):
    if i - 1 < start or i - 1 > end:
        raise Exception("Illegal order statistic")
    if start == end:
        return A[start]
    else:
        pivot_idx = partition(A, start, end)
        if pivot_idx > i - 1:
            return randomized_select(A, start, pivot_idx - 1, i)
        elif pivot_idx < i - 1:
            return randomized_select(A, pivot_idx + 1, end, i)
        else:
            return A[pivot_idx]


def main():
    # A = [7, 1, 2, 5, 4, 8, 9, 3, 6]
    A = [45, 3, 69, 97, 82, 32, 73, 40, 88, 15]
    print(randomized_select(A, 0, len(A) - 1, 6))


if __name__ == "__main__":
    main()
