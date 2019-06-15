f = open(__file__.split(".")[-2] + ".in.txt")
ncases = int(f.readline().strip())
for i in range(ncases):
    name, idx = f.readline().strip().split()
    idx = int(idx)
    print(name[:idx] + name[idx + 1:])
