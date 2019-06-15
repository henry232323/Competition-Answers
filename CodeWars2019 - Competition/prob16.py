i = input()
allowed = {
    "is": 2,
    "had": 2,
}
words = i.split()
for i, word in enumerate(words):
    if i >= len(words)-2:
        if words[-2].lower() not in allowed:
            break
    d = word.lower()
    if d in allowed:
        while words[i+1].lower() == d == words[i+2].lower():
            del words[i+2]
    else:
        while words[i+1].lower() == d:
            del words[i+1]
print(" ".join(words))