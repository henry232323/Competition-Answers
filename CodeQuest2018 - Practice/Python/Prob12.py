file = open("Prob12.in.txt")
n = int(file.readline().strip())

for x in range(n):
    limit = int(file.readline().strip())
    nums = list(range(limit + 1))
    nums[1] = None
    nums[0] = None
    for i, n in zip(range(limit//2), nums):
        if n is None:
            continue
        ct = 2*n
        elim = 0
        while ct <= limit:
            if nums[ct]:
                nums[ct] = None
                elim += 1
            ct += n
        if elim:
            print(f"Prime {n} Composite Set Size:  {elim}")

    print("{" + ", ".join(str(i) for i in filter(lambda d: d, nums)) + "}")
