def main():
    guide = {
        "A": {"X": 4, "Y": 8, "Z": 3},
        "B": {"X": 1, "Y": 5, "Z": 9},
        "C": {"X": 7, "Y": 2, "Z": 6},
    }

    guide_2 = {
        "A": {"X": 3, "Y": 4, "Z": 8},
        "B": {"X": 1, "Y": 5, "Z": 9},
        "C": {"X": 2, "Y": 6, "Z": 7},
    }

    with open("input.txt") as f:
        print(
            sum(
                [
                    guide[line.strip().split(" ")[0]][line.strip().split(" ")[1]]
                    for line in f
                ]
            )
        )


if __name__ == "__main__":
    main()
