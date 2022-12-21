import regex as re

with open("input-15.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
target_row = 2000000

# # Example input:
# lines = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3
# """.splitlines()
# target_row = 10


# Example answer = 26 for row y=10


def parse_line(line: str) -> tuple[tuple[int, int], tuple[int, int]]:
    match = re.search("x=(-?\d+), y=(-?\d+).+x=(-?\d+), y=(-?\d+)", line)
    if match:
        sx, sy, bx, by = match.groups()
        return (int(sx), int(sy)), (int(bx), int(by))


def manhattan_distance(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    (x1, y1), (x2, y2) = p1, p2
    return abs(x1 - x2) + abs(y1 - y2)


pairs = []

for line in lines:
    sensor, beacon = parse_line(line)
    pairs.append((sensor, beacon))

coverage = set()
for sensor, beacon in pairs:
    m_dist = manhattan_distance(sensor, beacon)
    sx, sy = sensor
    if sy + m_dist >= target_row >= sy - m_dist:
        for i in range(m_dist - abs(sy - target_row) + 1):
            coverage.add(sx + i)
            coverage.add(sx - i)

coverage = coverage.difference([bx for _, (bx, by) in pairs if by == target_row])

print(len(coverage))
