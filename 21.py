with open("input-21.txt", "r") as file:
    input_lines = [line.strip() for line in file.readlines()]


# # Example input:
# input_lines = [line.strip() for line in """
# root: pppw + sjmn
# dbpl: 5
# cczh: sllz + lgvd
# zczc: 2
# ptdq: humn - dvpt
# dvpt: 3
# lfqf: 4
# humn: 5
# ljgn: 2
# sjmn: drzm * dbpl
# sllz: 4
# pppw: cczh / lfqf
# lgvd: ljgn * ptdq
# drzm: hmdt - zczc
# hmdt: 32
# """.splitlines()][1:]
# # Example answer = 301


def parse_input(input_lines):
    monkeys = {}
    for line in input_lines:
        k, v = line.split(": ")
        monkeys[k] = v
    return monkeys


def get_monkey_value(monkeys: dict[str, str], monkey: str) -> int:
    val = monkeys[monkey].split()
    if len(val) == 1:
        return int(val[0])
    elif len(val) == 3:
        m1, op, m2 = val
        m1 = get_monkey_value(monkeys, m1)
        m2 = get_monkey_value(monkeys, m2)
        if op == "+":
            return m1 + m2
        if op == "-":
            return m1 - m2
        if op == "*":
            return m1 * m2
        if op == "/":
            return m1 / m2


def get_human_value(monkeys: dict[str, str], root_monkey: str) -> int:
    lower, upper = 1, 1
    m1, _, m2 = monkeys[root_monkey].split()
    finding_upper = True
    monkey_diff = None
    while finding_upper:
        diff = get_monkey_value(monkeys, m1) - get_monkey_value(monkeys, m2)
        if not monkey_diff or (diff >= 0) == (monkey_diff >= 0):
            monkey_diff = diff
            lower, upper = upper, upper * 2
            monkeys["humn"] = str(upper)
            finding_upper = True
        else:
            finding_upper = False
    while lower < upper:
        mid = int(lower + (upper - lower) / 2)
        monkeys["humn"] = str(mid)
        diff = get_monkey_value(monkeys, m1) - get_monkey_value(monkeys, m2)
        if diff == 0:
            return mid
        elif (diff >= 0) == (monkey_diff >= 0):
            lower = mid
        else:
            upper = mid


monkeys = parse_input(input_lines)
humn_val = get_human_value(monkeys, "root")
print(humn_val)
