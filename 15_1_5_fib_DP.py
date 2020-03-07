def fib(n):
    a1 = 0
    a2 = 1

    if n < 1:
        raise Exception("invalid argument")
    elif n == 1:
        return a1
    elif n == 2:
        return a2

    res = 0
    for i in range(2, n):
        res = a1 + a2
        a1 = a2
        a2 = res
    return res


def main():
    print(fib(9))


if __name__ == "__main__":
    main()
