from collections import deque

vactrains = dict(A=[], B=[], C=[])

pending = deque()
nsent = 0
while True:
    cmd = input()
    if cmd == "DONE":
        break
    cmd, *values = cmd.split()

    if cmd == "RECV":
        print("RECVED", values)
        pending.append(values)
    elif cmd == "LOAD":
        val = pending.popleft()
        vactrains[values[0]].append(val)
    elif cmd == "XFER":
        vactrains[values[1]].append(vactrains[values[0]].pop())
    elif cmd == "SEND":
        nsent += 1
        print("VACTRAIN", nsent)
        for item in reversed(vactrains[values[0]]):
            print(*item)
        vactrains[values[0]] = []
