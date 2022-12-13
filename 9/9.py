def add_tuple(a, b):
    return (a[0] + b[0], a[1] + b[1])


def tuple_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def one():

    with open("input.txt") as f:
        lines = [line for line in f]

    dir = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
    hPos = (0, 0)
    tPos = (0, 0)
    seen = set([(0, 0)])

    for line in lines:
        command = line.strip().split(" ")
        for i in range(int(command[1])):
            hPos = add_tuple(hPos, dir[command[0]])
            if (tPos[0] == hPos[0] or tPos[1] == hPos[1]) and tuple_distance(
                hPos, tPos
            ) == 2:
                tPos = add_tuple(tPos, dir[command[0]])
            elif tuple_distance(hPos, tPos) <= 2:
                continue
            else:
                new_dir = (
                    1 if tPos[0] < hPos[0] else -1,
                    1 if tPos[1] < hPos[1] else -1,
                )
                tPos = add_tuple(tPos, new_dir)
            seen.add(tPos)
    print(seen, len(seen))


def two():

    with open("input.txt") as f:
        lines = [line for line in f]

    dir = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
    hPos = (0, 0)
    tPos = [(0, 0) for i in range(9)]
    seen = set([(0, 0)])
    for line in lines:
        command = line.strip().split(" ")
        for i in range(int(command[1])):
            hPos = add_tuple(hPos, dir[command[0]])
            for i in range(len(tPos)):
                if i == 0:
                    head = hPos
                else:
                    head = tPos[i - 1]
                if (tPos[i][0] == head[0] or tPos[i][1] == head[1]) and tuple_distance(
                    head, tPos[i]
                ) == 2:
                    new_dir = (
                        0
                        if tPos[i][0] == head[0]
                        else 1
                        if tPos[i][0] < head[0]
                        else -1,
                        0
                        if tPos[i][1] == head[1]
                        else 1
                        if tPos[i][1] < head[1]
                        else -1,
                    )
                    tPos[i] = add_tuple(tPos[i], new_dir)
                elif tuple_distance(head, tPos[i]) <= 2:
                    continue
                else:
                    new_dir = (
                        1 if tPos[i][0] < head[0] else -1,
                        1 if tPos[i][1] < head[1] else -1,
                    )
                    tPos[i] = add_tuple(tPos[i], new_dir)
            seen.add(tPos[-1])
    print(seen, len(seen))


if __name__ == "__main__":
    one()
    two()
