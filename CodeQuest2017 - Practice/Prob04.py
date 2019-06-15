f = open(__file__.split(".")[-2] + ".in.txt")
ncases = int(f.readline().strip())
for i in range(ncases):
    a = int(f.readline().strip()) - 1
    print("a =", round((.5+.5*5**.5)**a/(5**.5)))
