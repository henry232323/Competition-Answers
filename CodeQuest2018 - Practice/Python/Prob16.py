from math import sin, cos, pi

file = open("Prob16.in.txt")
n = int(file.readline().strip())
for x in range(n):
    part = file.readline().strip()
    print(part)
    xc, yc, p, r1, r2 = (int(x) for x in part.split())
    angle = 2 * pi / 5
    for x in range(10):
        pa = angle * (x // 2)
        if x % 2 == 0:
            print("{1:.2f},{0:.2f}".format(r1 * cos(pa) + xc, r1 * sin(pa) + yc), end=" ")

        else:
            pa += pi / 5
            print("{1:.2f},{0:.2f}".format(r2 * cos(pa) + xc, r2 * sin(pa) + yc), end=" ")
