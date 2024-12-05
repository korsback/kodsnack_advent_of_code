import helpers

def start(filePath, part):
    data = helpers.read_file_lines(filePath)
    if part == "a":
        return run_a(data)
    elif part == "b":
        return run_b(data)

def filter_rows(data, char):
    return [row for row in data if char in row]

def split_data(data):
    return [filter_rows(data, "|"), filter_rows(data, ",")]

def split_instruction(instruction):
    split = instruction.split("|")
    return (split[0], split[1])

def check_order(a, b, line):
   return line.index(a) < line.index(b)

def run_a(data):
    data = split_data(data)
    instructions = data[0]
    lines = data[1]

    middle_values = []

    for line in lines:
        tmp = line.split(',')
        valid = True
        for instruction in instructions:
            a, b = split_instruction(instruction)
            if ((a in tmp and b in tmp) and check_order(a, b, tmp) == False):
                valid = False
                break

        if valid:
            index = len(tmp)//2
            middle_values.append(tmp[index])

    return sum(int(value) for value in middle_values)

def run_b(data):
    return 0