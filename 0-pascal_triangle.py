#!/usr/bin/python3

def pascal_triangle(n):
  # Returns an empty list if n <= 0
  if n <= 0:
    return []
  # Initialize the triangle with the first row
  triangle = [[1]]
  # Loop from 1 to n-1
  for i in range(1, n):
    # Initialize the current row with the first element
    row = [1]
    # Loop from 1 to i-1
    for j in range(1, i):
      # Get the sum of the previous row elements at j and j-1
      sum = triangle[i-1][j] + triangle[i-1][j-1]
      # Append the sum to the current row
      row.append(sum)
    # Append the last element to the current row
    row.append(1)
    # Append the current row to the triangle
    triangle.append(row)
  # Return the triangle
  return triangle

