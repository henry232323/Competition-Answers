d = input()
while input != '0':
    ninputs, *anums = [int(x) for x in d.split()]
    cnums = anums[::]

    mx1 = max(cnums)
    cnums.remove(mx1)
    mx2 = max(cnums)
    cnums.remove(mx2)
    mx3 = max(cnums)
    cnums.remove(mx3)

    mn1 = min(anums)
    anums.remove(mn1)
    mn2 = min(anums)
    anums.remove(mn2)

    print(max(mn1 * mn2 * mx1, mx1 * mx2 * mx3))

    d = input()