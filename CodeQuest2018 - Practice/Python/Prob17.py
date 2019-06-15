file = open("Prob17.in.txt")
n = int(file.readline().strip())
for x in range(n):
    line = file.readline().strip()
    if len(set(line[:3])) == 1 and line[0] != "-":
        print(line, "=", line[0], "WINS")
    elif len(set(line[3:6])) == 1 and line[3] != "-":
        print(line, "=", line[3], "WINS")
    elif len(set(line[6:])) == 1 and line[6] != "-":
        print(line, "=", line[6], "WINS")
    elif len({line[0], line[4], line[8]}) == 1 and line[0] != "-":
        print(line, "=", line[0], "WINS")
    elif len({line[2], line[4], line[6]}) == 1 and line[2] != "-":
        print(line, "=", line[2], "WINS")
    elif len({line[0], line[3], line[6]}) == 1 and line[0] != "-":
        print(line, "=", line[0], "WINS")
    elif len({line[1], line[4], line[7]}) == 1 and line[1] != "-":
        print(line, "=", line[1], "WINS")
    elif len({line[2], line[5], line[8]}) == 1 and line[2] != "-":
        print(line, "=", line[2], "WINS")
    else:
        print(line, "=", "TIE")