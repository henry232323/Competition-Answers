nlines = int(input())
for _ in range(nlines):
    val = int(input())
    for x in range(val):
        tv = val - x
        tn = str(tv)
        if len(tn + str(x)) == len(set(tn) | set(str(x))):
            tvx = tv * x
            if len(str(tvx)) != 10:
                continue
            if len(str(tvx)) == len(set(str(tvx))):
                print(val, ":", x, "*", tv, "=", tvx)
                break