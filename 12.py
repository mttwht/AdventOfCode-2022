with open("input-12.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]


# # Example input:
# lines = """Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi
# """.splitlines()
# # Example answer = 31


def parse_input(input: list[str]) -> list[list[int]]:
    return [[ord(c) for c in line.replace("S", "a").replace("E", "z")] for line in input]


def find_char(input: list[str], char: str) -> tuple[int, int]:
    for line in lines:
        if line.count(char):
            return line.index(char), input.index(line)


def find_end(input: list[str]) -> tuple[int, int]:
    return find_char(input, "E")


def find_start(input: list[str]) -> tuple[int, int]:
    return find_char(input, "S")


def find_shortest_paths(map: list[list[int]], start: tuple[int, int]) -> list[list[int]]:
    distances = [[None for x in range(len(map[y]))] for y in range(len(map))]

    distances[start[1]][start[0]] = 0
    next_check = [start]

    while next_check:
        x, y = next_check.pop(0)
        height = map[y][x]
        for (x2, y2) in [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]:
            # N, S, E, W
            if x2 < 0 or y2 < 0 or y2 >= len(map) or x2 >= len(map[y2]):
                # out of bounds
                continue
            elif distances[y2][x2]:
                # already calculated
                continue
            elif map[y2][x2] > height + 1:
                # too high
                continue
            else:
                distances[y2][x2] = distances[y][x] + 1
                next_check.append((x2, y2))

    return distances


map = parse_input(lines)
start, end = find_start(lines), find_end(lines)
distances = find_shortest_paths(map, start)

print(distances)
print(distances[end[1]][end[0]])
