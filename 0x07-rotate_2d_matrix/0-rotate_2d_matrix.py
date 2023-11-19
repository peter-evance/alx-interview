#!/usr/bin/python3
"""
Rotation 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in place.

    Parameters:
    - matrix (list): The input 2D matrix to be rotated.

    Returns:
    - None: The matrix is modified in place.
    """

    # Check if the input is a valid 2D matrix
    if not isinstance(matrix, list) or not matrix or not all(isinstance(row, list) for row in matrix):
        return
    
    # Check if all rows have the same number of columns
    num_columns = len(matrix[0])
    if not all(len(row) == num_columns for row in matrix):
        return
    
    rows, cols = len(matrix), num_columns
    new_matrix = []

    # Iterate through each element in the original matrix
    for i in range(rows * cols):
        # Add a new row if the current column index is a multiple of the number of rows
        if i % rows == 0:
            new_matrix.append([])

        # Determine the current column (c) and row (r) indices in the original matrix
        c, r = i % cols, rows - 1 - i // cols

        # Append the corresponding element to the new matrix
        new_matrix[-1].append(matrix[r][c])

    # Update the input matrix with the rotated elements
    matrix[:] = new_matrix
