file = open("Prob10.in.txt")
n = int(file.readline().strip())

for x in range(n):
    R, C = (int(i) for i in file.readline().strip().split(","))
    r1, c1 = (int(j) for j in file.readline().strip().split(","))
    r2, c2 = (int(k) for k in file.readline().strip().split(","))

    n = (r1 + c2) % 2
    print("Yes" if (r2 + c2) % 2 == n else "No")