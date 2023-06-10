"""This code calculates points in hands agility game."""
from typing import Tuple


def keys_vs_numbers(sixteen_cells: Tuple[int], keys: int) -> int:
    """Numbers vs key coincide & points calculation function."""
    set_row = [0] * 10
    for ind in sixteen_cells:
        if ind != '.':
            set_row[int(ind)] = set_row[int(ind)] + 1
    points = 0
    for num in set_row:
        if int(num) <= 2*keys and int(num) > 0:
            points = points + 1
    return points


def read_input() -> Tuple[int, Tuple[int]]:
    """Input available keys number for each player & gameplay field."""
    keys = int(input())
    sixteen_cells = []
    for _ in range(4):
        input_num = input().strip()
        sixteen_cells.extend(tuple(input_num))
    return sixteen_cells, keys


def init():
    """Intro & output."""
    sixteen_cells, keys = read_input()
    print(keys_vs_numbers(sixteen_cells, keys))


if __name__ == '__main__':
    init()
