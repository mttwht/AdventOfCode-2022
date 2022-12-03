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


def halveLine(line):
    length = int(len(line) / 2)
    return line[:length], line[length:]


def getCommonItem(sack1, sack2, sack3):
    common = set(sack1).intersection(set(sack2)).intersection(set(sack3))
    return common.pop()


itempriorities = list(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
def getItemPriority(item):
    return itempriorities.index(item)


totalPriority = 0
for line in range(int(len(lines) / 3)):
    beginLine = line * 3
    commonItem = getCommonItem(lines[beginLine+0], lines[beginLine+1], lines[beginLine+2])
    priority = getItemPriority(commonItem)
    totalPriority += priority

print(totalPriority)
