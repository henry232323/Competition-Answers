file = open("Prob13.in.txt")
n = int(file.readline().strip())
for x in range(n):
    ncases = int(file.readline().strip())
    users = {}
    items = file.readline().strip().split("]")
    users["name"] = items[0].strip("[,]").split(",")
    users["age"] = items[1].strip("[,]").split(",")
    users["username"] = items[2].strip("[,]").split(",")
    users["handle"] = items[3].strip("[,]").split(",")
    users["number"] = items[4].strip("[,]").split(",")
    users["address"] = items[5].strip("[,]").split(",")
    # print(users)

    for y in range(ncases):
        name = file.readline().strip()
        idx = users["name"].index(name)
        print(f"Name: {name}")
        print(f"Age: {users['age'][idx]}")
        print(f"Instagram: {users['username'][idx]}")
        print(f"Twitter: {users['handle'][idx]}")
        print(f"Phone: {users['number'][idx]}")
        print(f"Email: {users['address'][idx]}")
