def cut_rod(prices, n, path):
    max_val = 0
    for i in range(1, n + 1):
        tmp = cut_rod(prices, n - i, path)
        if max_val < prices[i - 1] + tmp:
            max_val = prices[i - 1] + tmp
            path[n] = i
    return max_val


def print_path(path, n):
    while n > 0:
        print(path[n], end=" ")
        n -= path[n]
    print()


def main():
    prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    path = [0] * 11
    print("optimal revenue:", cut_rod(prices, 4, path))
    print_path(path, 4)


if __name__ == "__main__":
    main()
