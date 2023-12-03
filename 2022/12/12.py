from dataclasses import dataclass
from typing import List


@dataclass
class Node:
    x: int
    y: int
    height: int
    is_start: bool = False
    is_end: bool = False
    g_cost: int = 0
    f_cost: int = 0
    parent: "Node" = None

    def get_neighbors(self, nodes):
        neighbors = []
        if self.x > 0:
            neighbors.append(
                list(
                    filter(
                        lambda node: node.x == self.x - 1 and node.y == self.y, nodes
                    )
                )[0]
            )
        if self.x < max(nodes, key=lambda node: node.x).x:
            neighbors.append(
                list(
                    filter(
                        lambda node: node.x == self.x + 1 and node.y == self.y, nodes
                    )
                )[0]
            )
        if self.y > 0:
            neighbors.append(
                list(
                    filter(
                        lambda node: node.x == self.x and node.y == self.y - 1, nodes
                    )
                )[0]
            )
        if self.y < max(nodes, key=lambda node: node.y).y:
            neighbors.append(
                list(
                    filter(
                        lambda node: node.x == self.x and node.y == self.y + 1, nodes
                    )
                )[0]
            )
        return neighbors

    def __repr__(self):
        return f"({self.x}, {self.y}), {self.height}, {self.g_cost}, {self.f_cost}"


def a_star(starts, goal, nodes: List[Node]):

    closed: List[Node] = []
    open: List[Node] = []
    open.extend(starts)

    while open:
        open.sort(key=lambda x: x.f_cost)
        current: Node = open.pop(0)
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = current.parent
            return path[::-1]

        if current not in closed:
            closed.append(current)
        neighbors = current.get_neighbors(nodes)

        for neighbor in neighbors:
            new_g_cost = current.g_cost + get_cost(current, neighbor)
            if (
                neighbor not in closed or new_g_cost < neighbor.g_cost
            ) and new_g_cost < 100000:
                neighbor.g_cost = new_g_cost
                neighbor.parent = current
                priority = new_g_cost + get_heuristic(goal, neighbor)
                neighbor.f_cost = priority
                if neighbor not in open:
                    open.append(neighbor)
    print("No path found")


# Define a function to get the cost of moving from one node to another
def get_cost(current, neighbor):
    if neighbor.is_start:
        return 0
    diff = current.height - neighbor.height
    if diff <= -2:
        return 100000
    return 10 if diff >= 0 else 5


# Define a function to get the heuristic of a node
def get_heuristic(goal, node):
    return (abs(goal.x - node.x) + abs(goal.y - node.y)) * 10


def one():

    with open("input.txt") as f:
        lines = [line for line in f]

    nodes: List[Node] = []
    y = 0
    for line in lines:
        print(line.strip())
        x = 0
        for char in line.strip():
            nodes.append(
                Node(
                    x=x,
                    y=y,
                    height=0
                    if char == "S" or char == "a"
                    else 26
                    if char == "E"
                    else ord(char) - 97,
                    is_start=True if char == "S" or char == "a" else False,
                    is_end=True if char == "E" else False,
                )
            )
            x += 1
        y += 1

    print()
    res_nodes = a_star(
        list(filter(lambda node: node.is_start, nodes)),
        list(filter(lambda node: node.is_end, nodes))[0],
        nodes,
    )
    for node in res_nodes:
        print(node.x, node.y, node.height, node.g_cost, node.f_cost)
    print(len(res_nodes))


if __name__ == "__main__":
    one()
