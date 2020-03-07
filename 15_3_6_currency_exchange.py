INVALID = -1
USD = 0
EUR = 1
ILS = 2
currency_dict = {USD: "USD", EUR: "EUR", ILS: "ILS", INVALID: "INVALID"}


def exchange(R, d, start, end, n):
    if n == 0:
        return INVALID, None
    currencies = len(R)
    m = []
    path = []
    for i in range(currencies):
        m.append([INVALID] * (n+1))
        path.append([INVALID] * (n+1))
    for i in range(currencies):
        m[i][1] = R[i][end]
        path[i][1] = end
    for k in range(2, n + 1):  # k is number of trades
        for i in range(currencies):  # i -> j, j ~> end
            m[i][k] = R[i][USD] * m[USD][k-1]
            path[i][k] = USD
            for j in range(1, currencies):
                if m[i][k] < R[i][j] * m[j][k-1]:
                    m[i][k] = R[i][j] * m[j][k - 1]
                    path[i][k] = j
    return m[start][n] * d, path


def print_path(path, start, n):
    if path is not None and n > 0:
        k = n
        print(currency_dict[start], end=" ")
        currency = start
        while k > 0:
            print("->", end=" ")
            currency = path[currency][k]
            print(currency_dict[currency], end=" ")
            k -= 1


def main():
    R = [[1, 0.5, 2],
         [1.5, 1, 3],
         [0.5, 1, 1]]
    max_revenue, path = exchange(R, 5, USD, ILS, 3)
    print(max_revenue)
    print(path)
    print_path(path, USD, 3)


if __name__ == "__main__":
    main()
