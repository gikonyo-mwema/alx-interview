#!/usr/bin/python3
"""
0-island_perimeter
This module contains a function that calculates the perimeter
of an island represented in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Parameters:
    grid (list of list of int): A 2D grid where 1 represents land
                                 and 0 represents water.

    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Check the four sides of the land cell
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1  # Top
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1  # Bottom
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1  # Left
                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1  # Right

    return perimeter
