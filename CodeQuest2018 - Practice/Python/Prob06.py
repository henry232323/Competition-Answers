file = open("Prob06.in.txt")
n = int(file.readline().strip())
typ = ["off", "red", "green", "blue"]
for x in range(n):
    ec = 0
    for i, item in enumerate(reversed(file.readline().strip().split())):
        if item == "BROKEN":
            ec += 2**i

    left = int(ec / 4)
    right = ec - (left * 4)

    print(typ[left], typ[right])