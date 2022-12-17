from dataclasses import dataclass
from typing import List

def parse_walls_and_find_min_max(lines: List[str]):
    max_x_y = (None, None)
    min_x_y = (None, None)
    walls = []
    for line in lines:
        wall = [
            (int(wall.split(",")[0]), int(wall.split(",")[1]))
            for wall in line.split(" -> ")
        ]
        for rock in wall:
            if max_x_y[0] == None or rock[0] > max_x_y[0]:
                max_x_y = (rock[0], max_x_y[1])
            if max_x_y[1] == None or rock[1] > max_x_y[1]:
                max_x_y = (max_x_y[0], rock[1])
            if min_x_y[0] == None or rock[0] < min_x_y[0]:
                min_x_y = (rock[0], min_x_y[1])
            if min_x_y[1] == None or rock[1] < min_x_y[1]:
                min_x_y = (min_x_y[0], rock[1])
        walls.append(wall)
    return walls, (min_x_y[0] - 300, min_x_y[1]), (max_x_y[0] + 300, max_x_y[1])

def fill_walls(walls: List[List[tuple]]):
    for wall in walls:
        for i, rock in enumerate(wall):
            if i + 1 == len(wall):
                break
            (rock_x, rock_y) = rock
            (next_rock_x, next_rock_y) = wall[i + 1]
            if abs(rock_x - next_rock_x) > 1:
                diff = rock_x - next_rock_x
                index = i + 1
                for x in range(rock_x - 1 if diff > 1 else rock_x + 1, next_rock_x, -1 if diff > 1 else 1):
                    wall.insert(index, (x, rock_y))
                    index += 1
            if abs(rock_y - next_rock_y) > 1:
                diff = rock_y - next_rock_y
                index = i + 1
                for y in range(rock_y - 1 if diff > 1 else rock_y + 1, next_rock_y, -1 if diff > 1 else 1):
                    wall.insert(index, (rock_x, y))
                    index += 1
    return walls

def print_map(air_map: List[List[str]]):
    for row in air_map:
        print("".join(row))

def construct_map(walls: List[List[tuple]], min_x_y: tuple, max_x_y: tuple):
    air_map = []
    for y in range(min_x_y[1], max_x_y[1] + 1):
        row = []
        for x in range(min_x_y[0], max_x_y[0] + 1):
            row.append(".")
        air_map.append(row)

    for wall in walls:
        for y, map_y in enumerate(range(min_x_y[1], max_x_y[1] + 1)):
            for x, map_x in enumerate(range(min_x_y[0], max_x_y[0] + 1)):
                if (map_x, map_y) in wall:
                    air_map[y][x] = "#"

    return air_map

def sand_fall(air_map: List[List[str]], start_x: int):
    y = 0
    x = start_x
    if air_map[y][x] == "o":
        return False
    while True:
        if y < 0 or y >= len(air_map) or x < 0 or x >= len(air_map[y]):
            return False
        if y == len(air_map) - 1 or air_map[y + 1][x] == ".":
            y += 1
            continue
        if y == len(air_map) - 1 or x == 0 or air_map[y + 1][x - 1] == ".":
            y += 1
            x -= 1
            continue
        if y == len(air_map) - 1 or x == len(air_map[y]) - 1 or air_map[y + 1][x + 1] == ".":
            y += 1
            x += 1
            continue
        air_map[y][x] = "o"
        break
    return True

def one():

    with open("input.txt") as f:
        lines = [line.strip() for line in f]

    walls, min_x_y, max_x_y = parse_walls_and_find_min_max(lines)
    walls = fill_walls(walls)
    air_map = construct_map(walls, min_x_y, max_x_y)
    print_map(air_map)
    fall_point = 500 - min_x_y[0]
    air_map = [["." for _ in range(len(air_map[0]))] for _ in range(min_x_y[1])] + air_map
    # For level 2
    air_map += [["." for _ in range(len(air_map[0]))], ["#" for _ in range(len(air_map[0]))]]
    sand_state = sand_fall(air_map, fall_point)
    count = 0
    while sand_state:
        sand_state = sand_fall(air_map, fall_point)
        count += 1
    print_map(air_map)
    print(count)


if __name__ == "__main__":
    one()
