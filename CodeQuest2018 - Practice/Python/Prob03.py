file = open("Prob03.in.txt")
n = int(file.readline().strip())
items = {
    "1": "st",
    "2": "nd",
    "3": "rd",
    "11": "th",
    "12": "th",
    "13": "th"
}
for x in range(n):
    num = file.readline()[:-3]
    if num in items:
        print(num + items[num])
    elif num[-1] in items:
        print(num + items[num[-1]])
    else:
        print(num + "th")