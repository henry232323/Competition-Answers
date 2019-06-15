while True:
    val = int(input())
    if val == 0:
        break

    a, b = bin(val)[2:].count("1"), bin(val)[2:].count("0")
    if a > b:
        print(val, "HEAVY")
    elif b > a:
        print(val, "LIGHT")
    else:
        print(val, "BALANCED")