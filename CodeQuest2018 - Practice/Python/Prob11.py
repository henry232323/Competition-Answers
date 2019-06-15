file = open("Prob11.in.txt")
n = int(file.readline().strip())

for x in range(n):
    Cr, Cg, Cb, T, Fr, Fg, Fb, Br, Bg, Bb = [int(x) for x in file.readline().strip().split()]
    Fd = ((Fr - Cr)**2 + (Fg-Cg)**2 + (Fb - Cb)**2)**0.5
    if Fd < T:
        print(Br, Bg, Bb)
    else:
        print(Fr, Fg, Fb)
    Bd = ((Br - Cr)**2 + (Bg-Cg)**2 + (Bb - Cb)**2)**0.5
