def pascal_triangle(n):
  """
  Prints an array of Pascal's triangle.

  Args:
    n: The number of rows in the triangle.
  """

  triangle = [[1]]
  for i in range(1, n):
    row = [1]
    for j in range(1, i + 1):
      row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
    triangle.append(row)
  for row in triangle:
    print(row)


print(pascal_triangle(5))
