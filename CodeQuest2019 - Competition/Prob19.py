def readint():
    return int(input())


def readfloat():
    return float(input())


def readlist(delimiter=","):
    return input().split(delimiter)


def readlistint(delimiter=","):
    return [int(x.strip()) for x in input().split(delimiter)]


from collections import defaultdict
import cmath

for x in range(readint()):
    addrs = []
    fbstring = ""
    for y in range(readint()):
        bstring = ""
        for n in readlistint("."):
            bstring += bin(n)[2:].zfill(8)

        addrs.append(bstring)

    for i in range(len(addrs[0])):
        if len({a[i] for a in addrs}) == 1:
            fbstring += "".join(addrs[0][i])
        else:
            break

    g = len(fbstring)
    fbstring += "0" * (32 - len(fbstring))
    a = int(fbstring[0:8], base=2)
    b = int(fbstring[8:16], base=2)
    c = int(fbstring[16:24], base=2)
    d = int(fbstring[24:32], base=2)

    print(f"{a}.{b}.{c}.{d}/{g}")
