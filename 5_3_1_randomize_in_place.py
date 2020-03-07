from random import randint


def randomize_in_place(A):
    n = len(A)
    for i in range(n):
        j = randint(i, n - 1)
        # swap
        A[i], A[j] = A[j], A[i]


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
randomize_in_place(arr)
print(arr)
