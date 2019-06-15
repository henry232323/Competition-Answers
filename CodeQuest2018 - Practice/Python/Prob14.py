file = open("Prob14.in.txt")
n = int(file.readline().strip())
for x in range(n):
    U = int(file.readline().strip())
    upperlines = [int(x) for x in file.readline().strip().split()]
    L = int(file.readline().strip())
    lowerlines = [int(x) for x in file.readline().strip().split()]
    message = file.read()
    lmessage = ""
    umessage = ""
    idu = 0
    idl = 0
    lmc, umc = 0, 0

    for c in message:
        if c.islower() or c == "=":
            lmessage += c
            lmc += 1
            if lmc == lowerlines[idl]:
                lmessage += "\n"
                idl += 1
                lmc = 0
        elif c.isupper() or c == "-":
            umessage += c
            umc += 1
            if umc == upperlines[idu]:
                umessage += "\n"
                idu += 1
                umc = 0

    lmessage = lmessage.replace("=", " ")
    umessage = umessage.replace("-", " ")

    print(umessage)
    print()
    print(lmessage)
