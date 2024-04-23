#!/usr/bin/python3
"""
Rotate 2D Matrix Module
"""

def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.
    
    Args:
        matrix (list of list): 2D matrix to rotate
    
    Returns:
        None: The matrix is edited in-place
    """
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
