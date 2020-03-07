def LCS(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    c = []
    for i in range(n1 + 1):
        c.append([0] * (n2 + 1))
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i-1] == s2[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i][j-1]
    return c


def print_LCS(s1, i, j, c):
    if i == 0 or j == 0 or c[i][j] == 0:
        return
    new_i = i
    new_j = j
    if c[i][j] == c[i-1][j]:
        new_i = i - 1
    elif c[i][j] == c[i][j-1]:
        new_j == j - 1

    if new_i == i and new_j == j:
        new_i = i - 1
        new_j = j - 1
        print_LCS(s1, new_i, new_j, c)
        print(s1[i-1], end=" ")
    else:
        print_LCS(s1, new_i, new_j, c)


def main():
    s1 = "ABCBDAB"
    s2 = "BDCABA"
    c = LCS(s1, s2)
    n1 = len(s1)
    n2 = len(s2)
    for i in range(n1 + 1):
        for j in range(n2 + 1):
            print(c[i][j], end=" ")
        print()
    print_LCS(s1, n1, n2, c)


if __name__ == "__main__":
    main()
