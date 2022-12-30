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
# # Example answer = 152


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
            return int(m1 / m2)


monkeys = parse_input(input_lines)
print(get_monkey_value(monkeys, "root"))
