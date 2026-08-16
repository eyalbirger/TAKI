import random
import pygame

COLOR_PALETTE = ('red', 'blue', 'green', 'yellow')

class Card:

    def __init__(self, color, val):
        self.color = color
        self.val = str(val)
        self.rect = pygame.Rect(0, 0, 80, 120)


class NumCard(Card):

    def __init__(self, color, num):
        super().__init__(color, num)
        self.num = num


#special cards
class PlusCard(Card):

    def __init__(self, color):
        super().__init__(color, "+")


class ChangeDirectionCard(Card):

    def __init__(self, color, clockwise=True):
        super().__init__(color, "DIR")
        self.clockwise = clockwise

    def switch_direction(self):
        self.clockwise = not self.clockwise
        return self.clockwise


class TakiCard(Card):

    def __init__(self, color, val = "TAKI"):
        super().__init__(color, val)
        self.open = True

    def open_and_close(self):
      self.open = not self.open
      return open


class Plus2(Card):

    def __init__(self, color, val="+2"):
        super().__init__(color, "+2")


class SuperTakiCard(TakiCard):
    
    def __init__(self, color, val ="STAKI"):
        super().__init__(color, "STAKI")

class KingCard(Card):
    def __init__(self, color):
        super().__init__(color, "KING")

class BackOfTheCard(Card):
    def __init__(self, color, val = "empty"):
        super().__init__("grey", val)

      

class TakePile:

    def __init__(self):
        self.cards = self.create_pile()

    #creating the deck
    @staticmethod
    def create_pile():
        fullpile = []
        for color in COLOR_PALETTE:
            for i in range(1, 10):  
                fullpile.append(NumCard(color, i))

            for j in range(2):
                fullpile.append(PlusCard(color))
                fullpile.append(Plus2(color))
                fullpile.append(ChangeDirectionCard(color))
                fullpile.append(TakiCard(color))

        fullpile.append(KingCard("green"))
        fullpile.append(SuperTakiCard("red"))
        fullpile.append(KingCard("blue"))
        fullpile.append(SuperTakiCard("yellow"))

        random.shuffle(fullpile)
        return fullpile

    def take(self):
        if self.cards:
            return self.cards.pop()
        return None

    def isEmpty(self):
        if len(self.cards) == 0:
            return True
        return False


class ThrowPile:

    def __init__(self):
        self.cards = []

    def receive(self, card):
        self.cards.append(card)

# for game logic
def draw_card(surface, card, x, y, width = 40, height = 60):
  CARDCOLORS = {
      'red': (255, 0, 0),
      'blue': (0, 0, 255),
      'green': (0, 255, 0),
      'yellow': (240, 200, 0),
      'colorless': (60, 60, 60)
  }

  bg_color = CARDCOLORS.get(card.color, (150, 150, 150))
  card_rect = pygame.Rect(x, y, width, height)
  card.rect = card_rect

  pygame.draw.rect(surface, bg_color, card_rect, border_radius = 8) # oh yeah i need to draw the fucking rectangle

  font = pygame.font.SysFont("arial", 18, bold = True)
  text_surface = font.render(card.val, True, (255, 255, 255)) # the true is for making the text smoother and who tf new it was possible like what is that 
  text_rect = text_surface.get_rect(center = card_rect.center)

  surface.blit(text_surface, text_rect)