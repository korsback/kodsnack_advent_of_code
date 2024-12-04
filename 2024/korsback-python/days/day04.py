import helpers
import re

def start(filePath, part):
    data = helpers.read_file_lines(filePath)
    if part == "a":
        return run_a(data)
    elif part == "b":
        return run_b()

regex = r"(?=(XMAS))|(?=(SAMX))"

def find_in_line(line):
    return len(re.findall(regex, line))

def get_vertical(lines, index):
    vertical = ""
    for line in lines:
        vertical += line[index]

    return vertical

def get_verticals(lines):
    verticals = []
    for i in range(len(lines[0])):
        verticals.append(get_vertical(lines, i))

    return verticals

def get_diagonal(lines_input, reverse):
    diagonal = []
    lines = lines_input[:]

    if reverse:
        lines = sort_lines(lines)

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            diagonal_index = row + col

            while len(diagonal) <= diagonal_index:
                diagonal.append([])

            diagonal[diagonal_index].append(char)

    return ["".join(line) for line in diagonal]

def sort_lines(lines):
    return [line for line in reversed(lines)]

def run_a(data):
    parsed_lines = []
    parsed_lines.extend(data)
    parsed_lines.extend(get_verticals(data))
    parsed_lines.extend(get_diagonal(data, False))
    parsed_lines.extend(get_diagonal(data, True))
    
    sum = 0
    for line in parsed_lines:
        sum += find_in_line(line)

    return sum

def run_b(data):
    return 0