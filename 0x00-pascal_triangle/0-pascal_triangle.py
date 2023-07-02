#!/usr/bin/python3
"""
Code to print Pascal Triangle on terminal
"""


def pascal_triangle(n):

    if n <= 0:
        yield from ()
""" Initialize the first row """
    row = [1]
""" Yield the first row """
    yield row


""" Loop from 1 to n-1 """
for i in range(1, n):
    next_row = [1]
""" Loop from 1 to i-1 """
for j in range(1, i):
    sum = row[j] + row[j-1]
""" Append the sum to the next row """
    next_row.append(sum)
""" Append the last element to the next row """
    next_row.append(1)
""" Yield the next row """
yield next_row
""" Update the current row with the next row """
row = next_row
