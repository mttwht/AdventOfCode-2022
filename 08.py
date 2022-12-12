with open("input-08.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# # Example input:
# lines = """30373
# 25512
# 65332
# 33549
# 35390
# """.splitlines()
# # Example answer = 8


tree_map = [[int(tree) for tree in line] for line in lines]

score_map = []
for row in range(1, len(tree_map) - 1):
    row_list = []
    for col in range(1, len(tree_map[row]) - 1):
        height = tree_map[row][col]

        n, e, s, w = 0, 0, 0, 0
        for h in [tree_map[x][col] for x in range(row-1, -1, -1)]:
            # visible to N
            n += 1
            if h >= height: break
        for h in [tree_map[row][x] for x in range(col+1, len(tree_map[row]))]:
            # visible to E
            e += 1
            if h >= height: break
        for h in [tree_map[x][col] for x in range(row+1, len(tree_map))]:
            # visible to S
            s += 1
            if h >= height: break
        for h in [tree_map[row][x] for x in range(col-1, -1, -1)]:
            # visible to W
            w += 1
            if h >= height: break
        row_list.append(n * e * s * w)
    score_map.append(row_list)

max_score = max([max(row) for row in score_map])
print(max_score)
