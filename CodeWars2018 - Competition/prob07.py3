while True:
    vals = input()
    print(vals)
    if vals == "0":
        break

    nvals, *values = (int(x) for x in input().split())

    biggest = []
    for _ in range(3):
        big = max(values, key=lambda x: abs(x))
        biggest.append(big)
        values.remove(big)

    while True:
        nn = []
        for item in biggest:
            if item < 0:
                nn.append(item)

        if len(nn) % 2 == 0:
            print(biggest[0] * biggest[1] * biggest[2])
            break

        biggest.remove(min(biggest, key=lambda x: abs(x)))
        big = max(values, key=lambda x: abs(x))
        biggest.append(big)