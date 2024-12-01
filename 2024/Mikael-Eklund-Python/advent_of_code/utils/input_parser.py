from typing import List, Union

def parse_integers(input_data: str) -> List[int]:
    """
    Parse input into a list of integers.
    
    Args:
        input_data (str): Raw input string
    
    Returns:
        List[int]: List of parsed integers
    """
    return [int(line) for line in input_data.splitlines()]

def parse_str_lines(input_data: str) -> List[str]:
    """
    Parse input into a list of strings.
    
    Args:
        input_data (str): Raw input string
    
    Returns:
        List[str]: List of input lines
    """
    return input_data.splitlines()

def parse_grid(input_data: str, convert_type: type = str) -> List[List[Union[str, int]]]:
    """
    Parse input into a 2D grid.
    
    Args:
        input_data (str): Raw input string
        convert_type (type, optional): Type to convert grid elements to. Defaults to str.
    
    Returns:
        List[List[Union[str, int]]]: 2D grid of parsed elements
    """
    return [
        [convert_type(char) for char in line.strip()]
        for line in input_data.splitlines()
    ]