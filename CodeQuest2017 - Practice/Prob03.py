f = open(__file__.split(".")[-2] + ".in.txt")
ncases = int(f.readline().strip())
for i in range(ncases):
    a, b = f.readline().strip().split()
    a = int(a)
    b = int(b)
    print(a + b, a * b)
