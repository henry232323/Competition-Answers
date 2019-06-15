def prob06():
    nlines = int(input())
    for x in range(nlines):
        diffs = []
        finals = []
        _, last, *inp = input().split()
        for item in inp:
            diffs.append(-int(item) + int(last))
        inp.insert(0, "0")

        for diff, init in zip(diffs, inp):
            print(init)
            finals.append(diff + int(init))

        print(finals)