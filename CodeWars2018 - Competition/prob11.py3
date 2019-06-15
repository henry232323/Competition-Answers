ngroups = int(input())
for x in range(ngroups):
    groupsize = int(input())
    players = []
    for y in range(groupsize):
        skill, name = input().split()
        skill = int(skill)
        players.append((skill, name))



