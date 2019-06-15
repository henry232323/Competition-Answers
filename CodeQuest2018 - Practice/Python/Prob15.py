file = open("Prob15.in.txt")
n = int(file.readline().strip())
key = "abcdefghijklmnopqrstuvwxyz".upper()
for x in range(n):
    ans = ""
    for c in file.readline().strip():
        idx = key.index(c) + 1
        #print(idx)
        if idx <= 5:
            ans += key[(idx + 6) % 26 - 1]
        elif 5 < idx <= 10:
            ans += key[idx ** 2 % 26 - 1]
        elif 10 < idx <= 15:
            ans += key[((idx % 3) * 5 + 1) % 26 - 1]
        elif 15 < idx <= 20:
            ans += key[sum(int(x) for x in str(idx)) * 8 % 26 - 1]
        elif 20 < idx <= 26:
            for x in range(idx-1, 0, -1):
                #print(idx, x, idx % x)
                if idx % x == 0:
                    divisor = x
                    break
            ans += key[(divisor * 2) % 26 - 1]

    print(ans)
