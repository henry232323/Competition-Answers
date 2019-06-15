cases = int(input())
for _ in range(cases):
    val0 = input()
    val = val0
    val = val.replace("(", "")
    val = val.replace(")", "")
    val = val.replace(".", "")
    val = val.replace("-", "")

    if val[0] in ("0", "1"):
        # print(val0, "01")
        print(val0, "INVALID")
        continue

    if val[1] == "9":
        # print(val0, 9)
        print(val0, "INVALID")
        continue

    if val[3] in ("0", "1"):
        # print(val0, 4, "01")
        print(val0, "INVALID")
        continue

    if val[4] + val[5] == "11":
        print(val0, "INVALID")
        continue

    print(val0, "VALID")
