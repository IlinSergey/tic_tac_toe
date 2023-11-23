import pygame


pygame.init()

screen = pygame.display.set_mode(size=(600, 600))
pygame.display.set_caption('TIC TAC TO')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
screen.fill('White')

circle_image = pygame.image.load('images/circle.png')
cross_image = pygame.image.load('images/cross.png')

is_game_active = True
while is_game_active:
    pygame.draw.line(surface=screen, color='Black',
                     start_pos=(0, 200), end_pos=(600, 200),
                     width=5)
    pygame.draw.line(surface=screen, color='Black',
                     start_pos=(0, 400), end_pos=(600, 400),
                     width=5)
    pygame.draw.line(surface=screen, color='Black',
                     start_pos=(200, 0), end_pos=(200, 600),
                     width=5)
    pygame.draw.line(surface=screen, color='Black',
                     start_pos=(400, 0), end_pos=(400, 600),
                     width=5)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_active = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            figure = cross_image
            if 0 < position[0] < 200 and 0 < position[1] < 200:  # Поле 1
                screen.blit(source=figure, dest=(3, 3))
            elif 200 < position[0] < 400 and 0 < position[1] < 200:  # Поле 2
                screen.blit(source=figure, dest=(203, 3))
            elif 400 < position[0] < 600 and 0 < position[1] < 200:  # Поле 3
                screen.blit(source=figure, dest=(403, 3))
            elif 0 < position[0] < 200 and 200 < position[1] < 400:  # Поле 4
                screen.blit(source=figure, dest=(3, 203))
            elif 200 < position[0] < 400 and 200 < position[1] < 400:  # Поле 5
                screen.blit(source=figure, dest=(203, 203))
            elif 400 < position[0] < 600 and 200 < position[1] < 400:  # Поле 6
                screen.blit(source=figure, dest=(403, 203))
            elif 0 < position[0] < 200 and 400 < position[1] < 600:  # Поле 7
                screen.blit(source=figure, dest=(3, 403))
            elif 200 < position[0] < 400 and 400 < position[1] < 600:  # Поле 8
                screen.blit(source=figure, dest=(203, 403))
            elif 400 < position[0] < 600 and 400 < position[1] < 600:  # Поле
                screen.blit(source=figure, dest=(403, 403))
