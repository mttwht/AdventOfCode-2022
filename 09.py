with open("input-09.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# # Example input:
# lines = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2
# """.splitlines()
# Example answer = 1


# # Example input 2:
# lines = """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20
# """.splitlines()
# # Example answer = 36


def parse_move(line: str) -> (str, int):
    direction, distance = line.split()
    return str(direction), int(distance)


def move_h(h, move):
    x, y = h
    if move[0] == "U":
        y += move[1]
    elif move[0] == "D":
        y -= move[1]
    elif move[0] == "L":
        x -= move[1]
    elif move[0] == "R":
        x += move[1]
    return (x, y)


def move_t(t, h):
    positions = set()
    x, y = t
    while abs(x - h[0]) > 1 or abs(y - h[1]) > 1:
        if x != h[0] and y != h[1]:
            # need to move diagonally
            if x < h[0]:
                x += 1
            else:
                x -= 1
            if y < h[1]:
                y += 1
            else:
                y -= 1
        else:
            if x < h[0] - 1:
                x += 1
            elif x > h[0] + 1:
                x -= 1
            elif y < h[1] - 1:
                y += 1
            elif y > h[1] + 1:
                y -= 1
        positions.add((x, y))
    return (x, y), positions


def do_move(move, rope):
    global t_positions
    for i in range(move[1]):
        m = (move[0], 1)
        rope[0] = move_h(rope[0], m)
        for knot in range(1, len(rope)):
            rope[knot], positions = move_t(rope[knot], rope[knot - 1])
        t_positions = t_positions.union(positions)
    return rope


rope = [(0, 0)] * 10

t_positions = {rope[-1]}

for line in lines:
    move = parse_move(line)
    rope = do_move(move, rope)

print(len(t_positions))
# print(sorted(t_positions))
