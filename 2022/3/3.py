def one():

    with open("input.txt") as f:
        priorities = []
        rucksacks = [line.strip() for line in f]
        for rucksack in rucksacks:
            middle = int(len(rucksack) / 2)
            rucksack1, rucksack2 = rucksack[middle:], rucksack[:middle]
            for item in rucksack1:
                if item in rucksack2:
                    priorities.append(
                        ord(item) - 64 + 26 if ord(item) < 97 else ord(item) - 96
                    )
                    break
        print(sum(priorities))


def two():
    with open("input.txt") as f:
        priorities = []
        rucksacks = [line.strip() for line in f]
        for i in range(0, len(rucksacks), 3):
            rucksack1, rucksack2, rucksack3 = (
                rucksacks[i],
                rucksacks[i + 1],
                rucksacks[i + 2],
            )
            print(rucksack1, rucksack2, rucksack3)
            for item in rucksack1:
                if item in rucksack2 and item in rucksack3:
                    priorities.append(
                        ord(item) - 64 + 26 if ord(item) < 97 else ord(item) - 96
                    )
                    break
        print(sum(priorities))


if __name__ == "__main__":
    one()
    two()
