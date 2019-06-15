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
    nums = input().split(" ")
    k = complex(float(nums[0]), float(nums[1]))
    zc = 0
    n = 1
    while True:
        zc = zc ** 2 + k
        if zc.real ** 2 + zc.imag ** 2 >= 100 ** 2:
            break
        if n >= 51:
            break
        n += 1

    if n <= 10:
        c = "RED"
    elif n <= 20:
        c = "ORANGE"
    elif n <= 30:
        c = "YELLOW"
    elif n <= 40:
        c = "GREEN"
    elif n <= 50:
        c = "BLUE"
    else:
        c = "BLACK"

    print(f"{nums[0]}{'+' if float(nums[1]) >= 0 else ''}{nums[1]}i", c)
