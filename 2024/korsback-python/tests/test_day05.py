import pytest
from days import day05

data = [
    "47|53", "97|13", "97|61", "97|47", "75|29", "61|13", "75|53", "29|13",
    "97|29", "53|29", "61|53", "97|53", "61|29", "47|13", "75|47", "97|75",
    "47|61", "75|61", "47|29", "75|13", "53|13","",
    "75,47,61,53,29", "97,61,53,29,13", "75,29,13", "75,97,47,61,53",
    "61,13,29", "97,13,75,29,47"
]

test_data = ["1|2", "3|4", "", "1,2,3", "4,3,5"]

def test_split_data():
    assert day05.split_data(test_data) == [["1|2", "3|4"], ["1,2,3", "4,3,5"]]

def test_split_instruction():
    assert day05.split_instruction("1|2") == ("1", "2")
    assert day05.split_instruction("3|4") == ("3", "4")

def test_check_order():
    assert day05.check_order("1", "2", "1,2,3") == True
    assert day05.check_order("2", "1", "1,2,3") == False

def test_run_a_with_test_data():
    assert day05.run_a(test_data) == 2

def test_run_a_with_data():
    assert day05.run_a(data) == 143