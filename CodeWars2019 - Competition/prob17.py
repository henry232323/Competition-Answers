from collections import Counter

d = input().replace(" ", "_")
c = Counter(d)

for i, v in sorted(c.items(), reverse=True, key=lambda x: (1, *x) if x[1] < 10 else (0, *x)):
    if v > 10:
        break
    print(f"{i}[{v}]", end="")
print(";", end="")
for i, v in sorted(c.items(), key=lambda x: (1, *x) if x[1] < 10 else (0, *x)):
    if v < 10:
        continue
    print(f"{i}[{v}]", end="")