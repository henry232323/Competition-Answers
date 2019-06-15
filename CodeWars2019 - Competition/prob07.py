d = input()
while d != "0 0":
    n, m = (int(x) for x in d.split())
    if m == 0:
        if n % 2 == 0:
            print(n + 2)
        else:
            print(n + 1)
    elif m == 1:
        x = n
        if n == 0:
            print(2)
        else:
            while True:
                x += 1
                for i in range(2, int(x ** 0.5)):
                    if x % i == 0:
                        break
                else:
                    print(x)
                    break

    elif m == 2:
        print((int(n**0.5)+1)**2)

    else:
        print((int(n ** (1/3)) + 1) ** 3)

    d = input()