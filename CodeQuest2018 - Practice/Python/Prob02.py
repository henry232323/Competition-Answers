file = open("Prob02.in.txt")
n = int(file.readline().strip())
for x in range(n):
    print(len(list(filter(lambda c: c in "aeiou", file.readline().strip()))))
