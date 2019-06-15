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
import string

for f in range(readint()):
    ninputs = readint()
    cipher = input()
    keys = [input() for d in range(ninputs)]

    for key in keys:
        fin = ""
        for x in range(0, len(cipher), 2):
            chars = cipher[x:x+2]
            hx = int(chars, 16)

            keychars = key[x:x+2]
            khx = int(keychars, 16)

            n = hx ^ khx
            if n >= 256:
                break

            fin += chr(n)

        print(f"[{fin}]")




