from Game import Game
import pygame


pygame.init()
# Class Game


# Fenêtre du jeu

pygame.display.set_caption("Football Heartstone")
screen = pygame.display.set_mode((1850, 1080))

running = True

# Arrière-plan

background = pygame.image.load('assets/board.jpg')

# Charger Jeu

game = Game()


i = 0
# Boucle
while running and game.mbappe.health > 0 and game.grizou.health > 0:

    # Applique arrière plan
    screen.blit(background, (0, 0))

    # Image Mbappe

    # Image Mbappe
    screen.blit(game.mbappe.image, game.mbappe.rect)
    pygame.display.flip()
    screen.blit(game.grizou.image, game.grizou.rect)

    game.mbappe.player_turn(game.grizou, screen, background)

    if(game.grizou.health > 0):
        game.grizou.player_turn(game.mbappe, screen, background)

    # fermeture de fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            pygame.quit()
            print("Fermeture")

if game.mbappe.health <= 0:
    print(game.grizou.name, " Win !!!<3")
else:
    print(game.mbappe.name, " Win<333 Marque t'es penalty Enfoiré")
