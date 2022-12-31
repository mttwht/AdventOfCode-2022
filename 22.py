import re

with open("input-22.txt", "r") as file:
    input_lines = [line.rstrip() for line in file.readlines()]

# # Example input:
# input_lines = [line.rstrip() for line in """
#         ...#
#         .#..
#         #...
#         ....
# ...#.......#
# ........#...
# ..#....#....
# ..........#.
#         ...#....
#         .....#..
#         .#......
#         ......#.
#
# 10R5L5R10L4R5L5
# """.splitlines()][1:]
# # Example answer = 6032

RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
NOTHING, TILE, WALL = " ", ".", "#"


def parse_input(lines: list[str]) -> tuple[list[str], list]:
    board = lines[:-2]
    width = max([len(row) for row in board])
    board = [row.ljust(width) for row in board]

    instructions = []
    instructions_line = lines[-1]
    while instructions_line:
        if instructions_line[0].isnumeric():
            match = re.match("^(\d+)", instructions_line)
            num = match.groups()[0]
            instructions.append(int(num))
            instructions_line = instructions_line[len(num):]
        else:
            instructions.append(instructions_line[0])
            instructions_line = instructions_line[1:]
    return board, instructions


def cell_in_front(board, position):
    (row, col), ori = position
    if ori == RIGHT:
        r, c = row, (col + 1) % len(board[row])
    elif ori == DOWN:
        r, c = (row + 1) % len(board), col
    elif ori == LEFT:
        r, c = row, (col - 1) % len(board[row])
    elif ori == UP:
        r, c = (row - 1) % len(board), col
    return (r, c), board[r][c]


def step(board, position):
    _, ori = position
    (row, col), cell_type = cell_in_front(board, position)
    while cell_type == NOTHING:
        (row, col), cell_type = cell_in_front(board, ((row, col), ori))
    if cell_type == TILE:
        return row, col
    elif cell_type == WALL:
        return position[0]


def walk(board, position, instruction):
    (row, col), ori = position
    for i in range(instruction):
        (row, col) = step(board, ((row, col), ori))
    return (row, col), ori


def turn(position, instruction):
    pos, ori = position
    if instruction == "L":
        ori = (ori - 1) % 4
    elif instruction == "R":
        ori = (ori + 1) % 4
    return pos, ori


def move(board, position, instruction):
    if type(instruction) is int:
        position = walk(board, position, instruction)
    else:
        position = turn(position, instruction)
    return position


def get_score(pos):
    (row, column), orientation = pos
    return (row + 1) * 1000 + (column + 1) * 4 + orientation


board, instructions = parse_input(input_lines)
position = ((0, board[0].index(".")), RIGHT)

for instruction in instructions:
    position = move(board, position, instruction)

print(get_score(position))
