years = "Rat Ox Tiger Rabbit Dragon Snake Horse Sheep Monkey Rooster Dog Pig".split()
#2008 + years.index(item)

zod = {
    "Aries": [("March", 21), ("April", 19)],
    "Taurus": [("April", 20), ("May", 20)],
    "Gemini": [("May", 20), ("June", 20)],
    "Cancer": [("June", 20), ("July", 20)],
    "Leo": [("July", 20), ("August", 20)],
    "Virgo": [("August", 20), ("September", 20)],
    "Libra": [("September", 20), ("October", 20)],
    "Scorpio": [("October", 20), ("November", 20)],
    "Sagittarius": [("November", 20), ("December", 20)],
    "Capricorn": [("December", 20), ("January", 20)],
    "Aquarius": [("January", 20), ("February", 20)],
    "Pisces": [("February", 20), ("March", 20)],
}

months = "January February March April May June July August September October November December".split()
year, month, day = (int(x) for x in input().split("-"))
month = months[month-1]
for key, [p1, p2] in zod.items():
    #print(p1, p2)
    if month in p1 or month in p2:
        #print("made it!")
        if month in p1 and day >= p1[1]:
            zodiac = key
            break
        elif month in p2 and day <= p2[1]:
            zodiac = key
            break
    else:
        continue

ytype = years[((year - 2008) % 12)]
print(f"If you were born on {month} {day}, your sign is {zodiac}.")
print(f"{year} is the year of the {ytype}.")
