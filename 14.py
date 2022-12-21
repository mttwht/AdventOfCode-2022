with open("input-14.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

EMPTY_SPACE = 0
ROCK = 1
SAND = 2

# # Example input:
# lines = """498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9
# """.splitlines()
# # Example answer = 93


def parse_paths(input: list[str]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    paths = []
    for line in input:
        points = line.split(" -> ")
        points = [p.split(",") for p in points]
        points = [(int(a), int(b)) for a, b in points]
        for i in range(len(points) - 1):
            paths.append((points[i], points[i+1]))
    return paths


def draw_line(slice_map, endpoints, material):
    ((x1, y1), (x2, y2)) = endpoints



def make_map(paths):
    max_x = max([point[0] for path in paths for point in path])
    max_y = max([point[1] for path in paths for point in path])
    slice_map = [[EMPTY_SPACE for y in range(max_y + 1)] for x in range(max_x + 1)]
    for i in range(len(paths)):
        ((x1, y1), (x2, y2)) = paths[i]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                slice_map[x1][y] = ROCK
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                slice_map[x][y1] = ROCK
    for x in range(len(slice_map)):
        slice_map[x] += [EMPTY_SPACE, ROCK]
    return slice_map


def drop_sand(slice_map):
    (x, y) = (500, 0)
    falling = True
    while falling:
        if x + 1 >= len(slice_map):
            new_col = [EMPTY_SPACE for _ in range(len(slice_map[0]))]
            new_col[-1] = ROCK
            slice_map.append(new_col)

        if slice_map[x][y + 1] == EMPTY_SPACE:
            (x, y) = (x, y+1)
        elif slice_map[x-1][y+1] == EMPTY_SPACE:
            (x, y) = (x-1, y+1)
        elif slice_map[x+1][y+1] == EMPTY_SPACE:
            (x, y) = (x+1, y+1)
        elif y == 0 and slice_map[x][y] != EMPTY_SPACE:
            return None
        else:
            return (x, y)


paths = parse_paths(lines)
slice_map = make_map(paths)

grain_count = 0
grain = drop_sand(slice_map)
while grain:
    (x, y) = grain
    slice_map[x][y] = SAND
    grain_count += 1
    grain = drop_sand(slice_map)

print(grain_count)
