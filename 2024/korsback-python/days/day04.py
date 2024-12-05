import helpers
import re

def start(filePath, part):
    data = helpers.read_file_lines(filePath)
    if part == "a":
        return run_a(data)
    elif part == "b":
        return run_b(data)

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

def test_lines_for_x_mas(lines):

    length = len(lines[0])
    count = 0
    line_top = lines[0]
    line_search = lines[1]
    line_bottom = lines[2]

    for i in range(length):
        if i > 0 and i < length - 1 and line_search[i] == "A":
            if (
                (line_top[i-1] + line_search[i] + line_bottom[i+1] == "MAS" or line_top[i-1] + line_search[i] + line_bottom[i+1] == "SAM") and
                (line_top[i+1] + line_search[i] + line_bottom[i-1] == "MAS" or line_top[i+1] + line_search[i] + line_bottom[i-1] == "SAM")
            ):
                count += 1

    return count

def run_b(data):
    count = 0
    for i in range(len(data)-2):
        lines = [data[i], data[i+1], data[i+2]]
        count += test_lines_for_x_mas(lines)

    return count