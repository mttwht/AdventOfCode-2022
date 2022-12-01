with open("input-01.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# # Example input:
# lines = """1000
# 2000
# 3000

# 4000

# 5000
# 6000

# 7000
# 8000
# 9000

# 10000
# """.splitlines()
# # Example answer = 24000

def parse(lines):
    elves = list()
    elf = 0
    for i in range(len(lines)):
        line = lines[i]
        if line != "":
            elf += int(line)
        else:
            elves.append(elf)
            elf = 0
    elves.append(elf)
    return elves

elves = parse(lines)

top3 = list(reversed(sorted(elves)))[:3]

print(sum(top3))
