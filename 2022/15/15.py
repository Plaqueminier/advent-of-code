from dataclasses import dataclass
from typing import List
import math


def one():

    with open("input.txt") as f:
        lines = [line.strip() for line in f]

    sensors = []
    beacons = []
    distances = []
    for line in lines:
        sensor_start = line[12:].split(", y=")
        sensor = (int(sensor_start[0]), int(sensor_start[1].split(":")[0]))
        beacon_start = line.split(": closest beacon is at x=")[1].split(", y=")
        beacon = (int(beacon_start[0]), int(beacon_start[1]))
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        distances.append(distance)
        sensors.append(sensor)
        beacons.append(beacon)
    print(sensors)
    print(beacons)
    print(distances)

    covered_count = 0
    for i in range(
        min([beacon[0] for beacon in beacons]) - 1000000,
        max([beacon[0] for beacon in beacons]) + 1000000,
    ):
        print(i)
        is_covered = False
        for index, sensor in enumerate(sensors):
            distance_to_pos = abs(sensor[0] - i) + abs(sensor[1] - 2000000)
            if (i, 2000000) not in beacons and distance_to_pos <= distances[index]:
                is_covered = True
                break
        if is_covered:
            covered_count += 1
    print(covered_count)


def two():

    with open("input.txt") as f:
        lines = [line.strip() for line in f]

    sensors = []
    beacons = []
    distances = []
    for line in lines:
        sensor_start = line[12:].split(", y=")
        sensor = (int(sensor_start[0]), int(sensor_start[1].split(":")[0]))
        beacon_start = line.split(": closest beacon is at x=")[1].split(", y=")
        beacon = (int(beacon_start[0]), int(beacon_start[1]))
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        distances.append(distance)
        sensors.append(sensor)
        beacons.append(beacon)
    print(sensors)
    print(beacons)
    print(distances)

    points_to_check = []
    for i, sensor in enumerate(sensors):
        x = sensor[0]
        y = sensor[1] - distances[i] - 1
        if x > 0 and x < 4000000 and y > 0 and y < 4000000:
            points_to_check.append((sensor[0], sensor[1] - distances[i] - 1))
        while x != sensor[0] + distances[i] + 1 and y != sensor[1]:
            x += 1
            y += 1
            if x > 0 and x < 4000000 and y > 0 and y < 4000000:
                points_to_check.append((x, y))
        while x != sensor[0] and y != sensor[1] + distances[i] + 1:
            x -= 1
            y += 1
            if x > 0 and x < 4000000 and y > 0 and y < 4000000:
                points_to_check.append((x, y))
        while x != sensor[0] - distances[i] - 1 and y != sensor[1]:
            x -= 1
            y -= 1
            if x > 0 and x < 4000000 and y > 0 and y < 4000000:
                points_to_check.append((x, y))
        while x != sensor[0] and y != sensor[1] - distances[i] - 1:
            x += 1
            y -= 1
            if x > 0 and x < 4000000 and y > 0 and y < 4000000:
                points_to_check.append((x, y))

    print(len(points_to_check))
    for (x, y) in points_to_check:
        is_covered = False
        for index, sensor in enumerate(sensors):
            distance_to_pos = abs(sensor[0] - x) + abs(sensor[1] - y)
            if distance_to_pos <= distances[index]:
                is_covered = True
                break
        if not is_covered and (x, y) not in beacons:
            print("found it", x, y)
            return


if __name__ == "__main__":
    # one()
    two()
