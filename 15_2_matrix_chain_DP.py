def matrix_chain(p):
    n = len(p) - 1
    m = []
    solution_path = []
    for i in range(n):
        m.append([0] * n)
        solution_path.append([0] * n)
    for l in range(2, n + 1):   # num of matrices in multiplication
        for i in range(n - l + 1):  # start from matrix i
            # optimal_val = float("inf")
            j = i + l - 1
            optimal_val = m[i][i] + m[i+1][j] + p[i]*p[i+1]*p[j+1]
            solution_path[i][j] = i
            for k in range(i + 1, j):
                if optimal_val > m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]:
                    optimal_val = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                    solution_path[i][j] = k
            m[i][j] = optimal_val
    return m[0][n - 1], solution_path


def print_solution(solution_path, start, end):
    if start == end:
        print("A" + str(start), end=" ")
    else:
        print("(", end=" ")
        print_solution(solution_path, start, solution_path[start][end])
        print_solution(solution_path, solution_path[start][end] + 1, end)
        print(")", end=" ")


def main():
    # p = [30, 35, 15, 5, 10]  # 4 matrices
    p = [30, 35, 15, 5, 10, 20, 25]
    optimal_val, solution_path = matrix_chain(p)
    print(optimal_val)
    print_solution(solution_path, 0, len(solution_path) - 1)


if __name__ == "__main__":
    main()
