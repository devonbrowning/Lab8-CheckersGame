import numpy as np
from random import choice

def build_board(size: int):
# Generate a {size} x {size} board with random entries of "Empty", "Red", or "Black"
    if size < 4 or size > 16:
        raise ValueError("Board size must be between 4 and 16")

    choices = ['Empty', 'Red', 'Black']
    board = np.array([choice(choices) for i in range(size * size)]).reshape(size, size)
    return board

def get_count(board: int, item: str):
#  Count the number of occurrences of "item" in the board.
    return np.sum(board == item)

if __name__ == "__main__":
    print("This file is not intended to be run as a main script.")

