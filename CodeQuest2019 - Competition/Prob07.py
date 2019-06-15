def readint():
    return int(input())

def readfloat():
    return float(input())

def readlist(delimiter=","):
    return input().split(delimiter)


def readlistint(delimiter=","):
    return [int(x.strip()) for x in input().split(delimiter)]

fs = "abcdefghijklmnopqrstuvwxyz"

import math

for x in range(readint()):
    nums = []
    for y in range(readint()):
        inp = readfloat()
        nums.append(inp)
    mi = min(nums)
    ma = max(nums)
    count = 0

    for y in range(len(nums)):
        print(round((nums[count] - mi) / (ma - mi) * 255))

        count += 1