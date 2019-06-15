def readint():
    return int(input())

def readfloat():
    return float(input())

def readlist(delimiter=","):
    return input().split(delimiter)


def readlistint(delimiter=","):
    return [float(x.strip()) for x in input().split(delimiter)]


from collections import defaultdict
import cmath

for x in range(readint()):
    hh = "00"
    mm = "00"
    ss = "00"

    ipt = input()
    for i in range(len(ipt)):
        if ipt[i] == "h":
            if i == 1:
                hh = ipt[0]
            else:
                hh = ipt[i - 1: i]
            if ipt[i-2].isdigit():
                hh = ipt[i - 2: i]

        if ipt[i] == "m":
            if i == 1:
                mm = ipt[0]
            else:
                mm = ipt[i - 1: i]
            if ipt[i-2].isdigit():
                mm = ipt[i - 2: i]

        if ipt[i] == "s":
            if i == 1:
                ss = ipt[0]
            else:
                ss = ipt[i - 1: i]
            if ipt[i-2].isdigit():
                ss = ipt[i - 2: i]


    ss = int(ss)
    mm = int(mm)
    hh = int(hh)
    if ss >= 60:
        ss = ss % 60
        mm += ss // 60
    if mm >= 60:
        mm = mm % 60
        hh += mm // 60

    print(f"{str(hh).zfill(2)}:{str(mm).zfill(2)}:{str(ss).zfill(2)}")