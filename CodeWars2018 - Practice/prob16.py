ncases = int(input())
for case in range(ncases):
    num = int(input())
    for x in range(1, num + 1):
        if "".join(sorted(str(x) + str(num-x))) == "0123456789":
            if "".join(sorted(str(x * (num - x)))) == "0123456789":
                print(f"{num} : {x} * {num - x} = {x * (num - x)}")
                break
