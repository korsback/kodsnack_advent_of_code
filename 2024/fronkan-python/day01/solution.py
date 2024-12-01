from argparse import ArgumentParser
from collections import Counter
from pathlib import Path


def puzzle1(input_file: Path):
    l1 = []
    l2 = []
    for line in input_file.read_text().splitlines():
        v1, v2 = line.split()
        l1.append(int(v1))
        l2.append(int(v2))

    l1 = sorted(l1)
    l2 = sorted(l2)

    return sum(abs(v1 - v2) for v1, v2 in zip(l1, l2))


def puzzle2(input_file: Path):
    l1 = []
    l2 = []
    for line in input_file.read_text().splitlines():
        v1, v2 = line.split()
        l1.append(int(v1))
        l2.append(int(v2))

    counts = Counter(l2)
    return sum(v * counts[v] for v in l1)


if __name__ == "__main__":
    print("Day 1")
    parser = ArgumentParser()
    parser.add_argument("--example", action="store_true", default=False)
    args = parser.parse_args()
    if args.example:
        print("running example file")
        input_file = Path(__file__).parent / "example_input.txt"
    else:
        input_file = Path(__file__).parent / "input.txt"
    print("Puzzle 1:", puzzle1(input_file))
    try:
        print("Puzzle 2:", puzzle2(input_file))
    except NotImplementedError:
        print("puzzle 2 not implemented yet")
