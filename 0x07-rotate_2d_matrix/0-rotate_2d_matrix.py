#!/usr/bin/python3
"""
Rotate 2D Matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list): The 2D matrix to be rotated.
    """
    n = len(matrix)  # size of the matrix

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):  # Start from i
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):  # Loop through each row
        matrix[i] = matrix[i][::-1]  # Reverse row in-place
