from datetime import timedelta

f = open(__file__.split(".")[-2] + ".in.txt")
ncases = int(f.readline().strip())
for i in range(ncases):
    dist, speed = (float(x) for x in f.readline().strip().split())
    time = dist/speed * 3600 * 10**6
    days, time = divmod(time, (3600 * 24))
    #print(days, time)
    hours, time = divmod(time, 3600)
    minutes, time = divmod(round(time), 60)

    print("Time to Mars: {} days, {} hours, {} minutes, {} seconds".format(*[round(x) for x in [days, hours, minutes, time]]))