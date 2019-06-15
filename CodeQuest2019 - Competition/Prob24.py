from collections import defaultdict
from math import floor, ceil

with open("Prob24.in.txt") as pf:
    board = [list(x) for x in pf.read().split("\n")]

rboard = dict()

for i in range(len(board)):
    for j in range(len(board[i])):
        c = board[i][j]
        if board[i][j] != ".":
            rboard[i, j] = [board[i][j]]
        else:
            rboard[i, j] = list("123456789")

for i in range(len(board)):
    for j in range(len(board[i])):
        if len(rboard[i, j]) > 1:
            print(".", end="")
        else:
            print(rboard[i, j][0], end="")
    print()
print()

while not all(len(x) == 1 for x in rboard.values()):
    for i in range(len(board)):  # For each tile on the board
        for j in range(len(board[i])):
            cs = rboard[i, j]  # The current board possibilities are here
            # print(cs)
            if len(cs) > 1:
                c = cs[0]
                for sj in range(len(board[i])):
                    if sj == j:
                        continue
                    if c in rboard[(i, sj)]:
                        # print(f"Removing {c} at ({i}, {sj})")
                        rboard[(i, sj)].remove(c)

                for si in range(len(board)):
                    if si == i:
                        continue
                    if c in rboard[(si, j)]:
                        # print(f"Removing {c} at ({si}, {j})")
                        rboard[(si, j)].remove(c)

                b = i or 1
                d = j or 1
                for si in range(floor(b / 3) * 3, ceil(b / 3) * 3):
                    for sj in range(floor(d / 3) * 3, ceil(d / 3) * 3):
                        if (si, sj) == (i, j):
                            continue
                        else:
                            # print((si, sj), (i, j), c, rboard[(si, sj)])
                            if c in rboard[(si, sj)]:
                                # print(f"Removing {c} at ({si}, {sj})")
                                rboard[(si, sj)].remove(c)



    for i in range(len(board)):
        for j in range(len(board[i])):
            if len(rboard[i, j]) > 1:
                print(".", end="")
            else:
                print(rboard[i, j][0], end="")
        print()
    print()
    import time; time.sleep(3)

for i in range(len(board)):
    for j in range(len(board[i])):
        print(rboard[i, j][0], end="")
    print()
