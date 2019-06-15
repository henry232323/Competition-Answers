def run(crosses):
    for t, f in crosses:
        for ot, of in crosses:
            if ((t, f) != (ot, of)):
                if (ot % t == 0 and of % t != 0):
                    print("They go forever!")
                    return
        else:
            continue

    for n in range(max(item[1] for item in crosses), 10 ** 8):
        for t, f in crosses:
            if (n - f) % t != 0:
                break
        else:
            print(n)
            break


d = input()
while d != "0":
    c, *nums = (int(x) for x in d.split())
    crosses = []
    for i, num in enumerate(nums):
        if i != 0:
            crosses.append((num, num + crosses[i - 1][1]))
        else:
            crosses.append((num, num))

    # print(crosses)
    run(crosses)
    d = input()
