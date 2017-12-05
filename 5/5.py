from utils.utils import load_input_line_by_line_int


def run(part_two):
    items = load_input_line_by_line_int('input.txt')
    length_items = len(items)
    step = 0
    index = 0
    while length_items > index >= 0:
        number = items[index]
        if part_two:
            items[index] += -1 if number > 2 else 1
        else:
            items[index] += 1
        step += 1
        index = number + index
    return step


# Part One
print('Day Five, Part One: ', run(False))

# Part Two
print('Day Five, Part Two: ', run(True))
