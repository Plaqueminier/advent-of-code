def one():

    with open("input.txt") as f:
        lines = [line for line in f]

    cycle = 1
    X = 1
    signal_strength = []

    for line in lines:
        command = line.strip().split(" ")
        if command[0] == "noop":
            cycle += 1
            if (cycle + 20) % 40 == 0:
                signal_strength.append(cycle * X)
        elif command[0] == "addx":
            cycle += 1
            if (cycle + 20) % 40 == 0:
                signal_strength.append(cycle * X)
            cycle += 1
            X += int(command[1])
            if (cycle + 20) % 40 == 0:
                signal_strength.append(cycle * X)

        print(cycle)
    print(sum(signal_strength))


def two():

    with open("input.txt") as f:
        lines = [line for line in f]

    cycle = 0
    X = 1
    sprites = "###......................................"
    res = [""]

    for line in lines:
        command = line.strip().split(" ")
        if command[0] == "noop":
            cycle += 1
            res[-1] += sprites[(cycle - 1)]
            if cycle == 40:
                sprites = "###......................................"
                res.append("")
                cycle = 0
        elif command[0] == "addx":
            cycle += 1
            res[-1] += sprites[(cycle - 1)]
            if cycle == 40:
                sprites = "###......................................"
                res.append("")
                cycle = 0
            cycle += 1
            res[-1] += sprites[(cycle - 1)]
            if cycle == 40:
                sprites = "###......................................"
                res.append("")
                cycle = 0
            X += int(command[1])
            sprites = "." * (X - 1) + "###" + "." * (40 - X - 2)

        print(cycle, res[-1], sprites)

    print()
    for sprite in res:
        print(sprite)


if __name__ == "__main__":
    one()
    two()
