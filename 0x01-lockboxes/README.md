
Lockboxes

This project provides a Python implementation of a function to determine if all the lockboxes can be opened, following the provided instructions.

Overview

The canUnlockAll function takes a list of lists representing the lockboxes and their respective keys. It returns True if all the boxes can be opened, otherwise False.

Usage

To use this function, simply call canUnlockAll(boxes), where boxes is a list of lists representing the lockboxes and their keys. It will return True if all the boxes can be opened, otherwise False.

Example:

from lockboxes import canUnlockAll

boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False

Requirements

Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
README.md file, at the root of the folder of the project, is mandatory
Your code should be documented
Your code should use the PEP 8 style (version 1.7.x)
All your files must be executable

License

This project is licensed under the MIT License - see the LICENSE file for details.

