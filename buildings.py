"""This code calculates farness from empty plots."""
from typing import List, Tuple


def nearest_buildings(buildings_qty: int, buildings_row: List[int]) -> int:
    """Nulls set & 3 farness direction ways detection from nulls."""
    proximity = [buildings_qty] * buildings_qty
    null = [i for i in range(buildings_qty) if buildings_row[i] == 0]
    init_null = null[0]
    last_null = null[-1]
    for i in range(init_null, buildings_qty):
        if buildings_row[i] == 0:
            proximity[i] = 0
        else:
            proximity[i] = proximity[i - 1] + 1
    for i in range(last_null, init_null, -1):
        if buildings_row[i] == 0:
            proximity[i] = 0
        else:
            proximity[i] = min(proximity[i], proximity[i + 1] + 1)
    for i in range(init_null - 1, -1, -1):
        proximity[i] = proximity[i + 1] + 1
    return proximity


def read_input() -> Tuple[int, List[int]]:
    """Input building quantity & building row."""
    buildings_qty = int(input())
    buildings_row = list(map(int, input().strip().split()))
    return buildings_qty, buildings_row


def init():
    """Intro & output."""
    buildings_qty, buildings_row = read_input()
    print(*nearest_buildings(buildings_qty, buildings_row))


if __name__ == '__main__':
    init()
