from math import log
from random import randint


def random(a, b):
    if a == b:
        return a
    n = int(log(b - a + 1) + 1)
    while True:
        temp = 0
        for i in range(n):
            temp <<= 1
            temp |= randint(0, 1)
        if a + temp <= b:
            return a + temp


for k in range(20):
    print(random(3, 10))
