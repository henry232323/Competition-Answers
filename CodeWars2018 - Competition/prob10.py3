cases = int(input())

for _ in range(cases):
    total = 0
    top, nlayers = (int(x) for x in input().split())
    base = int(top ** (1 / 2))
    for ln in range(nlayers):
        v = base + ln
        nliters = 4 * v + v ** 2 - (0 if ln == 0 else (v - 1)) ** 2
        total += nliters

    print(total, 'liters')
