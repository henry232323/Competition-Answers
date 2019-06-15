cases = int(input())
for _ in range(cases):
    g, s, b = (int(x) for x in input().split())

    sadd, sadr = divmod(b, 5)
    if sadr == 0:
        sadd, sadr = divmod(b - 1, 5)
        sadr += 1
    b = sadr
    s += sadd

    gadd, gadr = divmod(s, 10)
    if gadr == 0:
        gadd, gadr = divmod(s - 1, 10)
        gadr += 1

    s = gadr
    g += gadd

    print(g, s, b)
