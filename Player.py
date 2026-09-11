import Cards
import pygame
#import tkinter as tk

#TK_SILENCE_DEPRECATION=1

#root = tk.Tk()
SCREEN_WIDTH = 800#root.winfo_screenwidth
SCREEN_HEIGHT = 800#root.winfo_screenheight
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#root.destroy()

class player:
  def __init__(self):
    self.deck = []
    

  def addCard(self, pile):
    drawn_card = pile.take()
    if drawn_card:
        self.deck.append(drawn_card)
    return None

  def drawDeck(self, surface, playernum):
    if not self.deck:
      return None

    cards_width = 40
    if playernum == 1:
      y = SCREEN_HEIGHT*0.75
    else:
      y = SCREEN_HEIGHT*0.25

    length = len(self.deck) * cards_width
    startPos =  SCREEN_WIDTH / 2 - (length / 2)

    for count, card in enumerate(self.deck):
      x = startPos + (count * cards_width)
      Cards.draw_card(surface, card,  x ,y)

  def colorMatch(self, clicked_card):
    for i in self.deck:
      if str(clicked_card.color) == str(i.color):
        return True
    return False

  def get_clicked_card(self, mouse_pos):
    for card in reversed(self.deck):
      if hasattr(card, 'rect') and card.rect and card.rect.collidepoint(mouse_pos):
        return card

    return None

  