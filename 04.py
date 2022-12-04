with open("input-04.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# # Example input:
# lines = """2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8
# """.splitlines()


# Example answer = 2


def parseLine(line):
    sections = [sections.split("-") for sections in line.split(",")]
    sections = [list(range(int(s[0]), int(s[1])+1)) for s in sections]
    return sections[0], sections[1]


def fullyContains(a1: list, a2: list):
    overlap = set(a1).intersection(set(a2))
    if len(overlap) == len(a1) or len(overlap) == len(a2):
        return True
    return False


def contains(a1, a2):
    overlap = set(a1).intersection(set(a2))
    if len(overlap) > 0:
        return True
    return False


overlaps = 0
for line in lines:
    (area1, area2) = parseLine(line)
    if contains(area1, area2):
        overlaps += 1


print(overlaps)
