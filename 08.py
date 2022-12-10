with open("input-08.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# # Example input:
# lines = """30373
# 25512
# 65332
# 33549
# 35390
# """.splitlines()
# # Example answer = 21


tree_map = [[int(tree) for tree in line] for line in lines]

visible_trees = (len(tree_map) - 1) * 4
for row in range(1, len(tree_map) - 1):
    for col in range(1, len(tree_map[row]) - 1):
        height = tree_map[row][col]
        if height > max([tree_map[x][col] for x in range(row)]):
            # visible from N
            visible_trees += 1
            continue
        elif height > max([tree_map[row][x] for x in range(col + 1, len(tree_map[row]))]):
            # visible from E
            visible_trees += 1
            continue
        elif height > max([tree_map[x][col] for x in range(row + 1, len(tree_map))]):
            # visible from S
            visible_trees += 1
            continue
        elif height > max([tree_map[row][x] for x in range(col)]):
            # visible from W
            visible_trees += 1
            continue

print(visible_trees)
