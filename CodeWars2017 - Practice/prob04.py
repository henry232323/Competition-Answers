def prob04():
    nlines = int(input())
    for x in range(nlines):
        miles, time = input().split()
        print(float(miles) / (float(time) / 60))