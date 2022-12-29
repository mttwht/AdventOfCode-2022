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
# # Example answer = 64


def parse_input(lines):
    return [tuple(int(x) for x in line.split(",")) for line in lines]


def count_exposed_sides(cubes: list[tuple[int]]):
    exposed_sides = 0
    for cube in cubes:
        for d in range(len(cube)):  # d = dimension
            for v in [1, -1]:
                temp_cube = list(cube)
                temp_cube[d] += v
                temp_cube = tuple(temp_cube)
                if not cubes.count(temp_cube):
                    exposed_sides += 1
    return exposed_sides


cubes = parse_input(input_lines)
print(count_exposed_sides(cubes))
