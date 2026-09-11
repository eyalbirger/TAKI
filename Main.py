import Cards
import Player
import pygame
import sys
import random
import game as gm





    

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


while not isinstance(takePile.cards[-1], Cards.NumCard):
    random.shuffle(takePile.cards)

throwPile.receive(takePile.take())


name1 = "Player1"
name2 = "Player2"

font = pygame.font.SysFont("Arial", 36, bold = True)

# Main Game Loop
takepile_rect = None

names = (name1, name2)
turn = random.choice(names)

takiopen = False
plus2Counter = 0


twoOrMoreCards = (Cards.TakiCard, 
                  Cards.PlusCard, 
                  Cards.ChangeDirectionCard, 
                  Cards.KingCard, 
                  Cards.SuperTakiCard)

running = True
while running:
    if turn == name1:
        current_player = player1
        next_turn = name2
    else:
        current_player = player2
        next_turn = name1
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        #now the fucking events
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos

            close_rect = pygame.Rect(SCREEN_WIDTH * 0.1 - 40, SCREEN_HEIGHT/2-20, 80, 40)
            if takiopen and close_rect.collidepoint(mouse_pos):
                takiopen = False
                turn = next_turn
                continue
            
            if takepile_rect and takepile_rect.collidepoint(event.pos):
                if plus2Counter > 0:
                    for i in range (plus2Counter):
                        current_player.addCard(takePile)
                    plus2Counter = 0
                else:
                    current_player.addCard(takePile)
                if takiopen:
                    takiopen = False
                turn = next_turn

            else:
            
                clicked_card = current_player.get_clicked_card(mouse_pos)
                if clicked_card:
                    top_card = throwPile.cards[-1] if throwPile.cards else None
                    if plus2Counter > 0 and not isinstance(clicked_card, Cards.Plus2):
                        continue
                    

                    if Cards.is_valid_play(clicked_card, top_card):
                        current_player.deck.remove(clicked_card)
                        throwPile.receive(clicked_card)

                        # taki
                        if isinstance(clicked_card, (Cards.SuperTakiCard, Cards.TakiCard)):
                            takiopen = True
                            if not current_player.colorMatch(throwPile.cards[-1]):
                               takiopen = False
                               turn = next_turn

                        # +2
                        elif isinstance(clicked_card, Cards.Plus2):
                            plus2Counter += 2
                            if takiopen and not current_player.colorMatch(throwPile.cards[-1]):
                                takiopen = False
                            turn = next_turn

                        else:
                            if not takiopen and not isinstance (clicked_card, (Cards.ChangeDirectionCard, Cards.PlusCard)):
                                turn = next_turn

                        

                            

                                

    # 2. Game Logic / Updates
    # (Update positions, check collisions, etc.)
    
    # 3. Drawing
    screen.fill((0, 0, 0))  # Clear screen with background color

    #this is the players names
    if turn == name2:
        text_surface1 = font.render(name1, True, (255, 255, 0))
        text_surface2 = font.render(name2, True, (255, 255, 255))
    elif turn == name1:
        text_surface1 = font.render(name1, True, (255, 255, 255))
        text_surface2 = font.render(name2, True, (255, 255, 0))

    text_rect1 = text_surface1.get_rect(center= (SCREEN_WIDTH/2, SCREEN_HEIGHT * 0.1))
    text_rect2 = text_surface2.get_rect(center= (SCREEN_WIDTH/2, SCREEN_HEIGHT * 0.9))


    if takiopen:
        close_text = font.render("Close", True, (255, 255, 255))
    else:
        close_text = font.render("Close", True, (0, 0, 0))
    close_rect = close_text.get_rect(center= (SCREEN_WIDTH * 0.1, SCREEN_HEIGHT/2))

    screen.blit(text_surface1, text_rect1)
    screen.blit(text_surface2, text_rect2)
    screen.blit(close_text, close_rect)

    
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
