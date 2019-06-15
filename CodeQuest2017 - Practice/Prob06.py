f = open(__file__.split(".")[-2] + ".in.txt")
ncases = int(f.readline().strip())

rap = "ALPHA BRAVO CHARLIE DELTA ECHO FOXTROT GOLD HOTEL INDIA JULIET KILO LIMA MIKE NOVEMBER OSCAR PAPA QUEBEC ROMEO SIERRA TANGO UNIFORM VICTOR WHISKEY XRAY YANKEE ZULU".split()
rap.append(" ")
letters = "abcdefghijklmnopqrstuvwxyz "

for i in range(ncases):
    ndcases = f.readline().strip()
    for b in range(int(ndcases)):
        msg = f.readline().strip().split()
        fmsg = []
        for word in msg:
            #print(word)
            fmsg.append("-".join(map(lambda x: rap[letters.index(x.lower())], word)))

        print(" ".join(fmsg))
