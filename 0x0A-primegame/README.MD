# Prime Game

## Description
Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, this program determines who the winner of each game is.

## Prototype
```python
def isWinner(x, nums):
    pass
Usage
python
Copy code
print(isWinner(5, [2, 5, 1, 4, 3]))  # Output: Ben
Requirements
Allowed editors: vi, vim, emacs
All files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All files should end with a new line
The first line of all files should be exactly #!/usr/bin/python3
Your code should use the PEP 8 style (version 1.7.x)
