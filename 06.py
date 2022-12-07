with open("input-06.txt", "r") as file:
    line = file.readline().strip()


# Example input:
# line = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"  # Example answer = 19
# line = "bvwbjplbgvbhsrlpgdmjqwftvncz"  # Example answer = 23
# line = "nppdvjthqldpwncqszvftbrmjlhg"  # Example answer = 23
# line = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"  # Example answer = 29
# line = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"  # Example answer = 26


def index_after_marker(datastream, marker_length):
    """Finds the index of the character after the first marker"""

    for i in range(len(datastream) - marker_length):
        if (len(set(datastream[i:i + marker_length]))) == marker_length:
            return i + marker_length


print(index_after_marker(line, 14))
