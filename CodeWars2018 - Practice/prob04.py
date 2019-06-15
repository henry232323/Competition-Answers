inp = open("prob04-1-in.txt")
for n in range(int(inp.readline())):
    g, s, b = (int(c) for c in inp.readline().split())
    if (b - 1) // 50 > 0:
        b -= 1
        s += b // 50
        b = b % 50 + 1

    if (s - 1) // 10 > 0:
        s -= 1
        g += s // 10
        s = s % 10 + 1

    print(g, s, b)
