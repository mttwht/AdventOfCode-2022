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


# Example answer = 13


def parse_line(line: str) -> list:
    return json.loads(line)


def parse_input(input: list[str]) -> list[tuple[list, list]]:
    pairs = list()
    for i in range(0, len(input), 3):
        l, r = parse_line(input[i]), parse_line(input[i + 1])
        pairs.append((l, r))
    return pairs


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


pairs = parse_input(lines)
ordered_pairs = []
for i in range(len(pairs)):
    left, right = pairs[i]
    if is_ordered(left, right) != False:
        ordered_pairs.append(i + 1)

print(ordered_pairs)
print(sum(ordered_pairs))
