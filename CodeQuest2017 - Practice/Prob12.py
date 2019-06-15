f = open(__file__.split(".")[-2] + ".in.txt")
ncases = int(f.readline().strip())
key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(ncases):
    ndays = int(f.readline().strip())
    bal = 0
    sum = 0
    for d in range(ndays):
        day, purchases, payments = f.readline().strip().split(",")

        bal -= 0 if not payments else float(payments)
        bal += 0 if not purchases else float(purchases)

        sum += bal


    P = sum / ndays * 0.18 / (365//ndays)

    print(P)