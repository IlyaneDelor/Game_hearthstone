
import pygame


class Card:
    
    def __init__(self, name, attack, health, cost, shield, hidden, taunt, use, image, x, y):
        self.name = name
        self.attack = attack
        self.health = health
        self.cost = cost
        self.shield = shield
        self.hidden = hidden
        self.taunt = taunt
        self.use = use
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def __eq__(self, other):
        return (self.name == other.name and self.health == other.health and self.attack == other.attack and
                self.cost == other.cost and self.shield == other.shield and self.hidden == other.hidden and
                self.taunt == other.taunt)

    def print_card(self, display_mana=True):
        if self.shield != 0:
            shield = "S:" + str(self.shield)
        else:
            shield = ""

        if self.hidden != 0:
            hidden = "H"
        else:
            hidden = ""

        if self.taunt != 0:
            taunt = "T"
        else:
            taunt = ""
      

        if display_mana:
            print(self.name, "(", self.attack, "/", self.health, ") :",
                  self.cost, " ", shield, " ", hidden, " ", taunt)

        else:
            print(self.name, " ( ", self.attack, "/", self.health, ") ",
                  shield, " ", hidden, " ", taunt)

    def take_damage(self, damage):
        if self.shield > 0:
            self.shield -= damage
            self.health -= abs(self.shield)
        else:
            self.health -= damage

    def fight_card(self, card):
        self.hidden = 0
        self.use = 0
        
        print("Vous attaquez ", card.name, " (", card.attack, "|", card.health, ") avec ", self.name,
              " (", self.attack, "|", self.health, ")")
        card.take_damage(self.attack)
        self.take_damage(card.attack)
     
        

    def fight_attempt(self, player2, cardB):
        attackable = True
        for element in player2.field:
            if (element.taunt == 1 and element != cardB):
                attackable = False
                print("Vous ne pouvez pas attaquer cette carte, car ",
                      element.name, " a la capacité de provocation , TrashTalk !")
        if(cardB.hidden == 1):
            attackable = False
            print(
                "Ce monstre est camouflé danzs les gradin, vous ne pouvez pas l'attaquer !")
        if attackable:
            self.fight_card(cardB)
            return True
        else:
            return False
