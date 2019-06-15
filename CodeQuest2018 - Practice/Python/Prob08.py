file = open("Prob08.in.txt")
n = int(file.readline().strip())

for x in range(n):
    nums = [(float(z) - 180) % 360 for z in file.readline().strip().split()]
    print("{:.2f} {:.2f} {:.2f}".format(*nums))
