def readint():
    return int(input())


def readlist(delimiter=","):
    return input().split(delimiter)


def readlistint(delimiter=","):
    return [int(x.strip()) for x in input().split(delimiter)]

fs = "abcdefghijklmnopqrstuvwxyz"

for x in range(readint()):
    f = readint()
    n = 2**f
    for i in range(n):
        print(bin(i)[2:].zfill(f))