f = open(__file__.split(".")[-2] + ".in.txt")
ncases = int(f.readline().strip())
for i in range(ncases):
    name, scores = f.readline().strip().split(":")
    scores = scores.split(",")
    s = [0, 0, 0, 0]
    total = 0
    for item in scores:
        if item == "K":
            total += 1
            continue
        if item == "HR":
            item = "4B"
        if item[1] == "B" and item[0] != "B":
            s[int(item[0]) - 1] += 1
            total += 1

    avg = (s[0] + 2 * s[1] + 3 * s[2] + 4 * s[3])
    print(f"{name}={avg/total:.3f}")
