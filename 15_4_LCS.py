def LCS_helper(A, a_len, B, b_len):
    c = []
    path = []
    for i in range(a_len + 1):
        c.append([0] * (b_len + 1))
        path.append(['*'] * (b_len + 1))
    for i in range(1, a_len + 1):
        for j in range(1, b_len + 1):
            if A[i-1] == B[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                path[i][j] = '\\'
            else:
                if c[i][j-1] >= c[i-1][j]:
                    c[i][j] = c[i][j-1]
                    path[i][j] = '-'
                else:
                    c[i][j] = c[i-1][j]
                    path[i][j] = '|'
    return c, path


def print_LCS(A, i, j, path):
    if i == 0 or j == 0:
        return
    if path[i][j] == '\\':
        print_LCS(A, i-1, j-1, path)
        print(A[i-1], end=" ")
    elif path[i][j] == '-':
        print_LCS(A, i, j-1, path)
    else:
        print_LCS(A, i-1, j, path)


def LCS(A, B):
    a_len = len(A)
    b_len = len(B)
    c, path = LCS_helper(A, a_len, B, b_len)
    for i in range(a_len + 1):
        for j in range(b_len + 1):
            print(c[i][j], end=' ')
        print()
    for i in range(a_len + 1):
        for j in range(b_len + 1):
            print(path[i][j], end=' ')
        print()
    print_LCS(A, a_len, b_len, path)


def main():
    # s1 = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
    # s2 = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
    s1 = "ABCBDAB"
    s2 = "BDCABA"
    LCS(s1, s2)


if __name__ == "__main__":
    main()
