def prob05():
    nlines = int(input())
    players = {}
    for x in range(nlines):
        team, distance, speed = input().split()
        score = float(distance) / float(speed)
        players[team] = score

    winner = min(players.items(), key=lambda y: y[1])
    print(winner[0], winner[1])