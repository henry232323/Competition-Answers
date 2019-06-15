d = input()
while d != "0 0":
    s, l = (int(i) for i in d.split())
    if len(str(s)) > l:
        print(s, l, 0)
        d = input()
        continue
    chars = ""
    n = s
    while len(chars) < l:
        chars += str(n)
        n += 1

    print(s, l, n-1)
    d = input()