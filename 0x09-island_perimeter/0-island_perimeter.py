#!/usr/bin/python3
"""Island perimeter module."""


def island_perimeter(grid):
    """Calculates the perimeter of an island without lakes."""
    perimeter = 0
    if type(grid) != list:
        return 0
    num = len(grid)
    for i, row in enumerate(grid):
        row_count = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            outline = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == row_count - 1 or (row_count > j + 1 and row[j + 1] == 0),
                i == num - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(outline)
    return perimeter
