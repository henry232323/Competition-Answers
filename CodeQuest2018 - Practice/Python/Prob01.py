file = open("Prob01.in.txt")
n = int(file.readline().strip())
for x in range(n):
    grade = int(file.readline().strip())
    if grade >= 70:
        print("PASS")
    else:
        print("FAIL")