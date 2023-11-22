import pygame


pygame.init()

screen = pygame.display.set_mode(size=(600, 600))
pygame.display.set_caption('TIC TAC TO')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)


is_game_active = True
while is_game_active:
    pygame.draw.line(surface=screen, color='White',
                     start_pos=(0, 198), end_pos=(600, 198),
                     width=5)
    pygame.draw.line(surface=screen, color='White',
                     start_pos=(0, 396), end_pos=(600, 396),
                     width=5)
    pygame.draw.line(surface=screen, color='White',
                     start_pos=(198, 0), end_pos=(198, 600),
                     width=5)
    pygame.draw.line(surface=screen, color='White',
                     start_pos=(396, 0), end_pos=(396, 600),
                     width=5)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_active = False
            pygame.quit()
