import helpers

def start(filePath, part):
    data = helpers.read_file_lines(filePath)
    if part == "a":
        return run_a(data)
    elif part == "b":
        return run_b(data)

def run_a(data):
    return 0

def run_b(data):
    return 0