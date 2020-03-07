def LCS(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    if n1 < n2:
        s1, s2 = s2, s1
        n1, n2 = n2, n1
    c = [0] * (n2 + 1 + 1)
    top = 1
    left = n2 + 1
    curr_val = 0
    for i in range(1, n1 + 1):
        top = 0
        for j in range(1, n2 + 1):
            top += 1
            if s1[i-1] == s2[j-1]:
                curr_val = c[top-1] + 1
            elif c[top] >= c[left]:
                curr_val = c[top]
            else:
                curr_val = c[left]
            c[top-1] = c[left]
            c[left] = curr_val
        c[top] = c[left]
        c[left] = 0
    for i in range(n2 + 1 + 1):
        print(c[i], end=" ")
    print()
    return curr_val


def main():
    s1 = "ABCBDAB"
    s2 = "BDCABA"
    print(LCS(s1, s2))


if __name__ == "__main__":
    main()
