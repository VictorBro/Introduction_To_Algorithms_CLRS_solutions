import math

second = 10**6
minute = second * 60
hour = minute * 60
day = hour * 24
month = day * 30
year = day * 365
century = year * 100


def find_largest_n_for_t(method, t):
    n = 1
    res = method(n)
    while True:
        res = method(n * 2)
        if res < t:
            n *= 2
        else:
            break
    while True:
        res = method(n + 1)
        if res < t:
            n += 1
        else:
            break
    return n


def find_largest_n(method, method_name):
    print(method_name, "second: ", find_largest_n_for_t(method, second))
    print(method_name, "minute: ", find_largest_n_for_t(method, minute))
    print(method_name, "hour: ", find_largest_n_for_t(method, hour))
    print(method_name, "day: ", find_largest_n_for_t(method, day))
    print(method_name, "month: ", find_largest_n_for_t(method, month))
    print(method_name, "year: ", find_largest_n_for_t(method, year))
    print(method_name, "century: ", find_largest_n_for_t(method, century))


def calc_log(n):
    return math.log(n, 2)


def calc_sqrt(n):
    return math.sqrt(n)


def calc_linear(n):
    return n


def calc_nlogn(n):
    return n*math.log(n, 2)


def calc_n_mul_n(n):
    return n*n


def calc_n_mul_n_mul_n(n):
    return n**3


def calc_exp(n):
    return 2**n


def calc_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


#find_largest_n(calc_log, "log")
#find_largest_n(calc_sqrt, "sqrt")
#find_largest_n(calc_linear, "linear")
#find_largest_n(calc_nlogn, "nlogn")
find_largest_n(calc_n_mul_n, "n^2")
find_largest_n(calc_n_mul_n_mul_n, "n^3")
find_largest_n(calc_exp, "2^n")
find_largest_n(calc_factorial, "n!")
