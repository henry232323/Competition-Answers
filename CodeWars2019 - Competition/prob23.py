import datetime

file = open("datasets/prob23-1-in.txt")
posts = []
nposters = set()
for i, line in enumerate(file.readlines()):
    title, name, likes, dislikes, fcount, following, blocked, datepost, dateacct, total = line.strip().split("|")
    nposters.add(name)
    score = 10000
    if int(fcount) >= 1000000:
        score += 10000
    elif int(fcount) < 100:
        score -= 5000
    if likes != dislikes:
        score %= (int(likes) - int(dislikes))
    else:
        score %= 100

    if following == "true":
        score += 5000
    y, m, d = (int(x) for x in datepost.split("-"))
    datetoday = datetime.datetime.today()
    postdate = datetime.datetime(y,m,d)
    acctdate = datetime.datetime(*(int(x) for x in datepost.split("-")))

    if datetoday - postdate <= datetime.timedelta(weeks=1):
        score += 500
    elif datetoday - postdate >= datetime.timedelta(weeks=2):
        score -= 100

    score += int(total)
    score += (datetoday - acctdate).total_seconds() / 60 / 60 / 24 / 7
    if blocked != "true":
        posts.append((score, -i, title, name, datepost))

if posts:
    posts.sort(reverse=True)
    for score, i, title, name, datepost in posts:
        print(f"({score:.1f}) {title}, by: {name} [{datepost}]")
else:
    print(f"You are blocking all ({nposters}) posters in your feed")
