file = open("prob22.txt")
cnames = False
for line in files.readlines():
    if line.startswith("~"):
        cnames = True

    if not cnames:
        name, coords = line.strip().split("|")
        coords = coords.replace("(", "").replace(")", "")
    else:

