from collections import Counter

spelling = "ZERO ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN ELEVEN TWELVE".split()
*d, end = input().split()

counters = []
for n in d:
    counters.append(Counter(spelling[int(n)]))

nc = Counter()
for c in counters:
    for item, val in c.items():
        nc[item] = max(nc[item], val)

chars = ""
for item, val in nc.items():
    chars += item * val

print(" ".join(d) + ".", " ".join(sorted(chars)))