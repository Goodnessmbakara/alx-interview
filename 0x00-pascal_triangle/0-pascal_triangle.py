#!/usr/bin/python3
""" Module to find generate Pascals in an array"""


def pascal_triangle(n):
    """
    function to find pascals triangle

        Parameters:
            n(int): numbers of rows to generate

        Return:
            triangle: pascal_triangle in an array
    """

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
