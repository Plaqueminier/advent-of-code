import sys
import os


def main(file):
    elves = [[]]
    idx = 0
    with open(file, 'r') as f:
        for line in f:
            if line[0] == "\n":
                elves.append([])
                idx += 1
            else:
                elves[idx].append(int(line))
    calories = [sum(calories_of_elves) for calories_of_elves in elves]
    print(calories, max(calories))
    print(sorted(calories, reverse=True)[:3], sum(sorted(calories, reverse=True)[:3]))             


if __name__ == "__main__":
    main(sys.argv[1])