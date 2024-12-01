import re


def parse_2D_to_dict(inp, filter=".*", strip=False):
    dictionary = dict()
    if strip:
        stripping = lambda x: x.strip()
    else:
        stripping = lambda x: x
    filter = re.compile(filter)
    for line_idx, line in enumerate(inp.splitlines()):
        for column_idx, character in enumerate(stripping(line)):
            if filter.match(character):
                dictionary[(column_idx, line_idx)] = character
    return dictionary


def parse_lines(inp, functions, split_groups=None):
    if split_groups:
        groups = list(inp.split(split_groups))
        group_result = list()
        for function, group in zip(functions, group):
            group_result.append(list())
            for line in group:
                group_result[-1].append(function(line))
        return group_result
    result = []
    for line in inp.splitlines():
        result.append(functions(line))
    return result
