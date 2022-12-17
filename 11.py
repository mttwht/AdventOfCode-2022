with open("input-11.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# # Example input:
# lines = """Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0

# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3

# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1
# """.splitlines()
# # Example answer = 13140


def apply_relief(item: int) -> int:
    return int(item / 3)


class Monkey:

    def __init__(self, definition: list[str]) -> None:
        self.false = int(definition.pop().split()[-1])
        self.true = int(definition.pop().split()[-1])
        self.test_val = int(definition.pop().split()[-1])
        self.op = definition.pop().split()[-2:]
        self.items = [int(v)
                      for v in definition.pop().split(":")[-1].split(",")]
        self.inspections = 0

    def __str__(self) -> str:
        return ", ".join([str(item) for item in self.items])

    def inspect(self, item: int) -> int:
        if self.op[0] == '+':
            return item + int(self.op[1])
        elif self.op[0] == '*':
            if self.op[1] == "old":
                return item * item
            return item * int(self.op[1])

    def inspect_item(self) -> int:
        if self.items:
            self.inspections += 1
            item = self.items.pop(0)
            item = self.inspect(item)
            item = apply_relief(item)
            return item

    def who_to_throw_to(self, item: int) -> int:
        if item % self.test_val == 0:
            return self.true
        return self.false


def parse_monkeys(lines: list[str]) -> list[Monkey]:
    monkeys = list()
    for i in range(0, len(lines), 7):
        monkeys.append(Monkey(lines[i:i+6]))
    return monkeys


def print_monkey(index: int, monkey: Monkey) -> None:
    print("Monkey", index, ":", monkey)


def print_monkeys(monkeys: list[Monkey]) -> None:
    for monkey in monkeys:
        print_monkey(monkeys.index(monkey), monkey)


def monkey_business_level(monkeys: list[Monkey]) -> int:
    total_inspections = [m.inspections for m in monkeys]
    cheeky_monkeys = sorted(total_inspections)[-2:]
    return cheeky_monkeys[0] * cheeky_monkeys[1]


monkeys = parse_monkeys(lines)

print(0)
print_monkeys(monkeys)

for i in range(20):
    for monkey in monkeys:
        while monkey.items:
            item = monkey.inspect_item()
            m2 = monkey.who_to_throw_to(item)
            monkeys[m2].items.append(item)
    print(i + 1)
    print_monkeys(monkeys)

print(monkey_business_level(monkeys))
