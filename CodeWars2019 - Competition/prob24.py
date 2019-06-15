url = input()
out = ""
parts = url.split("//")
p1 = parts[0] + "//"
parts2 = parts[1].split("/")
durl = parts2[0]
p2 = url[len(p1) + len(durl):]
for char in p1:
    if not char.isalnum():
        char = "0x25" + hex(ord(char))[2:]
    out += char
out += durl
for char in p2:
    if not char.isalnum():
        char = "0x25" + hex(ord(char))[2:]
    out += char
print(out)# == open("prob24-1-out.txt").read().strip())