from dataclasses import dataclass, field
from typing import List
import random


@dataclass
class Valve:
    name: str
    rate: int
    tunnels: List["Valve"] = field(default_factory=list)
    is_open: bool = False
    is_target: bool = False

    def __repr__(self):
        return self.name


def get_valves(lines: str):
    valves = {}
    for line in lines:
        name = line.split(" has flow rate=")[0][6:]
        rate = int(line.split(" has flow rate=")[1].split(";")[0])
        valves[name] = Valve(name, rate)
    for line in lines:
        name = line.split(" has flow rate=")[0][6:]
        tunnels = line.replace("valves", "valve").split(" to valve ")[1].split(", ")
        for tunnel in tunnels:
            valves[name].tunnels.append(valves[tunnel])
    return valves


def get_max_valve_deep(
    valves: dict,
    current_target: Valve,
    path: List[str],
    deepness: int,
    current_max: Valve,
    current_deepness: int,
    current_path: List[str],
    time_limit: int,
):
    if deepness == min(10, time_limit):
        return current_max, current_deepness, current_path
    max_around = None
    for tunnel in current_target.tunnels:
        if tunnel.is_open or tunnel.rate == 0 or tunnel.is_target:
            continue
        if max_around == None or tunnel.rate > max_around.rate:
            max_around = tunnel

    if max_around != None:
        is_bigger = max_around.rate * (time_limit - deepness - 1) > current_max.rate * (
            time_limit - current_deepness - 1
        )
    if max_around != None and (is_bigger or current_max.is_open or current_max.is_target):
        current_max, current_deepness, current_path = max_around, deepness, path

    for tunnel in current_target.tunnels:
        current_max, current_deepness, current_path = get_max_valve_deep(
            valves,
            tunnel,
            path + [tunnel.name],
            deepness + 1,
            current_max,
            current_deepness,
            current_path,
            time_limit,
        )
    return current_max, current_deepness, current_path


def one():

    with open("input.txt") as f:
        lines = [line.strip() for line in f]

    valves = get_valves(lines)
    total_pressure = 0
    position = "AA"
    long_target, long_path = None, None

    for i in range(30):
        for valve in valves.values():
            if valve.is_open:
                print("Pressure gains " + str(valve.rate) + " from " + valve.name)
                total_pressure += valve.rate
        print("Pressure is now " + str(total_pressure))

        current_valve = valves[position]

        if not long_target:
            target, deepness, path = get_max_valve_deep(
                valves, current_valve, [], 1, current_valve, 0, [], 30 - i
            )
            long_target, long_path = target, path
        print(long_target, long_path)

        if current_valve == long_target and not long_target.is_open:
            current_valve.is_open = True
            long_target, long_path = None, None
            print("Open my valve " + position)
            continue

        if not current_valve.is_open and current_valve.rate != 0:
            current_valve.is_open = True
            print("Open my valve on the way " + position)
            continue

        if long_target != None and not long_target.is_open:
            position = long_path.pop(0) if len(long_path) else long_target.name
            print("Moved to path of target " + position)
            continue

        rand_index = random.randint(0, len(current_valve.tunnels) - 1)
        position = current_valve.tunnels[rand_index].name
        print("Moved randomly to " + position)

    print(total_pressure)


def two():

    with open("input.txt") as f:
        lines = [line.strip() for line in f]

    valves = get_valves(lines)
    total_pressure = 0
    my_position, e_position = "AA", "AA"
    my_target, my_path, e_target, e_path = None, None, None, None
    my_move, e_move = False, False

    for i in range(26):
        for valve in valves.values():
            if valve.is_open:
                print("Pressure gains " + str(valve.rate) + " from " + valve.name)
                total_pressure += valve.rate
        print("Pressure is now " + str(total_pressure))

        my_move, e_move = False, False
        current_valve = valves[my_position]
        e_valve = valves[e_position]

        if not my_target:
            target, _, path = get_max_valve_deep(
                valves, current_valve, [], 1, current_valve, 0, [], 26 - i
            )
            my_target, my_path = target, path
            my_target.is_target = True

        if not e_target:
            target, _, path = get_max_valve_deep(
                valves, e_valve, [], 1, e_valve, 0, [], 26 - i
            )
            e_target, e_path = target, path
            e_target.is_target = True

        print(my_target, my_path, e_target, e_path)
        if not my_move and current_valve == my_target and not my_target.is_open:
            current_valve.is_open = True
            current_valve.is_target = False
            my_target, my_path = None, None
            print("Open my valve " + my_position)
            my_move = True


        if not current_valve.is_open and current_valve.rate != 0:
            current_valve.is_open = True
            print("Open my valve on the way " + my_position)
            my_move = True

        if not my_move and my_target != None and not my_target.is_open:
            my_position = my_path.pop(0) if len(my_path) else my_target.name
            print("Moved to path of target " + my_position)
            my_move = True

        if not e_move and e_valve == e_target and not e_target.is_open:
            e_valve.is_open = True
            e_target.is_target = False
            e_target, e_path = None, None
            print("Elephant open valve " + e_position)
            e_move = True

        if not e_valve.is_open and e_valve.rate != 0:
            e_valve.is_open = True
            print("Elephant open valve on the way " + e_position)
            e_move = True

        if not e_move and e_target != None and not e_target.is_open:
            e_position = e_path.pop(0) if len(e_path) else e_target.name
            print("Elephant moved to path of target " + e_position)
            e_move = True

        if not my_move:
            rand_index = random.randint(0, len(current_valve.tunnels) - 1)
            my_position = current_valve.tunnels[rand_index].name
            print("Moved randomly to " + my_position)

        if not e_move:
            rand_index = random.randint(0, len(e_valve.tunnels) - 1)
            e_position = e_valve.tunnels[rand_index].name
            print("Elephant moved randomly to " + e_position)

    print(total_pressure)


if __name__ == "__main__":
    for i in range(10000):
        two()
