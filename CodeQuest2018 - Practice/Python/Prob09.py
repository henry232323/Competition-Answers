file = open("Prob09.in.txt")
n = int(file.readline().strip())

for x in range(n):
    nums = [int(x) for x in file.readline().strip().split(",")]
    A = max(nums)
    B = min(nums)


    if A == 1 and 1 == B:
        print("1-1=0")
        print("COPRIME")
        continue

    while A-B != 0:
        print(f"{A}-{B}={A-B}")
        D = A-B
        A, B = max(D, B), min(D, B)

    print(f"{A}-{B}={A-B}")
    if A != 1:
        print("NOT COPRIME")
    else:
        print("COPRIME")
