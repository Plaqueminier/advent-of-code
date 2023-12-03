def compare_package(left, right):
    print("1 -----")
    print(left, right)
    print("2 -----")
    if type(left) == int and type(right) == int:
        return 1 if left < right else 0 if left == right else -1
    if type(left) == int and type(right) == list:
        left = [left]
    if type(right) == int and type(left) == list:
        right = [right]
    if left == [] and right == []:
        return 0
    if not len(left) and len(right):
        return 1
    if not len(right) and len(left):
        return -1
    if left[0] != right[0]:
        comparison = compare_package(left[0], right[0])
        if comparison != 0:
            return comparison
    return compare_package(left[1:], right[1:])


def one():

    with open("input.txt") as f:
        lines = [line.strip() for line in f]

    sum = 0
    for i in range(0, len(lines), 3):
        left = eval(lines[i])
        right = eval(lines[i + 1])
        if compare_package(left, right) == 1:
            sum += (i // 3) + 1
    print(sum)


def two():

    with open("input.txt") as f:
        lines = [line.strip() for line in f]

    sum = 0
    packets = [[[2]], [[6]]]
    for i in range(0, len(lines), 3):
        left = eval(lines[i])
        right = eval(lines[i + 1])
        packets.append(left)
        packets.append(right)

    for i in range(len(packets)):
        for j in range(0, len(packets) - 1, 1):
            if compare_package(packets[j], packets[j + 1]) == -1:
                packets[j], packets[j + 1] = packets[j + 1], packets[j]
    print(packets)
    print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))


if __name__ == "__main__":
    two()
