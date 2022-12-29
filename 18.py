with open("input-18.txt", "r") as file:
    input_lines = [line.strip() for line in file.readlines()]

# # Example input:
# input_lines = [line.strip() for line in """
# 2,2,2
# 1,2,2
# 3,2,2
# 2,1,2
# 2,3,2
# 2,2,1
# 2,2,3
# 2,2,4
# 2,2,6
# 1,2,5
# 3,2,5
# 2,1,5
# 2,3,5
# """.splitlines()][1:]
# # Example answer = 58


def parse_input(lines):
    return [tuple(int(x) for x in line.split(",")) for line in lines]


def count_exposed_sides(cubes: list[tuple[int]]):
    exposed_sides = 0
    open_air = [(0,0,0)]
    i = 0
    max_xyz, min_xyz = [], []
    for d in range(3):
        max_xyz.append(max([cube[d] for cube in cubes]))
        min_xyz.append(min([cube[d] for cube in cubes]))

    while i < len(open_air):
        block = open_air[i]
        for d in range(len(block)):  # d = dimension
            for v in [1, -1]:
                temp_cube = list(block)
                temp_cube[d] += v
                temp_cube = tuple(temp_cube)
                if min_xyz[d] - 1 <= temp_cube[d] <= max_xyz[d] + 1:
                    if cubes.count(temp_cube):
                        exposed_sides += 1
                    elif not open_air.count(temp_cube):
                        open_air.append(temp_cube)
        i += 1
    return exposed_sides


cubes = parse_input(input_lines)
print(count_exposed_sides(cubes))
