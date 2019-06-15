f = open(__file__.split(".")[-2] + ".in.txt")
ncases = int(f.readline().strip())
key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(ncases):
    text = f.readline().strip()
    final = ""
    for word in text.split():
        fword = word
        word = list(filter(str.isalpha, word))
        #print(word)
        for w, c in zip(word, reversed(word)):
            #print(w, c)
            if w.isupper():
                final += c.upper()
            else:
                final += c.lower()
        if not fword[-1].isalpha():
            final += fword[-1]
        final += " "

    print(final)