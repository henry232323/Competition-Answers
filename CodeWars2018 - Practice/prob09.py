d = int(input())

while d != 0:
    b = bin(d)
    zct = b.count("0") - 1
    oct = b.count("1")
    if oct > zct:
        kind = "HEAVY"
    elif zct > oct:
        kind = "LIGHT"
    else:
        kind = "BALANCED"
    print(d, kind)

    d = int(input())
