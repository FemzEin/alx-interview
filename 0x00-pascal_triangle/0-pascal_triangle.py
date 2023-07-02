#!/usr/bin/python3
"""
Code to print Pascal Triangle on Terminal
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    """Initialize the triangle with the first row"""
    triangle = [[1]]

    """ Loop from 1 to n-1 """
    for i in range(1, n):
        row = [1]
        """ Loop from 1 to i-1 """
        for j in range(1, i):
            # Calculate the sum
            s = triangle[i-1][j] + triangle[i-1][j-1]
            """ Append the sum to the current row """
            row.append(s)
        """ Append the last element to the current row """
        row.append(1)
        """ Append the current row to the triangle """
        triangle.append(row)
    """ Return the triangle """
    return triangle
