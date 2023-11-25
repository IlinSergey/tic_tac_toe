import pygame

from settings import VICTORIE_LINES, FIELDS
from utils import (check_win, computer_step, drow_figure, current_player)


pygame.init()

# Инициализация и отрисовка поля
screen = pygame.display.set_mode(size=(600, 600))
pygame.display.set_caption('TIC TAC TOE')

background = pygame.image.load('images/background.png')
screen.blit(source=background, dest=(0, 0))

circle_image = pygame.image.load('images/circle.png')
cross_image = pygame.image.load('images/cross.png')

font = pygame.font.Font('fonts/cuyabra-Regular.ttf', 60)
game_over_text = font.render('GAME OVER!!!', True, pygame.Color('red'))
win_text = {
    'X': font.render('Победа игрока "X"!', True, pygame.Color('red')),
    'O': font.render('Победа игрока "O"!', True, pygame.Color('red')),
    }

figures = {
    'X': cross_image,
    'O': circle_image,
}

current_figure = figures['O']



def change_figure():
    '''
    Меняет текущую фигуру (игрока)
    '''
    global current_figure
    if current_figure == figures['O']:
        current_figure = figures['X']
    elif current_figure == figures['X']:
        current_figure = figures['O']


is_game_active = True  # "Закрывает" окно с игрой
is_game_over = False  # Останавливает игру без закрытия окна

while is_game_active:
    pygame.display.update()
    for event in pygame.event.get():

        if current_figure == figures['X'] and not is_game_over:
            step = computer_step(fields=FIELDS)
            drow_figure(figure=current_figure, field=step, screen=screen)
            FIELDS[step] = current_player(current_figure, figures)
            change_figure()
            result = check_win(victorie_lines=VICTORIE_LINES, fields=FIELDS)
            if result:
                screen.blit(source=win_text[result], dest=(20, 270))
                is_game_over = True

        if event.type == pygame.QUIT:
            is_game_active = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if not is_game_over:
                if 0 < position[0] < 200 and 0 < position[1] < 200 and not FIELDS['1']:  # Поле 1
                    drow_figure(current_figure, field='1', screen=screen)
                    FIELDS['1'] = current_player(current_figure, figures)
                    change_figure()
                elif 200 < position[0] < 400 and 0 < position[1] < 200 and not FIELDS['2']:  # Поле 2
                    drow_figure(current_figure, field='2', screen=screen)
                    FIELDS['2'] = current_player(current_figure, figures)
                    change_figure()
                elif 400 < position[0] < 600 and 0 < position[1] < 200 and not FIELDS['3']:  # Поле 3
                    drow_figure(current_figure, field='3', screen=screen)
                    FIELDS['3'] = current_player(current_figure, figures)
                    change_figure()
                elif 0 < position[0] < 200 and 200 < position[1] < 400 and not FIELDS['4']:  # Поле 4
                    drow_figure(current_figure, field='4', screen=screen)
                    FIELDS['4'] = current_player(current_figure, figures)
                    change_figure()
                elif 200 < position[0] < 400 and 200 < position[1] < 400 and not FIELDS['5']:  # Поле 5
                    drow_figure(current_figure, field='5', screen=screen)
                    FIELDS['5'] = current_player(current_figure, figures)
                    change_figure()
                elif 400 < position[0] < 600 and 200 < position[1] < 400 and not FIELDS['6']:  # Поле 6
                    drow_figure(current_figure, field='6', screen=screen)
                    FIELDS['6'] = current_player(current_figure, figures)
                    change_figure()
                elif 0 < position[0] < 200 and 400 < position[1] < 600 and not FIELDS['7']:  # Поле 7
                    drow_figure(current_figure, field='7', screen=screen)
                    FIELDS['7'] = current_player(current_figure, figures)
                    change_figure()
                elif 200 < position[0] < 400 and 400 < position[1] < 600 and not FIELDS['8']:  # Поле 8
                    drow_figure(current_figure, field='8', screen=screen)
                    FIELDS['8'] = current_player(current_figure, figures)
                    change_figure()
                elif 400 < position[0] < 600 and 400 < position[1] < 600 and not FIELDS['9']:  # Поле 9
                    drow_figure(current_figure, field='9', screen=screen)
                    FIELDS['9'] = current_player(current_figure, figures)
                    change_figure()

                result = check_win(victorie_lines=VICTORIE_LINES, fields=FIELDS)
                if result:
                    screen.blit(source=win_text[result], dest=(20, 270))
                    is_game_over = True

                if all(FIELDS.values()) and not is_game_over:  # Проверка на количество свободных полей
                    screen.blit(source=game_over_text, dest=(20, 270))
                    is_game_over = True
