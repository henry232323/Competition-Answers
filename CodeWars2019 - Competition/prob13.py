a, b, c, d = input(), input(), input(), input()

if a == "X":
    print(int(b) * (int(c) / int(d)))
elif b == "X":
    print(int(a) * int(d) / int(c))
elif c == "X":
    print(int(a) * int(d) / int(b))
elif d == "X":
    print(int(c) * int(b) / int(a))
