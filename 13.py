import json

with open("input-13.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# # Example input:
# lines = """[1,1,3,1,1]
# [1,1,5,1,1]
#
# [[1],[2,3,4]]
# [[1],4]
#
# [9]
# [[8,7,6]]
#
# [[4,4],4,4]
# [[4,4],4,4,4]
#
# [7,7,7,7]
# [7,7,7]
#
# []
# [3]
#
# [[[]]]
# [[]]
#
# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]
# """.splitlines()


# Example answer = 140


def parse_line(line: str) -> list:
    return json.loads(line)


def parse_input(input: list[str]) -> list[list]:
    return [parse_line(line) for line in input if line]
    packets = list()
    for line in input:
        if line:
            packets.append(parse_line(line))
    return packets


def is_ordered(left: list, right: list) -> bool|None:
    for i in range(len(left)):
        if i >= len(right):
            return False
        l, r = left[i], right[i]
        if type(l) == int and type(r) == int:
            if l != r:
                return l < r
        else:
            if type(l) == int:
                l = [l, ]
            if type(r) == int:
                r = [r, ]
            result = is_ordered(l, r)
            if result is not None:
                return result
    if len(left) < len(right):
        return True


packets = parse_input(lines)
dividers = [json.loads("[[2]]"), json.loads("[[6]]")]

groups = [[], [], []]

for packet in packets:
    if is_ordered(packet, dividers[0]):
        groups[0].append(packet)
    elif is_ordered(packet, dividers[1]):
        groups[1].append(packet)
    else:
        groups[2].append(packet)

print((len(groups[0]) + 1) * (len(groups[0]) + len(groups[1]) + 2))
