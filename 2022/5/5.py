def create_stacks(lines):
    stacks = [[] for i in range((len(lines[0]) + 1) // 4)]
    for line in lines:
        if line[1] == "1":
            for stack in stacks:
                stack.reverse()
            lines = lines[lines.index(line) + 2 :]
            break
        for i, index in enumerate(range(1, len(line), 4)):
            stacks[i].append(line[index]) if line[index] != " " else None
    return stacks, lines


def create_commands(lines):
    commands = [
        (
            int(line.split("move ")[1][: line.split("move ")[1].find(" ")]),
            int(line.split(" from ")[1][: line.split(" from ")[1].find(" ")]) - 1,
            int(line.strip().split(" to ")[1]) - 1,
        )
        for line in lines
    ]
    return commands


def move_crates_one(stacks, command):
    for i in range(command[0]):
        move = stacks[command[1]].pop()
        stacks[command[2]].append(move)
    return stacks


def one():

    with open("input.txt") as f:
        lines = [line for line in f]

    stacks, lines = create_stacks(lines)
    commands = create_commands(lines)
    for command in commands:
        move_crates_one(stacks, command)
    for stack in stacks:
        print(stack[-1], end="")
    print()


def move_crates_two(stacks, command):
    moves = []
    for i in range(command[0]):
        move = stacks[command[1]].pop()
        moves.append(move)
    moves.reverse()
    for move in moves:
        stacks[command[2]].append(move)
    return stacks


def two():

    with open("input.txt") as f:
        lines = [line for line in f]

    stacks, lines = create_stacks(lines)
    commands = create_commands(lines)
    for command in commands:
        move_crates_two(stacks, command)
    for stack in stacks:
        print(stack[-1], end="")
    print()


if __name__ == "__main__":
    one()
    two()
