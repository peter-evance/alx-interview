#!/usr/bin/python3
"""
A module for working with Pascal's triangle.
"""


# def pascal_triangle(n):
#     """
#     Creates a list of lists of integers representing
#     the Pascal's triangle of a given integer.
#     """
#     triangle = []
#     if type(n) is not int or n <= 0:
#         return triangle
#     for i in range(n):
#         line = []
#         for j in range(i + 1):
#             if j == 0 or j == i:
#                 line.append(1)
#             elif i > 0 and j > 0:
#                 line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
#         triangle.append(line)
#     return triangle
def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.
    
    Args:
        n (int): The number of rows for Pascal's triangle.
        
    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle