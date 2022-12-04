with open("input-03.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]


# # Example input:
# lines = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw
# """.splitlines()


# Example answer = 157


def halve_line(line):
    """Split a line in half and return the two halves"""

    length = int(len(line) / 2)
    return line[:length], line[length:]


def get_common_item(sack1, sack2, sack3):
    """Find the single common item between three sacks"""

    common = set(sack1).intersection(set(sack2)).intersection(set(sack3))
    return common.pop()


itemPriorities = list(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")


def get_item_priority(item):
    """Get the priority score for an item"""

    return itemPriorities.index(item)


totalPriority = 0
for line in range(int(len(lines) / 3)):
    beginLine = line * 3
    commonItem = get_common_item(lines[beginLine + 0], lines[beginLine + 1], lines[beginLine + 2])
    priority = get_item_priority(commonItem)
    totalPriority += priority

print(totalPriority)
