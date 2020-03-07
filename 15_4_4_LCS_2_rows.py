def LCS(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    if n1 < n2:
        s1, s2 = s2, s1
        n1, n2 = n2, n1
    c = []
    for i in range(2):
        c.append([0] * (n2 + 1))
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i-1] == s2[j-1]:
                c[1][j] = c[0][j-1] + 1
            elif c[0][j] >= c[1][j-1]:
                c[1][j] = c[0][j]
            else:
                c[1][j] = c[1][j-1]
            c[0][j-1] = c[1][j-1]
            if j == n2:
                c[0][j] = c[1][j]
    for i in range(2):
        for j in range(n2 + 1):
            print(c[i][j], end=" ")
        print()
    return c[0][n2]


def main():
    s1 = "ABCBDAB"
    s2 = "BDCABA"
    print(LCS(s1, s2))


if __name__ == "__main__":
    main()
