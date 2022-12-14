from typing import List

from dataclasses import dataclass


mod = 1


@dataclass
class Monkey:
    items: List[int]
    item_index: int = 0
    inspect_counter: int = 0
    operand: str = "+"
    coefficient: str = "old"
    test_value: int = 0
    throw_true: "Monkey" = None
    throw_false: "Monkey" = None

    def inspect(self, operand: str, coefficient: str):
        self.inspect_counter += 1
        item = self.items[self.item_index]

        if coefficient == "old":
            coefficient = item
        else:
            coefficient = int(coefficient)

        if operand == "+":
            return item + coefficient
        elif operand == "-":
            return item - coefficient
        elif operand == "*":
            return item * coefficient
        elif operand == "/":
            return item / coefficient

    def bored(self: int):
        self.items[self.item_index] //= 3

    def test(self: int):
        if self.items[self.item_index] % self.test_value == 0:
            self.throw(self.throw_true)
        else:
            self.throw(self.throw_false)

    def throw(self, monkey: "Monkey"):
        monkey.items.append(self.items[self.item_index])
        self.item_index += 1

    def clear(self):
        self.items = []
        self.item_index = 0

    def round(self):
        for item in self.items:
            self.items[self.item_index] = (
                self.inspect(self.operand, self.coefficient) % mod
            )
            # self.bored()
            self.test()
        self.clear()


def one():
    global mod

    with open("input.txt") as f:
        lines = [line for line in f]

    monkeys = []
    for i in range(len(lines)):
        if lines[i][:6] == "Monkey":
            monkeys.append(Monkey([]))
    monkey_index = 0
    for line in lines:
        line = line.strip()
        if line[:6] == "Monkey":
            monkey_index = int(line.strip().split(" ")[1][:-1])
        elif line.find("Starting items") != -1:
            monkeys[monkey_index].items = [
                int(item) for item in line.strip().split(":")[1].strip().split(",")
            ]
        elif line.find("Operation") != -1:
            operation = line.strip().split("old ")[1].strip().split(" ")
            monkeys[monkey_index].operand = operation[0].strip()
            monkeys[monkey_index].coefficient = operation[1].strip()
        elif line.find("Test") != -1:
            monkeys[monkey_index].test_value = int(
                line.strip().split("divisible by ")[1].strip()
            )
            mod *= monkeys[monkey_index].test_value
        elif line.find("true") != -1:
            monkeys[monkey_index].throw_true = monkeys[
                int(line.strip().split("to monkey ")[1].strip())
            ]
        elif line.find("false") != -1:
            monkeys[monkey_index].throw_false = monkeys[
                int(line.strip().split("to monkey ")[1].strip())
            ]

    for i in range(10000):
        print("Round", i, ":")
        for index, monkey in enumerate(monkeys):
            print("Start monkey", index, ":")
            # print(monkey.items)
            monkey.round()

    print(
        list(
            map(
                lambda monkey: monkey.inspect_counter,
                sorted(
                    monkeys, key=lambda monkey: monkey.inspect_counter, reverse=True
                ),
            )
        )
    )


if __name__ == "__main__":
    one()
