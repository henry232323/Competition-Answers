ipt = input()
while ipt != "0 0 0":
    v, a, t = (float(x) for x in ipt.split())
    print(v * t + .5*a*t**2)
    ipt = input()
