def readint():
    return int(input())


def readlist(delimiter=","):
    return input().split(delimiter)


def readlistint(delimiter=","):
    return [int(x.strip()) for x in input().split(delimiter)]

fs = "abcdefghijklmnopqrstuvwxyz"

import math

for x in range(readint()):
    height = readint()
    dist = (40075 / 2 / math.pi) + height

    answer = dist * 2 * math.pi
    print(round(answer, 1))