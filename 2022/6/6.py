def level(limit):

    with open("input.txt") as f:
        lines = [line for line in f]

    for line in lines:
        cursor = []
        for index, letter in enumerate(line):
            cursor.append(letter)
            if len(cursor) > limit:
                cursor.pop(0)
            seen = set(cursor)
            if len(seen) == limit:
                print(index + 1)
                break


if __name__ == "__main__":
    level(4)
    level(14)
