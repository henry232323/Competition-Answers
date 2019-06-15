file = open("Prob05.in.txt")
n = int(file.readline().strip())
for x in range(n):
    n = int(file.readline().strip())
    seq = [n]
    while seq[-1] != 1:
        if seq[-1] % 2 == 0:
            seq.append(seq[-1] / 2)
        else:
            seq.append(3 * seq[-1] + 1)

    print(f"{n}:{len(seq)}")