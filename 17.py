import copy

with open("input-17.txt", "r") as file:
    line = file.readline().strip()

# Example input:
# line = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
# Example answer = 1514285714288


EMPTY, FALLING, STOPPED = 0, 1, 2
shapes = [
    [  # h-line
        [0, 0, 1, 1, 1, 1, 0],  # ..####.
    ],
    [  # plus
        [0, 0, 0, 1, 0, 0, 0],  # ...#...
        [0, 0, 1, 1, 1, 0, 0],  # ..###..
        [0, 0, 0, 1, 0, 0, 0],  # ...#...
    ],
    [  # corner
        [0, 0, 0, 0, 1, 0, 0],  # ....#..
        [0, 0, 0, 0, 1, 0, 0],  # ....#..
        [0, 0, 1, 1, 1, 0, 0],  # ..###..
    ],
    [  # v-line
        [0, 0, 1, 0, 0, 0, 0],  # ..#....
        [0, 0, 1, 0, 0, 0, 0],  # ..#....
        [0, 0, 1, 0, 0, 0, 0],  # ..#....
        [0, 0, 1, 0, 0, 0, 0],  # ..#....
    ],
    [  # square
        [0, 0, 1, 1, 0, 0, 0],  # ..##...
        [0, 0, 1, 1, 0, 0, 0],  # ..##...
    ]
]


def print_chamber(chamber):
    for i in range(1, len(chamber) + 1):
        display_line = ""
        line = chamber[-i]
        for c in line:
            if c == EMPTY:
                display_line += " . "
            elif c == FALLING:
                display_line += " @ "
            elif c == STOPPED:
                display_line += " # "
        print("|", display_line, "|")
    print("|", "---" * 7, "|")


def drop_rock(chamber: list[list[int]], rock, jet_pattern, next_jet_index):
    while len(chamber) > 3 and not chamber[-4].count(STOPPED):
        chamber.pop()
    while chamber[-3].count(STOPPED):
        chamber += [[EMPTY] * 7]
    for i in range(len(rock)):
        chamber += [[EMPTY] * 7]

    rock = list(reversed(rock))
    rock_y = len(chamber) - 1
    while not any([row.count(FALLING + STOPPED) for row in chamber[rock_y - len(rock):rock_y + 1]]):
        # process effects of gas jets
        jet_direction = jet_pattern[next_jet_index % len(jet_pattern)]
        next_jet_index += 1
        temp_rock = copy.deepcopy(rock)
        # do not move through chamber walls
        if jet_direction == "<":
            if sum([row[0] for row in temp_rock]) == 0:
                temp_rock = [row[1:] + row[:1] for row in temp_rock]
        elif jet_direction == ">":
            if sum([row[-1] for row in temp_rock]) == 0:
                temp_rock = [row[-1:] + row[:-1] for row in temp_rock]
        # do not move through stopped rocks
        temp_rows = chamber[rock_y - len(temp_rock) + 1:rock_y + 1]
        if not any([True for row in range(len(temp_rock)) for col in range(len(temp_rock[row])) if
                    temp_rock[row][col] and temp_rows[row][col]]):
            rock = temp_rock
        else:
            temp_rock = rock

        rock_y -= 1
        temp_rows = chamber[rock_y - len(temp_rock) + 1:rock_y + 1]
        if rock_y - len(rock) + 1 < 0 or any(
                [True for row in range(len(temp_rock)) for col in range(len(temp_rock[row])) if
                 temp_rock[row][col] and temp_rows[row][col]]):
            rock_y += 1
            break

    for row in range(len(rock)):
        chamber[rock_y - row] = [chamber[rock_y - row][i] + (rock[-(row + 1)][i] * 2) for i in
                                 range(len(rock[-(row + 1)]))]

    return chamber, next_jet_index


def find_repeating_pattern(sequence):
    start_point = int(len(chamber_len_changes) / 2)
    while chamber_len_changes[start_point:-3].count(chamber_len_changes[-1]):
        c = chamber_len_changes[start_point:-3].index(chamber_len_changes[-1]) + start_point
        pattern_len = len(chamber_len_changes) - c - 1
        a1 = chamber_len_changes[c + 1:]
        a2 = chamber_len_changes[c + 1 - pattern_len: c + 1]
        if a1 == a2:
            return a1
        else:
            start_point = c + 1
    return None


chamber = [[EMPTY] * 7] * 3
chamber_len = 0
next_jet_index = 0
chamber_len_changes = []
skipped_lines = 0
rock_no = 0
while rock_no < 1000000000000:
    # for rock_no in range(3 * 5 * len(line)):
    chamber, next_jet_index = drop_rock(chamber, shapes[rock_no % len(shapes)], line, next_jet_index)
    if rock_no % len(shapes) == len(shapes) - 1:
        while not chamber[-1].count(STOPPED):
            chamber.pop()
        chamber_len_changes.append(len(chamber) - chamber_len)
        chamber_len = len(chamber)

        if not skipped_lines:
            pattern = find_repeating_pattern(chamber_len_changes)
            if pattern:
                repeats_needed = int((1000000000000 - (rock_no + 1)) / (len(pattern) * 5))
                rock_no += repeats_needed * len(pattern) * 5
                pattern_height = sum(pattern)
                skipped_lines = repeats_needed * pattern_height
    rock_no += 1

while not chamber[-1].count(STOPPED):
    chamber.pop()

# print_chamber(chamber)
print(len(chamber) + skipped_lines)
