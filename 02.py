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


def determineShape(line):
    (u, i) = line.split()
    shape = shapeScores[u]
    if i == 'X':
        shape -= 1
    elif i == 'Z':
        shape += 1
    shape %= 3
    return ['Z', 'X', 'Y'][shape]


def shapeScore(line):
    shape = determineShape(line)
    return shapeScores[shape]


def outcomeScore(line):
    (u, i) = line.split()
    return outcomeScores[i]


def roundScore(line):
    return shapeScore(line) + outcomeScore(line)


totalScore = 0
for line in lines:
    totalScore += roundScore(line)

print(totalScore)
