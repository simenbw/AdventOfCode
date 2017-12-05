from utils.utils import load_input_line_by_line_string

items = load_input_line_by_line_string('input.txt')


def task_one():
    count = 0
    for i in range(len(items)):
        words = items[i].split()
        if len(words) == len(set(words)):
            count += 1
    return count


def task_two():
    count = 0
    for i in range(len(items)):
        words = items[i].split()
        for y in range(len(words)):
            words[y] = ''.join(sorted(words[y]))
        if len(words) == len(set(words)):
            count += 1
    return count


# Part One
print('Day Four, Part One: ', task_one())

# Part two
print('Day Four, Part Two: ', task_two())

