f = open("prob19.txt")
key, *lines = f.readlines()

ckey = 0
for n, char in enumerate(key.strip("\n")):
    ckey += (-1)**(n) * ord(char)
while ckey < 32:
    ckey += 32
while ckey > 126:
    ckey -= 16

print("Key =", ckey)

for l in lines:
    items = []
    for c in l.strip("\n"):
        items.append((hex(ord(c) * ckey)[2:]).lower())

    print(",".join(items))
