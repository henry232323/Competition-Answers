def readint():
    return int(input())


def readlist(delimiter=","):
    return input().split(delimiter)


def readlistint(delimiter=","):
    return [int(x.strip()) for x in input().split(delimiter)]


from collections import defaultdict
for x in range(readint()):
    cities = defaultdict(list)
    for y in range(readint() - 1):
        a, b = readlist(" ")
        cities[a].append(b)
        cities[b].append(a)
    beginning, end = readlist(" ")

    path = [beginning]
    last = None
    current = beginning
    while current != end:
        dc = current
        if len(cities[current]) == 1:
            current = cities[current][0]
        else:
            current = next(filter(lambda x: x != last, cities[current]))
        path.append(current)
        last = dc

    print("\n".join(path))
