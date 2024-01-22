# Importing necessary modules and classes
from colors import Colors
import pygame
from position import Position


# Base class for Tetris blocks
class Block:
    def __init__(self, id):
        # Unique identifier for the block
        self.id = id
        # Dictionary to store cell positions for different orientations
        self.cells = {}
        # Size of each cell in pixels
        self.cell_size = 30
        # Offset for the current row and column position of the block
        self.row_offset = 0
        self.column_offset = 0
        # Current rotation state of the block (default is 0)
        self.rotation_state = 0
        # Dictionary of colors for each block type
        self.colors = Colors.get_cell_colors()

    # Move the block by the specified number of rows and columns
    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    # Get the cell positions for the current block state
    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            # Apply the block's offset to each cell position
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    # Rotate the block clockwise
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    # Undo the last rotation
    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1

    # Draw the block on the given screen
    def draw(self, screen):
        tiles = self.get_cell_positions()
        for tile in tiles:
            # Create a rectangle for each cell and draw it with the block's color
            tile_rect = pygame.Rect(tile.column * self.cell_size,
                                    tile.row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
