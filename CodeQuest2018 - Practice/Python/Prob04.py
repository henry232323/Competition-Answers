file = open("Prob04.in.txt")
n = int(file.readline().strip())
for x in range(n):
    choices = sorted(file.readline().strip().split())

    if choices.count("R") == 1 and "P" not in choices:
        print("ROCK")

    elif choices.count("P") == 1 and "S" not in choices:
        print("PAPER")

    elif choices.count("S") == 1 and "R" not in choices:
        print("SCISSORS")

    else:
        print("NO WINNER")
