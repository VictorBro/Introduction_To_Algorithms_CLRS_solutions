def LCS_helper(s1, s2, i, j, c):
    if i == 0 or j == 0:
        c[i][j] = 0
        return 0
    if c[i][j] != -1:
        return c[i][j]
    if s1[i-1] == s2[j-1]:
        c[i][j] = LCS_helper(s1, s2, i - 1, j - 1, c) + 1
    else:
        top = LCS_helper(s1, s2, i - 1, j, c)
        left = LCS_helper(s1, s2, i, j - 1, c)
        c[i][j] = max(top, left)
    return c[i][j]


def print_LCS(s1, s2, i, j, c):
    if c[i][j] == 0:
        return
    if s1[i-1] == s2[j-1]:
        print_LCS(s1, s2, i - 1, j - 1, c)
        print(s1[i-1], end=" ")
    elif c[i-1][j] >= c[i][j-1]:
        print_LCS(s1, s2, i - 1, j, c)
    else:
        print_LCS(s1, s2, i, j - 1, c)


def LCS(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    c = []
    for i in range(n1 + 1):
        c.append([-1] * (n2 + 1))
    LCS_helper(s1, s2, n1, n2, c)
    for i in range(n1 + 1):
        for j in range(n2 + 1):
            print("{:2d}".format(c[i][j]), end=" ")
        print()
    print_LCS(s1, s2, n1, n2, c)
    return c


def main():
    s1 = "ABCBDAB"
    s2 = "BDCABA"
    LCS(s1, s2)


if __name__== "__main__":
    main()
