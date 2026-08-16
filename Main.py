import Cards
import Player
import pygame
import sys
import random
import tkinter as tk

# Initialize Pygame
pygame.init()

# Screen setup
root = tk.Tk()
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()
root.destroy()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FUCKING TAKI YOU LIL BITCH")

# Clock to control frame rate
clock = pygame.time.Clock()
FPS = 60

# players
player1 = Player.player()

# im puting the things here 
exampleCard = Cards.TakiCard('red')
exampleCard2 = Cards.Plus2('yellow')
exampleCard3 = Cards.NumCard('red', 6)
takePile = Cards.TakePile.create_pile()
player1.addCard()
player1.addCard()
player1.addCard()



# Main Game Loop
running = True
while running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Game Logic / Updates
    # (Update positions, check collisions, etc.)

    # 3. Drawing
    screen.fill((0, 0, 0))  # Clear screen with background color
    
    # Draw elements here
    player1.drawDeck(screen)

    pygame.display.flip()  # Update the full display surface to the screen

    # Cap the frame rate
    clock.tick(FPS)

# Clean up and exit
pygame.quit()
sys.exit()
