COPY = 0
REPLACE = 1
DELETE = 2
INSERT = 3
TWIDDLE = 4
KILL = 5


def edit_distance(s1, s2, costs):
    n1 = len(s1)
    n2 = len(s2)
    distances = []
    transform_path = []

    for i in range(n1 + 1):
        distances.append([0] * (n2 + 1))
        transform_path.append(['*'] * (n2 + 1))

    for i in range(0, n1 + 1):
        for j in range(0, n2 + 1):
            if i == 0:  # distances[0][0] = 0
                distances[i][j] = j * costs[INSERT]
                transform_path[i][j] = 'i'
            if j == 0:
                if costs[KILL] <= i * costs[DELETE]:
                    distances[i][j] = costs[KILL]
                    transform_path[i][j] = 'k'
                else:
                    distances[i][j] = i * costs[DELETE]
                    transform_path[i][j] = 'd'

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                distances[i][j] = distances[i - 1][j - 1] + costs[COPY]
                transform_path[i][j] = 'c'
            else:
                distances[i][j] = distances[i - 1][j - 1] + costs[REPLACE]
                transform_path[i][j] = "r"

            if i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]:
                if distances[i][j] > distances[i - 2][j - 2] + costs[TWIDDLE]:
                    distances[i][j] = distances[i - 2][j - 2] + costs[TWIDDLE]
                    transform_path[i][j] = 't'

            if distances[i][j] > distances[i - 1][j] + costs[DELETE]:
                distances[i][j] = distances[i - 1][j] + costs[DELETE]
                transform_path[i][j] = 'd'

            if distances[i][j] > distances[i][j - 1] + costs[INSERT]:
                distances[i][j] = distances[i][j - 1] + costs[INSERT]
                transform_path[i][j] = 'i'

    for k in range(n1):
        if distances[n1][n2] > distances[k][n2] + costs[KILL]:
            distances[n1][n2] = distances[k][n2] + costs[KILL]
            transform_path[n1][n2] = 'k'

    for i in range(n1 + 1):
        for j in range(n2 + 1):
            print("{:2d}".format(distances[i][j]), end=" ")
        print()

    print("   ", end=" ")
    for j in range(n2):
        print(s2[j], end=" ")
    print()
    for i in range(n1 + 1):
        for j in range(n2 + 1):
            if j == 0 and 0 < i:
                print(s1[i - 1], end=" ")
            elif j == 0 and i == 0:
                print(" ", end=" ")
            print(transform_path[i][j], end=" ")
        print()

    return transform_path, distances


def print_solution(s1, s2, transform_path, distances, i, j):
    if i == 0 and j == 0:
        return

    op = transform_path[i][j]
    if op == 'c' or op == 'r':
        print_solution(s1, s2, transform_path, distances, i - 1, j - 1)
    elif op == 't':
        print_solution(s1, s2, transform_path, distances, i - 2, j - 2)
    elif op == 'd':
        print_solution(s1, s2, transform_path, distances, i - 1, j)
    elif op == 'i':
        print_solution(s1, s2, transform_path, distances, i, j - 1)
    elif op == 'k':
        min_distance = distances[0][j]
        min_idx = 0
        for k in range(1, i):
            if min_distance > distances[k][j]:
                min_distance = distances[k][j]
                min_idx = k
        print_solution(s1, s2, transform_path, distances, min_idx, j)
    print(op, end="")


def main():
    s1 = "algorithm"
    s2 = "altruistic"
    costs = [2, 2, 3, 3, 1, 1]
    # costs = [0, 1, 2, 2, 3, 3]
    transform_path, distances = edit_distance(s1, s2, costs)
    print(distances[len(s1)][len(s2)])
    print_solution(s1, s2, transform_path, distances, len(s1), len(s2))
    print()


if __name__ == "__main__":
    main()
