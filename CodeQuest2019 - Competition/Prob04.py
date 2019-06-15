def readint():
    return int(input())


def readlist(delimiter=","):
    return input().split(delimiter)


def readlistint(delimiter=","):
    return [int(x.strip()) for x in input().split(delimiter)]


for x in range(readint()):
    inp = readlist(" ")
    a = int(inp[0])
    b = inp[1]

    if a <= 60 or (b == "true" and a <= 65):
        print("no ticket")
    elif a <= 80 or (b == "true" and a <= 85):
        print("small ticket")
    else:
        print("big ticket")