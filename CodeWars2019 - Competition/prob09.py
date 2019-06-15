d = {
    "Scissors": ["Scissors cuts Paper", "Scissors decapitates Lizard"],
    "Paper": ["Paper covers Rock", "Paper disproves Spock"],
    "Rock": ["Rock crushes Lizard", "Rock crushes Scissors"],
    "Spock": ["Spock vaporizes Rock", "Spock smashes Scissors"],
    "Lizard": ["Lizard eats Paper", "Lizard eats Paper"]
}
a, b = input().split()
if a == b:
    print(f"TIE, {a} does not affect {a}")
else:
    for item in d[a]:
        if b in item:
            print(f"{a.upper()} WINS!", item)
            break
    else:
        for item in d[b]:
            if a in item:
                print(f"{a.upper()} LOSES!", item)
                break