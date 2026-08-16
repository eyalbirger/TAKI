import Cards
import Player
import pygame
import sys
import random
#import tkinter 

# Initialize Pygame
pygame.init()

# Screen setup
#TK_SILENCE_DEPRECATION=1
#root = tkinter.Tk()
SCREEN_WIDTH = 800#root.winfo_screenwidth()
SCREEN_HEIGHT = 800#root.winfo_screenheight()
#root.destroy()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FUCKING TAKI YOU LIL BITCH")

# Clock to control frame rate
clock = pygame.time.Clock()
FPS = 60

# players
player1 = Player.player()
player2 = Player.player()

# piles
takePile = Cards.TakePile()
throwPile = Cards.ThrowPile()

for i in range (8):
  player1.addCard(takePile)
  player2.addCard(takePile)

throwPile.receive(takePile.take())


name1 = "player1"
name2 = "player2"
font = pygame.font.SysFont("Arial", 36, bold = True)


# Main Game Loop
takepile_rect = None
turn = random.choice([name1, name2])
running = True
while running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #now the fucking events
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos

            if takepile_rect and takepile_rect.collidepoint(event.pos):
                if turn == name1:
                    player1.addCard(takePile)
                    turn = name2
                elif turn == name2:
                    player2.addCard(takePile)
                    turn = name1

            else:
                clicked_card = player1.get_clicked_card(mouse_pos)
                if clicked_card:
                    top_card = throwPile.cards[-1] if throwPile.cards else None

                    if Cards.is_valid_play(clicked_card, top_card):
                        player1.deck.remove(clicked_card)
                        throwPile.receive(clicked_card)
                        

    # 2. Game Logic / Updates
    # (Update positions, check collisions, etc.)

    # 3. Drawing
    screen.fill((0, 0, 0))  # Clear screen with background color

    #this is the players names
    if turn == name1:
        text_surface1 = font.render(name1, True, (255, 255, 0))
        text_surface2 = font.render(name2, True, (255, 255, 255))
    elif turn == name2:
        text_surface1 = font.render(name1, True, (255, 255, 255))
        text_surface2 = font.render(name2, True, (255, 255, 0))

    text_rect1 = text_surface1.get_rect(center= (SCREEN_WIDTH/2, SCREEN_HEIGHT * 0.1))
    text_rect2 = text_surface2.get_rect(center= (SCREEN_WIDTH/2, SCREEN_HEIGHT * 0.9))

    screen.blit(text_surface1, text_rect1)
    screen.blit(text_surface2, text_rect2)

    
    # Draw elements here
    takepile_rect = Cards.draw_blank(screen, SCREEN_WIDTH * 0.4, SCREEN_HEIGHT/2)
    if throwPile.cards:
        Cards.draw_card(screen, throwPile.cards[-1], SCREEN_WIDTH*0.52, SCREEN_HEIGHT/2)

    player1.drawDeck(screen, 1)
    player2.drawDeck(screen, 2)

    pygame.display.flip()  # Update the full display surface to the screen

    # Cap the frame rate
    clock.tick(FPS)

# Clean up and exit
pygame.quit()
sys.exit()
