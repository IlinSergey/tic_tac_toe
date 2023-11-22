import pygame


pygame.init()

screen = pygame.display.set_mode(size=(600, 600))
pygame.display.set_caption('TIC TAC TO')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

is_game_active = True

while is_game_active:

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_active = False
            pygame.quit()
