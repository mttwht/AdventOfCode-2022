import copy

import regex as re

with open("input-16.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]


# # Example input:
# lines = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
# Valve CC has flow rate=2; tunnels lead to valves DD, BB
# Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
# Valve EE has flow rate=3; tunnels lead to valves FF, DD
# Valve FF has flow rate=0; tunnels lead to valves EE, GG
# Valve GG has flow rate=0; tunnels lead to valves FF, HH
# Valve HH has flow rate=22; tunnel leads to valve GG
# Valve II has flow rate=0; tunnels lead to valves AA, JJ
# Valve JJ has flow rate=21; tunnel leads to valve II
# """.splitlines()


# Example answer = 1651


class Valve:
    def __init__(self, name: str, flow_rate: str | int, tunnels: list[str]):
        self.name = name
        self.flow_rate = int(flow_rate)
        self.tunnels = tunnels
        self.open = False


def parse_line(line):
    match = re.search("Valve (\w+) has flow rate=(\d+); tunnel[s]? lead[s]? to valve[s]? (.+)", line)
    if match:
        name, rate, conn = match.groups()
        conn = conn.split(", ")
        return Valve(name, rate, conn)


def parse_input(lines):
    valves = {}
    for line in lines:
        valve = parse_line(line)
        if valve:
            valves[valve.name] = valve
    return valves


def calculate_distances(valves, start_point):
    dists = {}
    nexts = [(start_point, 0)]
    while nexts:
        (v, d) = nexts.pop(0)
        if dists.get(v) is not None:
            continue
        dists[v] = d
        for t in valves[v].tunnels:
            if dists.get(t) is not None or len(list(filter(lambda x: x[0] == t, nexts))):
                continue
            nexts.append((t, d + 1))
    return dists


def get_move_values(valves, pos, time_remaining):
    distances = calculate_distances(valves, pos)
    values = {v: valves[v].flow_rate * (time_remaining - distances[v] - 1)
              for v in valves
              if not valves[v].open and valves[v].flow_rate > 0}
    values = {k: v for (k, v) in values.items() if v > 0}
    return values


def find_max_release(valves, pos, time_remaining):
    if time_remaining <= 1:
        return 0
    distances = calculate_distances(valves, pos)
    values = get_move_values(valves, pos, time_remaining)
    max_release = 0
    for v in values:
        temp_valves = copy.deepcopy(valves)
        temp_valves[v].open = True
        max_release = max(max_release, values[v] + find_max_release(temp_valves, v, time_remaining - distances[v] - 1))
    return max_release


valves = parse_input(lines)

score = find_max_release(valves, "AA", 30)
print(score)
