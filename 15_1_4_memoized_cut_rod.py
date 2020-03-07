def memoized_cut_rod_aux(prices, n, r, seq):
    if n == 0:
        return 0
    if n < len(r):
        return r[n]
    max_val = 0
    tmp_slice = 0
    for i in range(1, n + 1):
        tmp = memoized_cut_rod_aux(prices, n - i, r, seq)
        if max_val < prices[i - 1] + tmp:
            max_val = prices[i - 1] + tmp
            tmp_slice = i
    r.append(max_val)
    seq.append(tmp_slice)
    return r[n]


def memoized_cut_rod(prices, n):
    r = [0]
    seq = [0]
    max_revenue = memoized_cut_rod_aux(prices, n, r, seq)
    return max_revenue, seq


def print_seq(seq, n):
    while n > 0:
        print(seq[n], end=" ")
        n -= seq[n]
    print()


def main():
    prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    max_revenue, seq = memoized_cut_rod(prices, 4)
    print(max_revenue)
    print_seq(seq, 4)


if __name__ == "__main__":
    main()
