file = open("prob10.txt")
import datetime
for line in file.readlines():
    if ":" in line:
        a, b = line.strip().split(":")
        b = int(b)
        y, m, d = (int(x) for x in a.split("-"))

        if b == 0:
            date = datetime.datetime(y, m, d) + datetime.timedelta(days=364)
            y = date.year
            if y % 4 == 0 and y % 100 != 0:
                date += datetime.timedelta(days=1)
            m = date.month
            d = date.day
            print(f"Will still be 0 up to {y+b}-{str(m).zfill(2)}-{str(d).zfill(2)} if born on {a}")
        else:
            print(f"Will be {b} on {y+b}-{str(m).zfill(2)}-{str(d).zfill(2)} if born on {a}")
    else:
        a, b = line.strip().split()

        ya, ma, da = (int(x) for x in a.split("-"))
        yb, mb, db = (int(x) for x in b.split("-"))

        at = datetime.datetime(ya, ma, da)
        bt = datetime.datetime(yb, mb, db)
        years = (bt - at).total_seconds() / 60 / 60 / 24 / 365
        print(f"If born on {a}, will be {int(years)} years old on {b}")
