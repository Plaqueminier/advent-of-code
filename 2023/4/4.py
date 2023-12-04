file_path = "4.txt"


def part_1():
    scores = 0
    with open(file_path, "r") as file:
        for line in file:
            id, cards = line.split(":")
            id = int(id[5:])
            w_cards, m_cards = cards.split("|")
            w_cards = [
                int(x.strip()) for x in w_cards.strip().replace("  ", " ").split(" ")
            ]
            m_cards = [
                int(x.strip()) for x in m_cards.strip().replace("  ", " ").split(" ")
            ]
            intersection = set(w_cards).intersection(set(m_cards))
            if (len(intersection) == 0):
                continue
            scores += pow(2, len(set(w_cards).intersection(set(m_cards))) - 1)
        print(scores)


def part_2():
    ids = 0
    with open(file_path, "r") as file:
        lines = file.readlines()
        stack = [0] + ([1] * (len(lines)))
        for line in lines:
            ids += 1
            id, cards = line.split(":")
            id = int(id[5:])
            w_cards, m_cards = cards.split("|")
            w_cards = [
                int(x.strip()) for x in w_cards.strip().replace("  ", " ").split(" ")
            ]
            m_cards = [
                int(x.strip()) for x in m_cards.strip().replace("  ", " ").split(" ")
            ]
            intersection = set(w_cards).intersection(set(m_cards))
            if (len(intersection) == 0):
                continue
            for i in range(1, len(intersection) + 1):
                if (len(stack) >= id + i):
                    stack[id + i] += stack[id]
        print(sum(stack))


part_1()

part_2()
