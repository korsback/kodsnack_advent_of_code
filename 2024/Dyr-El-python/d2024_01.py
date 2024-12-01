from aoc_prepare import PrepareAoc
from utils.parse import parse_lines


def part1(inp):
    l1, l2 = map(
        sorted, map(list, zip(*parse_lines(inp, lambda l: map(int, l.split()))))
    )
    return sum(map(lambda x, y: abs(x - y), l1, l2))


def part2(inp):
    l1, l2 = map(list, zip(*parse_lines(inp, lambda l: map(int, l.split()))))
    return sum((l2.count(i1) * i1 for i1 in l1))


def test_1_1():
    assert (
        part1(
            """3   4
4   3
2   5
1   3
3   9
3   3"""
        )
        == 11
    )


def test_1_2():
    assert (
        part2(
            """3   4
4   3
2   5
1   3
3   9
3   3"""
        )
        == 31
    )


def main(inp):
    print("Part1:", part1(inp.strip()))
    print("Part2:", part2(inp.strip()))


if __name__ == "__main__":
    prep = PrepareAoc(2024, 1)
    main(prep.get_content())
