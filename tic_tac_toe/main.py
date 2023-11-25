from random import choice

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
text = font.render('GAME OVER!!!', True, pygame.Color('red'))
win_text = {
    'X': font.render('Победа игрока "X"!', True, pygame.Color('red')),
    'O': font.render('Победа игрока "O"!', True, pygame.Color('red')),
    }

circle_image = pygame.image.load('images/circle.png')
cross_image = pygame.image.load('images/cross.png')

victories_lines = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['1', '4', '7'],
    ['2', '5', '8'],
    ['3', '6', '9'],
    ['1', '5', '9'],
    ['3', '5', '7'],
]

figures = {
    'X': cross_image,
    'O': circle_image,
}

figure = figures['O']

fields = {
    '1': False,
    '2': False,
    '3': False,
    '4': False,
    '5': False,
    '6': False,
    '7': False,
    '8': False,
    '9': False,
}


def check_win() -> str | bool:
    for line in victories_lines:
        if fields[line[0]] == 'X' and fields[line[1]] == 'X' and fields[line[2]] == 'X':
            return 'X'
        elif fields[line[0]] == 'O' and fields[line[1]] == 'O' and fields[line[2]] == 'O':
            return 'O'
        else:
            False


def current_player(figure) -> str:
    if figure == figures['O']:
        return 'O'
    else:
        return 'X'


def computer_step() -> str:
    free_fields = [field for field in fields.keys() if fields[field]]
    step = choice(free_fields)
    return step


def drow_figure():
    pass


def change_figure():
    global figure
    if figure == figures['O']:
        figure = figures['X']
    elif figure == figures['X']:
        figure = figures['O']


is_game_active = True

while is_game_active:

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            is_game_active = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()

            if 0 < position[0] < 200 and 0 < position[1] < 200 and not fields['1']:  # Поле 1
                screen.blit(source=figure, dest=(3, 3))
                fields['1'] = current_player(figure)
                change_figure()
            elif 200 < position[0] < 400 and 0 < position[1] < 200 and not fields['2']:  # Поле 2
                screen.blit(source=figure, dest=(203, 3))
                fields['2'] = current_player(figure)
                change_figure()
            elif 400 < position[0] < 600 and 0 < position[1] < 200 and not fields['3']:  # Поле 3
                screen.blit(source=figure, dest=(403, 3))
                fields['3'] = current_player(figure)
                change_figure()
            elif 0 < position[0] < 200 and 200 < position[1] < 400 and not fields['4']:  # Поле 4
                screen.blit(source=figure, dest=(3, 203))
                fields['4'] = current_player(figure)
                change_figure()
            elif 200 < position[0] < 400 and 200 < position[1] < 400 and not fields['5']:  # Поле 5
                screen.blit(source=figure, dest=(203, 203))
                fields['5'] = current_player(figure)
                change_figure()
            elif 400 < position[0] < 600 and 200 < position[1] < 400 and not fields['6']:  # Поле 6
                screen.blit(source=figure, dest=(403, 203))
                fields['6'] = current_player(figure)
                change_figure()
            elif 0 < position[0] < 200 and 400 < position[1] < 600 and not fields['7']:  # Поле 7
                screen.blit(source=figure, dest=(3, 403))
                fields['7'] = current_player(figure)
                change_figure()
            elif 200 < position[0] < 400 and 400 < position[1] < 600 and not fields['8']:  # Поле 8
                screen.blit(source=figure, dest=(203, 403))
                fields['8'] = current_player(figure)
                change_figure()
            elif 400 < position[0] < 600 and 400 < position[1] < 600 and not fields['9']:  # Поле 9
                screen.blit(source=figure, dest=(403, 403))
                fields['9'] = current_player(figure)
                change_figure()

            if len(fields) > 5:  # Проверка выигрыша
                result = check_win()
                if result:
                    screen.blit(source=win_text[result], dest=(20, 270))

            if all(fields.values()):  # Проверка на кроичество свободных полей
                screen.blit(source=text, dest=(20, 270))
