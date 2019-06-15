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
    gens = readint()
    map = []
    d = input()
    while d:
        try:
            map.append([0, *(int(x) for x in d), 0])
            d = input()
        except:
            d = ""

    map.insert(0, [0] * len(map[0]))
    map.append([0] * len(map[0]))

    nmap = map
    for _ in range(gens):
        for i in range(1, len(map) -1):
            for j in range(1, len(map[i])-1):
                if j == 0:
                    continue
                sum = (map[i-1][j-1] + map[i][j-1] + map[i-1][j] +
                        map[i+1][j+1] + map[i][j+1] + map[i+1][j] +
                       map[i+1][j-1] + map[i-1][j+1]
                       )

                if map[i][j] == 1 and sum < 2:
                    nmap[i][j] = 0
                if map[i][j] == 1 and sum < 4:
                    nmap[i][j] = 1
                if map[i][j] == 1 and sum >= 4:
                    nmap[i][j] = 0
                if map[i][j] == 0 and sum == 3:
                    nmap[i][j] = 1

        map = nmap

        for i in range(1, len(map)-1):
            for j in range(len(map[i])-1):
                print(map[i][j], end="")
            print()

        print()

