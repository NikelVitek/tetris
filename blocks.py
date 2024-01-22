# Importing necessary classes for the Tetris blocks
from block import Block
from position import Position


# Class for the L-shaped Tetris block
class L(Block):
    def __init__(self):
        # Initializing the L block with ID 1
        super().__init__(id=1)
        # Define the cell positions for each orientation
        self.cells = {
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
        }
        # Move the block to the initial position (0, 3)
        self.move(0, 3)


# Class for the J-shaped Tetris block
class J(Block):
    def __init__(self):
        # Initializing the J block with ID 2
        super().__init__(id=2)
        # Define the cell positions for each orientation
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }
        # Move the block to the initial position (0, 3)
        self.move(0, 3)


# Class for the I-shaped Tetris block
class I(Block):
    def __init__(self):
        # Initializing the I block with ID 3
        super().__init__(id=3)
        # Define the cell positions for each orientation
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }
        # Move the block to the initial position (-1, 3)
        self.move(-1, 3)


# Class for the O-shaped Tetris block
class O(Block):
    def __init__(self):
        # Initializing the O block with ID 4
        super().__init__(id=4)
        # Define the cell positions for the only orientation
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
        }
        # Move the block to the initial position (0, 4)
        self.move(0, 4)


# Class for the S-shaped Tetris block
class S(Block):
    def __init__(self):
        # Initializing the S block with ID 5
        super().__init__(id=5)
        # Define the cell positions for each orientation
        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        # Move the block to the initial position (0, 3)
        self.move(0, 3)


# Class for the T-shaped Tetris block
class T(Block):
    def __init__(self):
        # Initializing the T block with ID 6
        super().__init__(id=6)
        # Define the cell positions for each orientation
        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        # Move the block to the initial position (0, 3)
        self.move(0, 3)


# Class for the Z-shaped Tetris block
class Z(Block):
    def __init__(self):
        # Initializing the Z block with ID 7
        super().__init__(id=7)
        # Define the cell positions for each orientation
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        }
        # Move the block to the initial position (0, 3)
        self.move(0, 3)
