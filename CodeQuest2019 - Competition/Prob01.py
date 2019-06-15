def readint():
    return int(input())


def readlist(delimiter=","):
    return input().split(delimiter)


def readlistint(delimiter=","):
    return [int(x.strip()) for x in input().split(delimiter)]


for x in range(readint()):
    i = readlistint(" ")
    a = i[0]
    b = i[1]

    if a != b:
        print(a + b)
    else:
        print(2 * (a + b))