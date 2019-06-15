from collections import Counter

def prob11():
    rows, columns, noise = (int(x) for x in input().split())
    nsolutions = [int(x) for x in input().split()]
    length = nsolutions.pop(0)
    val = " ".join(input() for x in range(rows)).split()
    numbers = Counter(val)
    removers = []
    for char, n in numbers.items():
        if n >= noise:
            removers.append(char)

    for char in removers:
        while char in val:
            val.remove(char)

    solution = []
    for n in nsolutions:
        sol, val = val[:n], val[n:]
        solution.append("".join(sol))

    print(" ".join(solution))