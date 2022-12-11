def is_visible_left(trees, tree, x, y):
    for k in range(0, x):
        if trees[y][k] >= tree:
            return False
    return True


def is_visible_right(trees, tree, x, y):
    for k in range(x + 1, len(trees[0])):
        if trees[y][k] >= tree:
            return False
    return True


def is_visible_up(trees, tree, x, y):
    for k in range(0, y):
        if trees[k][x] >= tree:
            return False
    return True


def is_visible_down(trees, tree, x, y):
    for k in range(y + 1, len(trees[0])):
        if trees[k][x] >= tree:
            return False
    return True


def one():

    with open("input.txt") as f:
        lines = [line for line in f]

    trees = []
    for line in lines:
        line = line.strip()
        trees.append([])
        for tree in line:
            trees[-1].append(int(tree))

    visible_sum = 0
    print(trees)
    for y, row in enumerate(trees):
        for x, tree in enumerate(row):
            if x == 0 or y == 0 or x == len(row) - 1 or y == len(trees) - 1:
                visible_sum += 1
            else:
                if (
                    is_visible_left(trees, tree, x, y)
                    or is_visible_right(trees, tree, x, y)
                    or is_visible_up(trees, tree, x, y)
                    or is_visible_down(trees, tree, x, y)
                ):
                    visible_sum += 1
                    continue

    print(visible_sum)


def scenic_left(trees, tree, x, y):
    score = 1
    for k in range(x - 1, 0, -1):
        if trees[y][k] >= tree:
            return score
        score += 1 if k > 0 and k < len(trees[0]) - 1 else 0
    return score


def scenic_right(trees, tree, x, y):
    score = 1
    for k in range(x + 1, len(trees[0])):
        if trees[y][k] >= tree:
            return score
        score += 1 if k > 0 and k < len(trees[0]) - 1 else 0
    return score


def scenic_up(trees, tree, x, y):
    score = 1
    for k in range(y - 1, 0, -1):
        if trees[k][x] >= tree:
            return score
        score += 1 if k > 0 and k < len(trees[0]) - 1 else 0
    return score


def scenic_down(trees, tree, x, y):
    score = 1
    for k in range(y + 1, len(trees[0])):
        if trees[k][x] >= tree:
            return score
        score += 1 if k > 0 and k < len(trees[0]) - 1 else 0
    return score


def two():

    with open("input.txt") as f:
        lines = [line for line in f]

    trees = []
    for line in lines:
        line = line.strip()
        trees.append([])
        for tree in line:
            trees[-1].append(int(tree))

    scenic_scores = []
    for y, row in enumerate(trees):
        for x, tree in enumerate(row):
            if x == 0 or y == 0 or x == len(row) - 1 or y == len(trees) - 1:
                continue
            else:
                scenic_scores.append(
                    scenic_up(trees, tree, x, y)
                    * scenic_right(trees, tree, x, y)
                    * scenic_down(trees, tree, x, y)
                    * scenic_left(trees, tree, x, y),
                )
    print(scenic_scores)
    print(max(scenic_scores))


if __name__ == "__main__":
    one()
    two()
