import re

with open("input-05.txt", "r") as file:
    lines = [line.strip("\n") for line in file.readlines()]


# # Example input:
# lines = """    [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
#
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# """.splitlines()
# Example answer = 'CMZ'


def parse_stacks(lines):
    """Parse input lines into a list of crate stacks"""

    stacks = list()
    for line in lines:
        crates = [line[i:i + 4] for i in range(0, len(line), 4)]
        stacks.append(crates)
    crateStacks = list()
    for s in range(len(stacks.pop())): crateStacks.append(list())

    while len(stacks):
        row = stacks.pop()
        for i in range(len(row)):
            cell = row[i]
            if cell.startswith('['):
                crateStacks[i].append(cell[1])

    return crateStacks


def print_stacks(stacks: dict):
    """Print out all stacks visually"""

    height = max([len(a) for a in stacks])
    for h in range(height - 1, 0 - 1, -1, ):
        for s in range(0, len(stacks)):
            if h < len(stacks[s]):
                print("[" + stacks[s][h] + "]", end=" ")
            else:
                print("   ", end=" ")
        print()
    for i in range(len(stacks)):
        print(" " + str(i + 1) + " ", end=" ")
    print()


def print_tops(stacks):
    """Print the top item of each stack"""

    for stack in stacks:
        print(stack[len(stack) - 1], end="")
    print()


sectionLength = lines.index('')

stacks = parse_stacks(lines[:sectionLength])
print_stacks(stacks)

p = re.compile("^move (\d+) from (\d+) to (\d+)")
for line in lines[sectionLength + 1:]:
    (move_count, move_from, move_to) = p.match(line).groups()
    (move_from_i, move_to_i) = (int(move_from) - 1, int(move_to) - 1)
    moving_crates = list()
    for i in range(int(move_count)):
        moving_crates.append(stacks[move_from_i].pop())
    stacks[move_to_i] += reversed(moving_crates)

print_stacks(stacks)
print()
print_tops(stacks)
