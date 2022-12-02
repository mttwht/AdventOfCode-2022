with open("input-02.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# # Example input:
# lines = """A Y
# B X
# C Z
# """.splitlines()
# # Example answer = 15

shapeScores = {'A': 1, 'B': 2, 'C': 3,
               'X': 1, 'Y': 2, 'Z': 3}

def shapeScore(line):
    (u, i) = line.split()
    return shapeScores[i]

def outcomeScore(line):
    (u, i) = line.split()
    outcome = shapeScores[u] - shapeScores[i]
    if outcome == 0: # result = draw
        return 3
    elif outcome % 3 == 1: # result = loss
        return 0
    else: # 
        return 6

def roundScore(line):
    return shapeScore(line) + outcomeScore(line)

totalScore = 0
for line in lines:
    totalScore += roundScore(line)

print(totalScore)
