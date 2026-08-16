import Cards
import pygame
import tkinter as tk


root = tk.Tk()
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
root.destroy()

class player:
  def __init__(self):
    self.deck = []
    

  def addCard(self):
    self.deck.append(Cards.TakePile.take())
    return None

  def drawDeck(self, surface):
    if not self.deck:
      return

    cards_width = 40
    y = SCREEN_HEIGHT*0.75

    length = len(self.deck) * cards_width
    startPos =  SCREEN_WIDTH / 2 - (length / 2)

    for count, card in enumerate(self.deck):
      x = startPos + (count * cards_width)
      Cards.draw_card(surface, card.color, card, x ,y)
    return None