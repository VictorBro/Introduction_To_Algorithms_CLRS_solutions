def bottom_up_cut_rop(prices, n):
    r = [0]
    seq = [0]
    for i in range(1, n + 1):
        max_val = prices[i - 1]
        first_slice = i
        for j in range(1, i):
            if max_val < prices[j - 1] + r[i - j]:
                max_val = prices[j - 1] + r[i - j]
                first_slice = j
        r.append(max_val)
        seq.append(first_slice)
    return r[n], seq


def print_path(seq, n):
    while n > 0:
        print(seq[n], end=" ")
        n -= seq[n]
    print()


def main():
    prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    revenue, seq = bottom_up_cut_rop(prices, 4)
    print("revenue:", revenue)
    print_path(seq, 4)


if __name__ == "__main__":
    main()
