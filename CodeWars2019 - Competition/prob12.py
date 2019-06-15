iter = int(input())
decimal = int(input())

pi = 3

for i in range(2, iter**2, 2):
    pi += (-1)**(i/2) * (4/(i) * (i+1) * (i + 2))

print(pi)
print(str(pi)[decimal+1])