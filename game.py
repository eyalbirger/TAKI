import pygame
import random
import Cards

class game:
  def __init__(self, players):
    self.players = players
    self.turn_index = random.randint(1, 2)

    @property
    def currentTurn(self):
      return self.turn_index

    def switchTurn(self):
      if self.turn_index == 1:
        self.turn_index = 2
        return self.turn_index
      self.turn_index = 1
      return self.turn_index

    def dontSwitchTurns(self, clicked_card):
      open1 = False
      open2 = False

      if switchTurn() == 1:
        open1 = True
      else:
        open2 = True
      if not isinstance(clicked_card, Cards.TakiCard):
        if not isinstance(clicked_card, Cards.ChangeDirectionCard) or isinstance(clicked_card, Cards.PlusCard):
          open1 = False
          switchTurn()
        elif isinstance(clicked_card, Cards.ChangeDirectionCard) or isinstance(clicked_card, Cards.PlusCard):
          open2 = False

def switchTurn(turn):
      if turn == "player1":
        return "player2"
      return "player1"