f = open(__file__.split(".")[-2] + ".in.txt")
ncases = int(f.readline().strip())
key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(ncases):
    text = f.readline().strip()
    keyword = f.readline().strip()

    ans = ""
    k = 0
    for word in text.split():
        for c in word:
            offset = key.index(keyword[k])
            loc = key.index(c)
            ans += key[(loc + offset) % len(key)]
            k += 1
            k %= 4

        ans += " "

    print(ans.strip())