h, m, s = (int(x) for x in input().split())

if (h <= m / s):
    print(h, m, s, "I will make it!")
else:
    print(h, m, s, "I will be late!")