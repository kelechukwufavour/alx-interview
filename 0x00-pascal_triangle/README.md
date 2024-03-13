0x00-pascal_triangle
Below is the implementation of the Pascal's Triangle function in Python, adhering to the provided instructions:

def pascal_triangle(n):
    """
    Generate Pascal's triangle of n rows.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Print the triangle.
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))

You can find this code in the file 0-pascal_triangle.py within the directory 0x00-pascal_triangle of the GitHub repository alx-interview.

README.md

Pascal's Triangle

This project provides a Python implementation of Pascal's Triangle generation function, following the instructions provided.

Overview

The pascal_triangle function generates Pascal's triangle of n rows. It returns a list of lists of integers representing the triangle.

Usage

To use this function, simply call pascal_triangle(n), where n is the desired number of rows in the triangle. It will return the Pascal's triangle as a list of lists of integers.

Example:

from pascal_triangle import pascal_triangle

triangle_5_rows = pascal_triangle(5)
print(triangle_5_rows)

Output:

[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

Requirements

	Python 3.x

License

This project is licensed under the MIT License - see the LICENSE file for details.
