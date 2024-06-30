#!/usr/bin/python3
"""
Pascal's Triangle
"""


from math import factorial


def pascal_triangle(n):
    """
    Return pascals triangle using list of lists
    """

    # Return an empty list for non-positive n
    if n <= 0:
        return []

    # Initialize an empty list to store the rows
    triangle = []

    for i in range(n):
        # Create an empty list for the current row
        row = []

        for j in range(i+1):
            # Calculate the binomial cofficient (n choose k)
            coef = factorial(i) // (factorial(j) * factorial(i - j))
            # Add the coefficient to the row
            row.append(coef)
            # Add the row to the triangle
        triangle.append(row)

    return triangle
