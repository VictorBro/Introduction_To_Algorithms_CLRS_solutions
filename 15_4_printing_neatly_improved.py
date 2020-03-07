def print_solution(r, text_arr, j):
    if j >= 0:
        print_solution(r, text_arr, r[j] - 1)
        print(text_arr[r[j]: j + 1])


def print_neatly(l, M, text_arr):
    n = len(l)
    extra = []
    p = []
    c = [-1] * n
    r = [-1] * n

    for i in range(n):
        p.append([float("inf")] * n)
        extra.append([0] * n)
        # r.append([-1] * n)

    for i in range(n):
        for j in range(i, n):
            if l[j] > M:
                raise Exception("text has word that exceeds row length")
            if i == j:
                extra[i][j] = M - l[j]
            else:
                extra[i][j] = extra[i][j - 1] - l[j] - 1
            if extra[i][j] >= 0:
                if j == n - 1:
                    p[i][j] = 0
                else:
                    p[i][j] = extra[i][j] ** 3

    c[0] = p[0][0]
    r[0] = 0
    for j in range(1, n):  # optimal arrangement of words 0,...,j
        c[j] = p[0][j]
        r[j] = 0
        for i in range(1, j + 1):
            if c[j] > c[i - 1] + p[i][j]:
                c[j] = c[i - 1] + p[i][j]
                r[j] = i
    print(c[n - 1])
    # print(c)
    # print(r)
    print_solution(r, text_arr, n - 1)
    # for i in range(n):
    #     for j in range(n):
    #         print(extra[i][j], end=" ")
    #     print()
    # for i in range(n):
    #     for j in range(n):
    #         print(p[i][j], end=" ")
    #     print()


def main():
    text = "Buffy the Vampire Slayer fans are sure to get their fix with the DVD release of the show's first season. " \
           "The three-disc collection includes all 12 episodes as well as many extras. There is a collection of " \
           "interviews by the show's creator Joss Whedon in which he explains his inspiration for the show as well as " \
           "comments on the various cast members. Much of the same material is covered in more depth with Whedon's " \
           "commentary track for the show's first two episodes that make up the Buffy the Vampire Slayer pilot. The " \
           "most interesting points of Whedon's commentary come from his explanation of the learning curve he " \
           "encountered shifting from blockbuster films like Toy Story to a much lower-budget television series. The " \
           "first disc also includes a short interview with David Boreanaz who plays the role of Angel. Other " \
           "features include the script for the pilot episodes, a trailer, a large photo gallery of publicity shots " \
           "and in-depth biographies of Whedon and several of the show's stars, including Sarah Michelle Gellar, " \
           "Alyson Hannigan and Nicholas Brendon."
    # text = "Tushar Roy likes to code"
    # text = "aaa bb cc ddddd"
    text_arr = text.split(" ")
    l = []
    for word in text_arr:
        l.append(len(word))
    # print(l)
    M = 72
    print_neatly(l, M, text_arr)


if __name__ == "__main__":
    main()
