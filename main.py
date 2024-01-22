# Importing necessary modules and classes
import pygame, sys
from game import Game
from colors import Colors

# Initialize the Pygame library
pygame.init()

# Set up fonts and text for game over message
title_font = pygame.font.Font(None, 60)
font = pygame.font.Font(None, 25)
game_over_text = title_font.render("GAME OVER", True, Colors.white)
try_again_text = font.render("Press any key to restart", True, Colors.white)

# Create the game window
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

# Set up the game clock
clock = pygame.time.Clock()

# Create a new instance of the Game class
game = Game()

# Set up a custom event for game updates
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

# Main game loop
while True:
    # Handle Pygame events
    for event in pygame.event.get():
        # Quit the game if the window is closed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Check for keyboard input
        if event.type == pygame.KEYDOWN:
            # Restart the game if it's over
            if game.game_over is True:
                game.game_over = False
                screen.fill(Colors.black)
                game.reset()
            # Move the block based on key input
            if event.key == pygame.K_LEFT and game.game_over is False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over is False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over is False:
                game.move_down()
            if event.key == pygame.K_UP and game.game_over is False:
                game.rotate()
        # Game update event for moving the block down automatically
        if event.type == GAME_UPDATE and game.game_over is False:
            game.move_down()

    # Check if the game is over
    if game.game_over is True:
        # Display game over message and instructions to restart
        screen.fill(Colors.dark_blue)
        screen.blit(game_over_text, (25, 250, 0, 0)) 
        screen.blit(try_again_text, (50, 300, 0, 0))
    else:
        # Draw the current state of the game
        game.draw(screen)

    # Update the display
    pygame.display.update()
    # Set the frame rate to 60 frames per second
    clock.tick(60)
