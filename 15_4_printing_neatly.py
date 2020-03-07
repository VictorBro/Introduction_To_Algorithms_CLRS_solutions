def print_neatly_helper(l, n, M, p, r):
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            chars_num = j - i

            for q in range(i, j + 1):
                if l[q] > M:
                    raise Exception("this text couldn't be printed neatly")
                chars_num += l[q]

            if chars_num > M:
                for k in range(i, j):
                    if p[i][j] > p[i][k] + p[k + 1][j]:
                        p[i][j] = p[i][k] + p[k + 1][j]
                        r[i][j] = k
            else:
                if j == n - 1:
                    p[i][j] = 0
                else:
                    p[i][j] = (M - chars_num) ** 3
    return p[0][n - 1]


def print_solution(r, text_arr, i, j):
    if i <= j:
        if r[i][j] == -1:
            print(text_arr[i: j + 1])
        else:
            print_solution(r, text_arr, i, r[i][j])
            print_solution(r, text_arr, r[i][j] + 1, j)


def print_neatly(l, M, text_arr):
    n = len(l)
    p = []
    r = []
    for i in range(n):
        p.append([float("inf")] * n)
        r.append([-1] * n)
    res = print_neatly_helper(l, n, M, p, r)
    print(res)
    print_solution(r, text_arr, 0, n - 1)


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
    print(l)
    M = 72
    print_neatly(l, M, text_arr)

    text = ["Buffy the Vampire Slayer fans are sure to get their fix with the DVD",
            "release of the show's first season. The three-disc collection includes",
            "all 12 episodes as well as many extras. There is a collection of",
            "interviews by the show's creator Joss Whedon in which he explains",
            "his inspiration for the show as well as comments on the various cast",
            "members. Much of the same material is covered in more depth with",
            "Whedon's commentary track for the show's first two episodes that make",
            "up the Buffy the Vampire Slayer pilot. The most interesting points of",
            "Whedon's commentary come from his explanation of the learning curve",
            "he encountered shifting from blockbuster films like Toy Story to a",
            "much lower-budget television series. The first disc also includes a",
            "short interview with David Boreanaz who plays the role of Angel. Other",
            "features include the script for the pilot episodes, a trailer, a large",
            "photo gallery of publicity shots and in-depth biographies of Whedon and",
            "several of the show's stars, including Sarah Michelle Gellar, Alyson",
            "Hannigan and Nicholas Brendon."]
    sumi = 0
    for i in range(len(text) - 2):
        sumi += (M - len(text[i])) ** 3
    print(sumi)


if __name__ == "__main__":
    main()
