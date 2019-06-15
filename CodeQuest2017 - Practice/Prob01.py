f = open(__file__.split(".")[-2] + ".in.txt")
ncases = int(f.readline().strip())
for i in range(ncases):
    ipt = f.readline()

    print(ipt * 2, end="")