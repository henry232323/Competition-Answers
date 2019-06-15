def readint():
    return int(input())


def readlist(delimiter=","):
    return input().split(delimiter)


def readlistint(delimiter=","):
    return [int(x.strip()) for x in input().split(delimiter)]

fs = "abcdefghijklmnopqrstuvwxyz"

import math

for x in range(readint()):
    a, b, length = readlistint(" ")

    cur = 0
    while b >= 1 and cur + 5 <= length:
        cur += 5
        b -= 1

    while a >= 1 and cur + 1 <= length:
        cur += 1
        a -= 1

    if cur == length:
        print("true")
    else:
        print("false")