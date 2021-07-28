import pygame
from Cards import Card

class magicCard(Card):

    def __init__(self,name, attack, health, cost, shield, hidden, taunt, use, image, x, y,nbpers,dmg_add,all_effect):
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
        self.nbpers = nbpers
        self.dmg_add = dmg_add
        self.all_effect = all_effect

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

        if self.nbpers != 0:
            nbpers = self.nbpers
        else:
            nbpers = self.nbpers

        if self.dmg_add != 0:
            dmg_add = "Y"
        else:
            dmg_add = "N"



        if display_mana:
            print("MAGIC : " + self.name, "(", self.attack, "/", self.health, ") :",
                  self.cost, " ", shield, " ", hidden, " ", taunt, " ",dmg_add, " ", nbpers)

        else:
            print("MAGIC : " + self.name, "(", self.attack, "/", self.health, ") :",
                  self.cost, " ", shield, " ", hidden, " ", taunt, " ",dmg_add, " ", nbpers)


    def magic_attempt(self, player2, cardB):
        if(self.dmg_add == 0):
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
                self.magic_use(cardB)
                return True
            else:
                return False
        else:
            self.magic_use(cardB)
            return True
           


    def magic_use(self,cardB):
        if self.dmg_add == 1 and self.all_effect ==0:
            cardB.attack += self.attack
            print("L'attaque de " + str(cardB.name) + " Passe à " + str(cardB.attack))


        if self.all_effect ==0 and self.dmg_add == 1 and self.attack>0 :
            cardB.health += self.attack
            print("La vie de " + str(cardB.name) + " Passe à " + str(cardB.health))
        
        if self.dmg_add == 0 and self.all_effect ==0 and self.attack>0 :
            cardB.health -= self.attack
            print("La vie de " + str(cardB.name) + " Passe à " + str(cardB.health))
        
        

            
