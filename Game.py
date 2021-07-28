import pygame


from Player import Player
from Decks import *

# Class Game


class Game:

    def __init__(self):

        self.mbappe = Player("Cowboy Mbappé", France,
                             "assets/mbappe.png", 827, 725)
        self.grizou = Player("Grizou Black", France2,
                             "assets/grizou.png", 827, 105)
