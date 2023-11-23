import pygame


pygame.init()

# Инициализация и отрисовка поля
screen = pygame.display.set_mode(size=(600, 600))
pygame.display.set_caption('TIC TAC TO')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
background = pygame.image.load('images/background.png')
screen.blit(source=background, dest=(0, 0))

font = pygame.font.Font('fonts/cuyabra-Regular.ttf', 60)
text = font.render('Ходы закончилиcь!', True, pygame.Color('red'))

circle_image = pygame.image.load('images/circle.png')
cross_image = pygame.image.load('images/cross.png')

figures = {
    'X': cross_image,
    'O': circle_image,
}
figure = figures['O']

fields = dict()


is_game_active = True

while is_game_active:

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_active = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if len(fields) == 9:
                screen.blit(source=text, dest=(20, 270))
            if 0 < position[0] < 200 and 0 < position[1] < 200 and '1' not in fields:  # Поле 1
                screen.blit(source=figure, dest=(3, 3))
                fields['1'] = True
            elif 200 < position[0] < 400 and 0 < position[1] < 200 and '2' not in fields:  # Поле 2
                screen.blit(source=figure, dest=(203, 3))
                fields['2'] = True
            elif 400 < position[0] < 600 and 0 < position[1] < 200 and '3' not in fields:  # Поле 3
                screen.blit(source=figure, dest=(403, 3))
                fields['3'] = True
            elif 0 < position[0] < 200 and 200 < position[1] < 400 and '4' not in fields:  # Поле 4
                screen.blit(source=figure, dest=(3, 203))
                fields['4'] = True
            elif 200 < position[0] < 400 and 200 < position[1] < 400 and '5' not in fields:  # Поле 5
                screen.blit(source=figure, dest=(203, 203))
                fields['5'] = True
            elif 400 < position[0] < 600 and 200 < position[1] < 400 and '6' not in fields:  # Поле 6
                screen.blit(source=figure, dest=(403, 203))
                fields['6'] = True
            elif 0 < position[0] < 200 and 400 < position[1] < 600 and '7' not in fields:  # Поле 7
                screen.blit(source=figure, dest=(3, 403))
                fields['7'] = True
            elif 200 < position[0] < 400 and 400 < position[1] < 600 and '8' not in fields:  # Поле 8
                screen.blit(source=figure, dest=(203, 403))
                fields['8'] = True
            elif 400 < position[0] < 600 and 400 < position[1] < 600 and '9' not in fields:  # Поле 9
                screen.blit(source=figure, dest=(403, 403))
                fields['9'] = True

            if figure == figures['O']:
                figure = figures['X']
            elif figure == figures['X']:
                figure = figures['O']
