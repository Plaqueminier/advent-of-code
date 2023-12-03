def one():

    with open("input.txt") as f:
        pairs = [
            (
                [int(nb) for nb in pair[0].split("-")],
                [int(nb) for nb in pair[1].split("-")],
            )
            for pair in [line.strip().split(",") for line in f]
        ]
        containment = 0
        for pair in pairs:
            narrowest, widest = (
                (pair[1], pair[0])
                if pair[0][1] - pair[0][0] > pair[1][1] - pair[1][0]
                else (pair[0], pair[1])
            )
            if widest[0] <= narrowest[0] <= narrowest[1] <= widest[1]:
                containment += 1
        print(containment)


def two():

    with open("input.txt") as f:
        pairs = [
            (
                [int(nb) for nb in pair[0].split("-")],
                [int(nb) for nb in pair[1].split("-")],
            )
            for pair in [line.strip().split(",") for line in f]
        ]
        overlap = 0
        for pair in pairs:
            lowest, highest = (
                (pair[1], pair[0]) if pair[0][1] > pair[1][0] else (pair[0], pair[1])
            )
            if not (lowest[0] <= lowest[1] < highest[0] <= highest[1]):
                overlap += 1
        print(overlap)


if __name__ == "__main__":
    one()
    two()
