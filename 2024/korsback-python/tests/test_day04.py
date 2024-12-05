import pytest
from days import day04

test_data = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX"
]

test_data_2 = [
    ".M.S......",
    "..A..MSMS.",
    ".M.S.MAA..",
    "..A.ASMSM.",
    ".M.S.M....",
    "..........",
    "S.S.S.S.S.",
    ".A.A.A.A..",
    "M.M.M.M.M.",
    ".........."
]
test_data_2_split = [
    [".M.S......"],
    ["..A..MSMS."],
    [".M.S.MAA.."],
    ["..A.ASMSM."],
    [".M.S.M...."],
    [".........."],
    ["S.S.S.S.S."],
    [".A.A.A.A.."],
    ["M.M.M.M.M."],
    [".........."]
]

@pytest.mark.parametrize(
    "data, expected",
    [
        ("MMMSXXMASM", 1),
        ("MSAMXMSMSA", 1),
        ("MSAMXMASAM", 2),
    ]
)

def test_find_in_line(data, expected):
    assert day04.find_in_line(data) == expected

def test_get_vertical():
    assert day04.get_vertical(test_data, 0) == "MMAMXXSSMM"

def test_get_diagonal():
    data = [
        "ABCDEF", 
        "DEFGHI", 
        "JKLMNO", 
        "PQRSTU",
    ]
    expected = ["A", "BD", "CEJ", "DFKP", "EGLQ", "FHMR", "INS", "OT", "U"]

    assert day04.get_diagonal(data, False) == expected

def test_sort_lines():
    data = [
        "ABC", 
        "DEF", 
        "GHI", 
        "JKL"
    ]
    expected = [
        "JKL", 
        "GHI", 
        "DEF", 
        "ABC"
    ]

    assert day04.sort_lines(data) == expected

def test_get_diagonal_reverse():
    data = [
        "ABCDEF", 
        "DEFGHI", 
        "JKLMNO", 
        "PQRSTU",
    ]
    expected = ["P", "QJ", "RKD", "SLEA", "TMFB", "UNGC", "OHD", "IE", "F"]

    assert day04.get_diagonal(data, True) == expected

def test_get_diagonal_reverse_with_test_data():
    result = day04.get_diagonal(test_data, True)

    assert result[0] == "M"
    assert result[1] == "XM"
    assert result[2] == "MAS"

def test_get_verticals():
    data = [
        "ABC", 
        "DEF", 
        "GHI", 
        "JKL"
    ]
    expected = ["ADGJ", "BEHK", "CFIL"]

    assert day04.get_verticals(data) == expected

def test_run_a():

    data = [
        "XOOSXMASOXOOOXOOO",
        "MOOAOOSAMXOOOOMOO",
        "AOOMSOOAOOOOOOOAO",
        "SOOXOOSOOOOOOOOOS"
    ]
    assert day04.run_a(data) == 6

def test_run_a_with_real_data():

    assert day04.run_a(test_data) == 18

def test_lines_for_x_mas():
    data = [test_data_2[0], test_data_2[1], test_data_2[2]]
    expected = 1

    assert day04.test_lines_for_x_mas(data) == expected

def test_run_b():
    assert day04.run_b(test_data) == 9

