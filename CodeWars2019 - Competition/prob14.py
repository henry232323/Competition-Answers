a, b = int(input()), int(input())
items = [a, b]
for x in range(int(input())-2):
    a, b = b, b + a
    items.append(b)
print(items)