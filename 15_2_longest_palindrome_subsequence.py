def LCS(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    p = []
    solution_path = []
    for i in range(n1 + 1):
        p.append([0] * (n2 + 1))
        solution_path.append(['*'] * (n2 + 1))

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                p[i][j] = 1 + p[i - 1][j - 1]
                solution_path[i][j] = '\\'
            else:
                if p[i - 1][j] >= p[i][j - 1]:
                    p[i][j] = p[i - 1][j]
                    solution_path[i][j] = '|'
                else:
                    p[i][j] = p[i][j - 1]
                    solution_path[i][j] = '-'
    for i in range(n1 + 1):
        for j in range(n2 + 1):
            print(p[i][j], end=" ")
        print("    ", end="")
        for j in range(n2 + 1):
            print(solution_path[i][j], end=" ")
        print()
    return solution_path


def print_solution(solution_path, s, i, j):
    if i == 0 or j == 0:
        return
    if solution_path[i][j] == '\\':
        print_solution(solution_path, s, i - 1, j - 1)
        print(s[i - 1], end=" ")
    elif solution_path[i][j] == '|':
        print_solution(solution_path, s, i - 1, j)
    else:
        print_solution(solution_path, s, i, j - 1)


def longest_palindrome(word):
    reversed_word = word[::-1]
    solution_path = LCS(word, reversed_word)
    n = len(word)
    print_solution(solution_path, word, n, n)


def main():
    # word = "character"
    # word = "aibohphobia"
    word = "tracecar"
    longest_palindrome(word)


if __name__ == "__main__":
    main()
