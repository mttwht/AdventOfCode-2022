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


def getCommonItem(comp1, comp2):
    common = set(comp1).intersection(set(comp2))
    return common.pop()


itempriorities = list(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
def getItemPriority(item):
    return itempriorities.index(item)


totalPriority = 0
for line in lines:
    (begin, end) = halveLine(line)
    commonItem = getCommonItem(begin, end)
    priority = getItemPriority(commonItem)
    totalPriority += priority

print(totalPriority)
