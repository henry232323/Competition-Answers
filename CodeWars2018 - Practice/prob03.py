inp = open("prob03-1-in.txt")
num = inp.readline().strip()
while num != '0':
    prime = True
    for x in range(1, len(num)):
        inum = int(num[:x]) + int(num[x:])

        for n in range(2, int(inum ** 0.5)):
            if inum % n == 0:
                prime = False
                break
        else:
            if (inum in (0, 1)):
                prime = False
            else:
                prime = True

        if not prime:
            break
    if prime:
        print(num, "MAGNANIMOUS")
    else:
        print(num, "PETTY")

    num = inp.readline().strip()
