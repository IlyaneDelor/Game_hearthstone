from magicCards import magicCard
from pygame import display
from Decks import *
import pygame

from Cards import Card


class Player:
    def __init__(self, name, deck, image, x, y):
        self.name = name
        self.health = 30
        self.mana = 0
        self.turn_mana = 0
        self.max_mana = 10
        self.hand = []
        self.field = []
        self.deck = deck
        self.cemetery = []
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def take_damage(self, card):
        self.health -= card.attack

    def pickUp(self, screen, image, rectt, player2, background):

        self.hand.append(self.deck[0])
        del self.deck[0]
        self.display_init(screen, image, rectt, player2, background)

    def turn_message(self):
        print("C'est à votre tour, ", self.name,
              " ! Il vous reste ", self.health, " PV")

    def initiate_mana(self, screen, image, rectt, player2, background):
        if self.turn_mana < self.max_mana:
            self.turn_mana += 1
        self.mana = self.turn_mana
        self.display_init(screen, image, rectt, player2, background)

    def wake_cards(self):
        for element in self.field:
            element.use = 1

    def phase_invoke_cards(self, screen, background, image, rectt, player2):
        arret = 0
        on = 0
        i = 0
     

        print(
            "Voici les serviteurs présents dans votre main. Montant de mana : ", self.mana)
        while arret != 1:
          

            

            for e in pygame.event.get():
                if e.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    print("Coordone X" + str(mx))
                    print("Coordone y" + str(my))
                    self.display_init(
                        screen, image, rectt, player2, background)
                    test = 0

                    for element in self.hand:
                        test += 1
                        if(mx+50 > element.rect.x > mx-50) and (my+50 > element.rect.y > my-50):
                            

                            print("-(", i, ")", end=' ')
                            element.print_card()
                            card = element
                            print("test : " + str(test))

                            if on == 0:
                               
                                print("tessssst" + str(test))
                                rect = pygame.Surface((175, 235))
                                rect.set_alpha(60)
                                rect.fill((255, 255, 255))
                                screen.blit(
                                    rect, (element.rect.x, element.rect.y))

                                on = 1

                                pygame.display.flip()

                            elif(mx+50 > element.rect.x > mx-50) and (my+50 > element.rect.y > my-50):
                              

                                screen.blit(
                                    rect, (element.rect.x, element.rect.y))
                                pygame.display.flip()

                    if (my > 245 and my < 700 and on == 1)   :
                        
                        print("name , cost : " +str(card.name) , str(card.cost))
                        
                       
                        

                        on = 0
                        if self.mana >= card.cost:

                          
                            
                            if("magicCard" == type(card).__name__):
                               
    
                                on =0
                                if(card.dmg_add ==0):
                                    print("Attack")

                                    for element in player2.field:
                                        if(mx+100 > element.rect.x > mx-100) and (my+100 > element.rect.y > my-100):
                                            if on == 0:
                                              
                                                card.magic_attempt(player2,element)
                                                self.mana -= card.cost
                                                del self.hand[test-2]
                                            if(mx+100 > player2.rect.x > mx-100) and (my+100 > player2.rect.y > my-100) and on == 0 and card.dmg_add == 0:
                                                card.magic_attempt(player2,player2)
                                                del self.hand[test-2]
                                    
                                        else:
                                            print("Selectionner un footballer")        
                                    self.display_init(
                                        screen, image, rectt, player2, background)

                                else:
                                    for element in self.field:
                                        if(mx+100 > element.rect.x > mx-100) and (my+100 > element.rect.y > my-100):
                                            if on == 0:
                                                card.magic_attempt(player2,element)
                                                self.mana -= card.cost
                                              
                                                del self.hand[test-1]
                                            if(mx+100 > self.rect.x > mx-100) and (my+100 > self.rect.y > my-100) and on == 0 and self.dmg_add == 0:
                                                card.magic_attempt(player2,player2)
                                                del self.hand[test-1]
                                    
                                        else:
                                            print("Selectionner un footballer")  

                                    self.display_init(
                                        screen, image, rectt, player2, background)      



                            else: 
                                self.mana -= card.cost
                                self.field.append(card)
                                print("Vous avez posé ", card.name)
                             
                            
                                print(str(test))
                                del self.hand[test-1]
                                test = 0

                                pygame.display.flip()
                                self.display_init(
                                    screen, image, rectt, player2, background)
                        else:
                            print("Pas assez de mana ")

                    if(1550 > mx > 1350):
                        if(550 > my > 450):
                            arret = 1
                            break
                        



    def phase_attack(self, screen, image, rectt, player2, background):
        print("Phase d'attaque !")
        on = 0
        arret = 0
        while arret != 1:
            for e in pygame.event.get():
                if e.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    print("Coordone X" + str(mx))
                    print("Coordone Y" + str(my))

                    for element in self.field:
                        if(mx+100 > element.rect.x > mx-100) and (my+100 > element.rect.y > my-100):

                            rect = pygame.Surface(
                                (175, 235))
                            rect.set_alpha(60)
                            rect.fill((255, 255, 255))
                            element.print_card()

                            screen.blit(
                                rect, (element.rect.x, element.rect.y))
                            on = 1
                            cardA = element
                            pygame.display.flip()

                    if(1550 > mx > 1350):
                        if(550 > my > 450):
                            arret = 1
                            break

                    for element in player2.field:
                        if(mx+100 > element.rect.x > mx-100) and (my+100 > element.rect.y > my-100):
                            if on == 1:
                                if cardA.use == 1:
                                    cardA.fight_attempt(player2, element)

                                    print(str(cardA.health))
                                    print(str(element.health))

                                    self.display_init(
                                        screen, image, rectt, player2, background)

                                else:
                                    print("Le footballeur est sur le banc")

                            else:
                                print("Selectionner un footballer avant")
                        else:
                            print("Le footballeur est sur le banc")

                    if(mx+50 > player2.rect.x > mx-50) and (my+50 > player2.rect.y > my-50):

                        if cardA.use == 1:
                            player2.health -= cardA.attack
                            cardA.use = 0
                            self.display_init(
                                screen, image, rectt, player2, background)

                            '''self.clean_after()'''

                        else:
                            print("Votre joueur est sur le Banc ")


    def clean_after(self):
        print("Morts ", self.name, " : ")
        for element in self.field:
            if element.health == 0:
                print("-", element.name)
        i = 0
        while i < len(self.field):
            if self.deck[i].health == 0:
                self.cemetery.append(self.deck[i])
                del self.deck[i]
                while self.deck[i].health == 0:
                    self.cemetery.append(self.deck[i])
                    del self.deck[i]
            i += 1

    def display_init(self, screen, image, rectt, player2, background):

        screen.blit(background, (0, 0))
        screen.blit(image, rectt)

        screen.blit(player2.image, player2.rect)

        police = pygame.font.SysFont("monospace", 17)

        image_health = police.render(
            str(self.health) + " / 30", 1, (255, 255, 255))

        image_health2 = police.render(
            str(player2.health) + " / 30", 1, (255, 255, 255))

        image_mana = police.render(
            str(self.mana) + " / 10", 1, (255, 255, 255))
        image_mana2 = police.render(
            str(player2.mana) + " / 10", 1, (255, 255, 255))
        if(self.name == "Cowboy Mbappé"):
            screen.blit(image_mana, (1185, 980))
            screen.blit(image_mana2, (1145, 62))
        else:
            screen.blit(image_mana2, (1185, 980))
            screen.blit(image_mana, (1145, 62))

        screen.blit(image_health, (self.rect.x, self.rect.y))

        screen.blit(image_health2, (player2.rect.x, player2.rect.y))

        if(self.name == "Cowboy Mbappé"):
            for i in range(len(self.field)):
                if self.field[i].health <= 0:
                    del self.field[i]
                else:
                    self.field[i].image = pygame.transform.scale(
                        self.field[i].image, (160, 220))
                    self.field[i].rect.x = 600 + (i * 175)
                    self.field[i].rect.y = 525

                    screen.blit(
                        self.field[i].image, (self.field[i].rect.x, 525))

            for i in range(len(player2.field)):
                if player2.field[i].health <= 0:
                    del player2.field[i]
                else:
                    player2.field[i].image = pygame.transform.scale(
                        player2.field[i].image, (160, 220))
                    player2.field[i].rect.x = 600 + (i * 175)
                    player2.field[i].rect.y = 250

                    screen.blit(
                        player2.field[i].image, (player2.field[i].rect.x, player2.field[i].rect.y))

            for i in range(len(self.hand)):

                self.hand[i].image = pygame.transform.scale(
                    self.hand[i].image, (175, 235))
                self.hand[i].rect.x = (i * 175)
                screen.blit(
                    self.hand[i].image, self.hand[i].rect)
            for i in range(len(player2.hand)):

                player2.hand[i].image = pygame.transform.scale(
                    player2.hand[i].image, (175, 235))
                player2.hand[i].rect.x = (i * 175)
                player2.hand[i].rect.y = 50

                screen.blit(
                    player2.hand[i].image, player2.hand[i].rect)
        else:

            for i in range(len(player2.field)):
                if player2.field[i].health <= 0:
                    del player2.field[i]
                else:
                    player2.field[i].image = pygame.transform.scale(
                        player2.field[i].image, (160, 220))
                    player2.field[i].rect.x = 600 + (i * 175)
                    player2.field[i].rect.y = 525

                    screen.blit(
                        player2.field[i].image, (player2.field[i].rect.x, 525))

            for i in range(len(self.field)):
                if self.field[i].health <= 0:
                    del self.field[i]
                else:
                    self.field[i].image = pygame.transform.scale(
                        self.field[i].image, (160, 220))
                    self.field[i].rect.x = 600 + (i * 175)
                    self.field[i].rect.y = 250
                    screen.blit(
                        self.field[i].image, (self.field[i].rect.x, 250))

            for i in range(len(player2.hand)):

                player2.hand[i].image = pygame.transform.scale(
                    player2.hand[i].image, (175, 235))
                player2.hand[i].rect.x = (i * 175)
                screen.blit(
                    player2.hand[i].image, player2.hand[i].rect)
            for i in range(len(self.hand)):

                self.hand[i].image = pygame.transform.scale(
                    self.hand[i].image, (175, 235))
                self.hand[i].rect.x = (i * 175)
                self.hand[i].rect.y = 50

                screen.blit(
                    self.hand[i].image, self.hand[i].rect)

        pygame.display.flip()

    def player_turn(self, player2, screen, background):

        self.turn_message()
        print("Terrain adverse : ")
        for element in player2.field:
            element.print_card(False)
        print("------------------------------------------------")
        print("Votre terrain")
        for element in self.field:
            element.print_card(False)
        print("------------------------------------------------")
        self.wake_cards()
        self.pickUp(screen, self.image, self.rect, player2, background)
        self.initiate_mana(screen, self.image, self.rect, player2, background)
        self.phase_invoke_cards(
            screen, background, self.image, self.rect, player2)
        self.phase_attack(screen, self.image, self.rect, player2, background)
