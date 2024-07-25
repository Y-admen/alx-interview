#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generates a Pascal's triangle of a given height.

    Args:
    n (int): The height of the Pascal's triangle to generate.

    Returns:
    list: A list of lists representing the Pascal's triangle.
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
