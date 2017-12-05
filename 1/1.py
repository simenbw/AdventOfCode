from utils.utils import load_input_char_only_digit


def run_calc(subtract_index):
    total_sum = 0
    for i in range(len(items)):
        check_against_index = i - subtract_index
        if items[i] == items[check_against_index]:
            total_sum += items[i]
    return total_sum


items = load_input_char_only_digit('input.txt')

# Part One
print('Day One, Part One: ', run_calc(1))

# Part Two
print('Day One, Part Two: ', run_calc(int(len(items) / 2)))


