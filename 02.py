with open("input-02.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# # Example input:
# lines = """A Y
# B X
# C Z
# """.splitlines()
# # Example answer = 15

shapeScores = {'A': 1, 'B': 2, 'C': 3,
               'X': 1, 'Y': 2, 'Z': 3}  # relevant to part 1 only

outcomeScores = {'X': 0, 'Y': 3, 'Z': 6}


def determine_shape(line):
    """Determine the shape the player is to play"""

    (u, i) = line.split() # u & i = You & I
    shape = shapeScores[u]
    if i == 'X':
        shape -= 1
    elif i == 'Z':
        shape += 1
    shape %= 3
    return ['Z', 'X', 'Y'][shape]


def shape_score(line):
    """Calculate the players score for the shape played"""

    shape = determine_shape(line)
    return shapeScores[shape]


def outcome_score(line):
    """Calculate the players score for an outcome"""

    (u, i) = line.split() # u & i = You & I
    return outcomeScores[i]


def round_score(line):
    """Calculate the score for a single round"""

    return shape_score(line) + outcome_score(line)


totalScore = 0
for line in lines:
    totalScore += round_score(line)

print(totalScore)
