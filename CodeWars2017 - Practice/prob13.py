def prob13():
    """Incomplete"""
    text = int(input())
    solution = []
    direction = "r"
    x, y = 0, 0
    for char in text:
        char = char.lower()
        if char in ("l", "r", "u", "d"):
            direction = char

        if direction == "l":
            if x != 0:
                x -= 1
            solution[y].insert(x, char)