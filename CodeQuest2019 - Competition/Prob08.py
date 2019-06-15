def readint():
    return int(input())


def readfloat():
    return float(input())


def readlist(delimiter=","):
    return input().split(delimiter)


def readlistint(delimiter=","):
    return [int(x.strip()) for x in input().split(delimiter)]


from math import hypot

for x in range(readint()):
    focus = readlistint(" ")
    #print(focus)
    grid = [[0] * 20 for x in range(20)]

    for i in range(20):
        for j in range(20):
            if i == focus[0] and j == focus[1]:
                grid[i][j] = 100

            elif hypot(i - focus[0], j - focus[1]) < 2:
                grid[i][j] = 50

            elif 3 > hypot(i - focus[0], j - focus[1]) >= 2:
                grid[i][j] = 25

            else:
                grid[i][j] = 10

    for row in grid:
        print(*row)
