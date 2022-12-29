import copy

with open("input-20.txt", "r") as file:
    input_lines = [line.strip() for line in file.readlines()]

# # # Example input:
# input_lines = [line.strip() for line in """
# 1
# 2
# -3
# 3
# -2
# 0
# 4
# """.splitlines()][1:]

# # Example answer = 3


def parse_input(lines):
    numbers = []
    for i in range(len(lines)):
        numbers.append((int(lines[i]), i))
    return numbers


numbers = parse_input(input_lines)
original_numbers = copy.deepcopy(numbers)

for number in original_numbers:
    current_index = numbers.index(number)
    new_index = (current_index + number[0])
    numbers.remove(number)
    if new_index == 0:
        numbers.append(number)
    else:
        numbers.insert(new_index % len(numbers), number)
    # print(number, [n[0] for n in numbers])

for i in range(len(numbers)):
    if numbers[i][0] == 0:
        zero_index = i
        break
coords = [numbers[(zero_index + i) % len(numbers)][0] for i in [1000, 2000, 3000]]
print(sum(coords), coords)
