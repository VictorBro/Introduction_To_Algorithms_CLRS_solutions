from math import sqrt
# reference: Introduction to Algorithms - Cormen Solution
# http://www.jade-cheng.com/uh/coursework/ics-311/homework/homework-08.pdf
# https://stackoverflow.com/questions/874982/how-to-compute-optimal-paths-for-traveling-salesman-bitonic-tour
# http://marcodiiga.github.io/bitonic-tour


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


def merge(arr, left, mid, right):
    L = arr[left: mid + 1]
    L_size = mid - left + 1
    R = arr[mid + 1: right + 1]
    R_size = right - mid
    k = left
    i = j = 0
    while i < L_size and j < R_size:
        if L[i].x <= R[j].x:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < L_size:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < R_size:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def distance(a, b):
    x = (b.x - a.x) ** 2
    y = (b.y - a.y) ** 2
    z = sqrt(x + y)
    return z


# t[i,j] clockwise bitonic path starting from i and ending in j
# t[0,1] = dist[0,1]
# t[i,j] = t[i,j-1] + dist[j-1,j] if i < j - 1
# t[i,j] = min{t[k,i] + dist[k,j]}, 0 <= k < i
def bitonic_tour(points):
    n = len(points)
    tour_lengths = []
    tour = []

    merge_sort(points, 0, n - 1)

    for i in range(n):
        tour_lengths.append([0] * n)
        tour.append([-1] * n)

    for j in range(1, n):
        tour_lengths[0][j] = tour_lengths[0][j - 1] + distance(points[j - 1], points[j])
        tour[0][j] = j - 1

    for i in range(1, n):
        for j in range(i, n):
            if i < j - 1:
                tour_lengths[i][j] = tour_lengths[i][j - 1] + distance(points[j - 1], points[j])
                tour[i][j] = j - 1
            else:
                tour_lengths[i][j] = tour_lengths[0][i] + distance(points[0], points[j])
                tour[i][j] = 0
                for k in range(1, i):
                    temp = tour_lengths[k][i] + distance(points[k], points[j])
                    if tour_lengths[i][j] > temp:
                        tour_lengths[i][j] = temp
                        tour[i][j] = k

    for i in range(n):
        for j in range(n):
            print("{:6.3f}".format(tour_lengths[i][j]), end=" ")
        print()

    for i in range(n):
        for j in range(n):
            print("{:2d}".format(tour[i][j]), end=" ")
        print()

    return tour, tour_lengths[n - 1][n - 1]


def print_path(points, tour, i, j):
    if i < j:
        k = tour[i][j]
        print(points[k], end="->")
        if k > 0:
            print_path(points, tour, i, k)
    else:
        k = tour[j][i]
        if k > 0:
            print_path(points, tour, k, j)
            print(points[k], end="->")


def print_tour(points, tour):
    n = len(points)
    print(points[n - 1], end="->")
    print(points[n - 2], end="->")
    k = tour[n - 2][n - 1]
    print_path(points, tour, k, n - 2)
    if k > 0:
        print(points[k], end="->")
    print()


def main():
    points = [Point(1, 0), Point(6, 1), Point(8, 2), Point(7, 5),
              Point(5, 4), Point(0, 6), Point(2, 3)]
    # points = [Point(0, 6), Point(1, 2), Point(3, 0), Point(5, 2), Point(8, 6)]
    tour, length = bitonic_tour(points)

    for p in points:
        print(p, end=" ")
    print()

    print(length)
    print_tour(points, tour)

    # n = len(points)
    # dist = []
    # for i in range(n):
    #     dist.append([0] * n)
    # for i in range(n):
    #     for j in range(n):
    #         dist[i][j] = distance(points[i], points[j])
    #         print("{:6.3f}".format(dist[i][j]), end=" ")
    #     print()


if __name__ == "__main__":
    main()
