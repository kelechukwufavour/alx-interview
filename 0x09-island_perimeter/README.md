This README provides an overview of the problem, explains the solution, and offers usage instructions. It also outlines the environment requirements and credits the author.

# Island Perimeter

## Task

Create a function `island_perimeter(grid)` that returns the perimeter of the island described in `grid`:

- `grid` is a list of list of integers:
  - `0` represents water
  - `1` represents land
- Each cell is square, with a side length of `1`
- Cells are connected horizontally/vertically (not diagonally).
- `grid` is rectangular, with its width and height not exceeding `100`
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

## Solution

The solution to the problem is implemented in `0-island_perimeter.py`. This script defines a function `island_perimeter(grid)` that calculates the perimeter of the island in the given grid.

## Usage

To use the function `island_perimeter(grid)`, import it into your Python script or interactive session and call it with a valid grid as an argument.

Example:

```python
from 0-island_perimeter import island_perimeter

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

print(island_perimeter(grid))  # Output: 12
Environment
Allowed editors: vi, vim, emacs
Interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
Follows PEP 8 style (version 1.7)
No external modules are imported
All modules and functions are documented
All files are executable
Author
This solution was created by Kelechukwu Favour.




