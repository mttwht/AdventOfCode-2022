with open("input-23.txt", "r") as file:
    input_lines = [line.strip() for line in file.readlines()]

# # Example input:
# input_lines = [line.strip() for line in """
# ....#..
# ..###.#
# #...#.#
# .#...##
# #.###..
# ##.#.##
# .#..#..
# """.splitlines()][1:]
# # Example answer = 110

ELF, EMPTY = "#", "."
DIRECTION_SEQUENCE = "NSWE"
NORTH, EAST, SOUTH, WEST = "^>v<"

grove = input_lines


def trim(grove):
    while grove[0].count(ELF) == 0:
        grove.pop(0)
    while grove[-1].count(ELF) == 0:
        grove.pop(-1)
    while [row[0] for row in grove].count(ELF) == 0:
        grove = [row[1:] for row in grove]
    while [row[-1] for row in grove].count(ELF) == 0:
        grove = [row[:-1] for row in grove]
    return grove


def pad(grove: list[str]):
    if grove[0].count(ELF) > 0:
        grove.insert(0, EMPTY * len(grove[0]))
    if grove[-1].count(ELF) > 0:
        grove.append(EMPTY * len(grove[0]))
    if [row[0] for row in grove].count(ELF) > 0:
        grove = [EMPTY + row for row in grove]
    if [row[-1] for row in grove].count(ELF) > 0:
        grove = [row + EMPTY for row in grove]
    return grove


def propose(grove):
    moves = [[EMPTY, ] * len(row) for row in grove]
    for row in range(len(grove)):
        for col in range(len(grove[row])):
            if grove[row][col] == EMPTY:
                continue
            neighbours = "".join([r[col - 1:col + 2] for r in grove[row - 1:row + 2]])
            moves[row][col] = ELF
            if neighbours.count(ELF) == 1:
                continue
            for dir in DIRECTION_SEQUENCE:
                if dir == "N" and grove[row - 1][col - 1:col + 2].count(ELF) == 0:
                    moves[row][col] = NORTH
                    break
                if dir == "E" and not any(1 for r in grove[row - 1:row + 2] if r[col + 1] == ELF):
                    moves[row][col] = EAST
                    break
                if dir == "S" and grove[row + 1][col - 1:col + 2].count(ELF) == 0:
                    moves[row][col] = SOUTH
                    break
                if dir == "W" and not any(1 for r in grove[row - 1:row + 2] if r[col - 1] == ELF):
                    moves[row][col] = WEST
                    break
    return moves


def move(moves):
    for row in range(len(moves)):
        for col in range(len(moves[row])):
            target_cell: tuple[int, int]
            if moves[row][col] == EMPTY:
                continue
            elif moves[row][col] == NORTH:
                target_cell = row - 1, col
            elif moves[row][col] == EAST:
                target_cell = row, col + 1
            elif moves[row][col] == SOUTH:
                target_cell = row + 1, col
            elif moves[row][col] == WEST:
                target_cell = row, col - 1
            else:
                continue

            neighbours = []
            trow, tcol = target_cell
            if trow - 1 >= 0 and moves[trow - 1][tcol] == SOUTH:
                neighbours.append((trow - 1, tcol))
            if tcol + 1 < len(moves[row]) and moves[trow][tcol + 1] == WEST:
                neighbours.append((trow, tcol + 1))
            if trow + 1 < len(moves) and moves[trow + 1][tcol] == NORTH:
                neighbours.append((trow + 1, tcol))
            if tcol - 1 >= 0 and moves[trow][tcol - 1] == EAST:
                neighbours.append((trow, tcol - 1))

            if len(neighbours) == 1:
                r, c = neighbours[0]
                moves[row][col] = EMPTY
                moves[trow][tcol] = ELF
            else:
                for r, c in neighbours:
                    moves[r][c] = ELF
    return ["".join(row) for row in moves]


def do_turn(grove: list[str]) -> list[str]:
    global DIRECTION_SEQUENCE
    grove = pad(grove)

    # First half of round
    moves = propose(grove)

    # Second half of round
    grove = move(moves)

    # End of round
    DIRECTION_SEQUENCE = DIRECTION_SEQUENCE[1:] + DIRECTION_SEQUENCE[0]

    return grove


for turn in range(10):
    grove = do_turn(grove)

grove = trim(grove)
print(sum([row.count(EMPTY) for row in grove]))
