def load_input_line_by_line_int(filename):
    with open(filename, 'r') as f:
        content = f.readlines()

    content = [int(x.strip()) for x in content]
    return content


def load_input_line_by_line_string(filename):
    with open(filename, 'r') as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    return content


def load_input_char_only_digit(filename):
    array = []
    with open(filename, 'r') as file:
        while True:
            current_char = file.read(1)
            if not current_char:
                break
            if current_char.isdigit():
                array.append(int(current_char))
    return array
