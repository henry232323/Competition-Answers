from math import ceil, sqrt

while True:
    n = input().strip()
    if n == "0":
        break

    fail = False
    for x in range(1, len(n)):
        val = int(n[:x]) + int(n[x:])

        if val == 1:
            fail = True
        for y in range(2, int(ceil(sqrt(val)))):
            if val % y == 0:
                fail = True
                break

        if fail:
            print(n, "PETTY")
            break

    else:
        print(n, "MAGNANIMOUS")
