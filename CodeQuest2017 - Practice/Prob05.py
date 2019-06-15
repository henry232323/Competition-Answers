f = open(__file__.split(".")[-2] + ".in.txt")
ncases = int(f.readline().strip())
for i in range(ncases):
    first = set(f.readline().strip().split(","))
    second = set(f.readline().strip().split(","))
    print(",".join(sorted(first - second)))
    print(",".join(sorted(first & second)))
    print(",".join(sorted(second - first)))