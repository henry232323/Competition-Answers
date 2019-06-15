file = open("Prob07.in.txt")
n = int(file.readline().strip())
for x in range(n):
    subcases = int(file.readline().strip())
    np = []
    for i in range(subcases):
        n = file.readline().strip().lower()
        if n != n[::-1]:
            np.append(str(i + 1))

    if not np:
        print(True)
    else:
        print(False, "-", ", ".join(np))
