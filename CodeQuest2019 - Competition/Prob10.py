def readint():
    return int(input())


def readlist(delimiter=","):
    return input().split(delimiter)


def readlistint(delimiter=","):
    return [int(x.strip()) for x in input().split(delimiter)]

fs = "abcdefghijklmnopqrstuvwxyz"

for x in range(readint()):
    offset = readint()
    s = input()
    fin = ""
    for c in s:
        if c not in fs:
            fin += c
            continue
        fin += fs[(fs.index(c) - offset) % 26]

    print(fin)