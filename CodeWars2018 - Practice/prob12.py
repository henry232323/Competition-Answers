cases = dict()
for i in range(int(input())):
    d = input()
    cases["".join(sorted(d.replace(" ", "")))] = d
for i in range(int(input())):
    d = input()
    st = "".join(sorted(d.replace(" ", "")))
    if st in cases:
        print("Yes:", cases[st])
    else:
        print("No: No matching case")
