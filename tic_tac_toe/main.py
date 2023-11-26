import pygame

from settings import (VICTORIE_LINES, FIELDS, CIRCLE_IMAGE, GAME_OVER_TEXT,
                      CROSS_IMAGE, BACKGROUND_IMAGE, FONT, FONT_SIZE)
from utils import check_win, computer_step, drow_figure


pygame.init()

# Инициализация и отрисовка поля
screen = pygame.display.set_mode(size=(600, 600))  # Размер экрана
pygame.display.set_caption('TIC TAC TOE')  # Заголовок

background = pygame.image.load(BACKGROUND_IMAGE)  # Загрузка фонового изображения
screen.blit(source=background, dest=(0, 0))  # Отрисовка фонового изображения

#  Загрузка изображений фигур
circle_image = pygame.image.load(CIRCLE_IMAGE)
cross_image = pygame.image.load(CROSS_IMAGE)

#  Привязка изображений с фигурами к их строковому аналогу
figures = {
    'X': cross_image,
    'O': circle_image,
}


#  Загрузка шрифта и текст для отображений
font = pygame.font.Font(FONT, FONT_SIZE)
game_over_text = font.render(GAME_OVER_TEXT, True, pygame.Color('red'))
win_text = {
    'X': font.render('Победа игрока "X"!', True, pygame.Color('red')),
    'O': font.render('Победа игрока "O"!', True, pygame.Color('red')),
    }

#  Список игроков и их фигуры
players = {
    'user': 'X',
    'computer': 'O',
}


# Право первого хода, переключение игроков через переменную
current_figure = 'user'


def change_player() -> None:
    '''
    Смена игрока
    '''
    global current_figure
    if current_figure == 'user':
        current_figure = 'computer'
    elif current_figure == 'computer':
        current_figure = 'user'


def main():
    is_game_active = True  # "Закрывает" окно с игрой
    is_game_over = False  # Останавливает игру без закрытия окна

    while is_game_active:
        pygame.display.update()
        for event in pygame.event.get():

            figure = figures[players[current_figure]]

            if current_figure == 'computer' and not is_game_over:
                step = computer_step(fields=FIELDS)
                drow_figure(figure=figure, field=step, screen=screen)
                FIELDS[step] = players[current_figure]
                change_player()
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
                        drow_figure(figure, field='1', screen=screen)
                        FIELDS['1'] = players[current_figure]
                        change_player()
                    elif 200 < position[0] < 400 and 0 < position[1] < 200 and not FIELDS['2']:  # Поле 2
                        drow_figure(figure, field='2', screen=screen)
                        FIELDS['2'] = players[current_figure]
                        change_player()
                    elif 400 < position[0] < 600 and 0 < position[1] < 200 and not FIELDS['3']:  # Поле 3
                        drow_figure(figure, field='3', screen=screen)
                        FIELDS['3'] = players[current_figure]
                        change_player()
                    elif 0 < position[0] < 200 and 200 < position[1] < 400 and not FIELDS['4']:  # Поле 4
                        drow_figure(figure, field='4', screen=screen)
                        FIELDS['4'] = players[current_figure]
                        change_player()
                    elif 200 < position[0] < 400 and 200 < position[1] < 400 and not FIELDS['5']:  # Поле 5
                        drow_figure(figure, field='5', screen=screen)
                        FIELDS['5'] = players[current_figure]
                        change_player()
                    elif 400 < position[0] < 600 and 200 < position[1] < 400 and not FIELDS['6']:  # Поле 6
                        drow_figure(figure, field='6', screen=screen)
                        FIELDS['6'] = players[current_figure]
                        change_player()
                    elif 0 < position[0] < 200 and 400 < position[1] < 600 and not FIELDS['7']:  # Поле 7
                        drow_figure(figure, field='7', screen=screen)
                        FIELDS['7'] = players[current_figure]
                        change_player()
                    elif 200 < position[0] < 400 and 400 < position[1] < 600 and not FIELDS['8']:  # Поле 8
                        drow_figure(figure, field='8', screen=screen)
                        FIELDS['8'] = players[current_figure]
                        change_player()
                    elif 400 < position[0] < 600 and 400 < position[1] < 600 and not FIELDS['9']:  # Поле 9
                        drow_figure(figure, field='9', screen=screen)
                        FIELDS['9'] = players[current_figure]
                        change_player()

                    result = check_win(victorie_lines=VICTORIE_LINES, fields=FIELDS)
                    if result:
                        screen.blit(source=win_text[result], dest=(20, 270))
                        is_game_over = True

                    if all(FIELDS.values()) and not is_game_over:  # Проверка на количество свободных полей
                        screen.blit(source=game_over_text, dest=(20, 270))
                        is_game_over = True


if __name__ == '__main__':
    main()
