file = open("Prob19.in.txt")
n = int(file.readline().strip())
for x in range(n):
    rnum = [0, 0, 0, 0]
    rs = []
    for y in range(3):
        r, val = [int(i) for i in file.readline().strip().split()]
        rnum[r-1] = val
        rs.append(r-1)

    num = file.readline().strip()
    rotors = [
        [1, 3, 6, 0, 5, 4, 8, 7, 9, 2],
        [0, 3, 5, 2, 6, 9, 1, 4, 8, 7],
        [5, 9, 1, 7, 3, 8, 0, 2, 4, 6],
        [1, 6, 5, 2, 9, 0, 7, 4, 3, 8]
    ]
    ref= [3, 6, 8, 0, 5, 4, 1, 9, 2, 7]

    for r in range(4):
        if r not in rs:
            del rotors[r]
            del rnum[r]

    r1 = rotors[0]
    r2 = rotors[1]
    r3 = rotors[2]

    rfin = ""
    final = ""
    for c in num:
        n = int(c)
        v1 = r1[(n + rnum[0]) % 10]
        v2 = r2[(v1 + rnum[1]) % 10]
        v3 = r3[(v2 + rnum[2]) % 10]
        rev1 = ref[v3]
        rfin += str(rev1)
        rv1 = (r1.index(rev1) - rnum[0]) % 10
        rv2 = (r2.index(rv1)  - rnum[1]) % 10
        rv3 = (r3.index(rv2)  - rnum[2]) % 10
        final += str(rv3)

        rnum[2] += 1
        if rnum[2] == 10:
            rnum[1] += 1
            if rnum[1] == 10:
                rnum[0] += 1

        #print(c, v1, v2, v3, rev1, rv1, rv2, rv3)

    print(rfin, final)