while True:
    v, a, t = input().split()
    if (v, a, t) == ("0", "0", "0"):
        break
    print(float(v) * float(t) + (1/2) * (float(a)*float(t)**2))