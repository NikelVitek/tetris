# Importing necessary modules and classes
from grid import Grid
from blocks import *
import random


# Class representing the Tetris game
class Game:
    def __init__(self):
        # Initializing the game with an empty grid
        self.grid = Grid()
        # List of different Tetris blocks
        self.blocks = [I(), J(), L(), O(), S(), T(), Z()]
        # Current and next blocks in play
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        # Flag to track game over status
        self.game_over = False

    # Selects a random block from the available ones
    def get_random_block(self):
        # If no blocks are left, reset the block list
        if len(self.blocks) == 0:
            self.blocks = [I(), J(), L(), O(), S(), T(), Z()]
        # Choose and remove a random block from the list
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    # Moves the current block to the left
    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() is False or self.block_fits() is False:
            self.current_block.move(0, 1)

    # Moves the current block to the right
    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() is False or self.block_fits() is False:
            self.current_block.move(0, -1)

    # Moves the current block down
    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() is False or self.block_fits() is False:
            self.current_block.move(-1, 0)
            self.lock_block()

    # Locks the current block in place on the grid
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        # Check if the new block fits; if not, game over
        if self.block_fits() is False:
            self.game_over = True

    # Resets the game to its initial state
    def reset(self):
        self.grid.reset()
        self.blocks = [I(), J(), L(), O(), S(), T(), Z()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    # Checks if the current block fits within the grid
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) is False:
                return False
        return True

    # Rotates the current block
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() is False or self.block_fits() is False:
            self.current_block.undo_rotation()

    # Checks if the current block is inside the grid boundaries
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) is False:
                return False
        return True

    # Draws the grid and the current block on the screen
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)
