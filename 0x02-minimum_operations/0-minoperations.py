#!/usr/bin/python3
""" Minumun Operations """


def minOperations(n):
    """
    calculates the fewest number of operations needed,
    to result in exactly n H characters in the file.
    """
    current_h = 1
    operations = 0
    while current_h < n:
        if n % current_h == 0:
            # Use Copy All and Paste to double the count
            current_h *= 2
            operations += 1
        else:
            # Increment by 1 using Paste
            current_h += 1
            operations += 1
    return operations
