with open("input-06.txt", "r") as file:
    line = file.readline().strip()


# Example input:
# line = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"  # Example answer = 7
# line = "bvwbjplbgvbhsrlpgdmjqwftvncz"  # Example answer = 5
# line = "nppdvjthqldpwncqszvftbrmjlhg"  # Example answer = 6
# line = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"  # Example answer = 10
# line = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"  # Example answer = 11


def index_after_sop_marker(datastream):
    """Finds the index of the character after the first start-of-packet marker"""

    for i in range(len(datastream) - 4):
        if (len(set(datastream[i:i + 4]))) == 4:
            return i + 4


print(index_after_sop_marker(line))
