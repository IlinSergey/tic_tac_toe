from random import choice
from time import sleep

from pygame.surface import Surface


def check_win(victorie_lines: list[list[str]], fields: dict[str: bool | str]) -> str | bool:
    '''
    Проверяет существут ли выигрышная комбинация на поле
    Возвращает строковое представление выигрывшего знака либо
    False если выигрышной комбинации нет
    '''
    for line in victorie_lines:
        if fields[line[0]] == 'X' and fields[line[1]] == 'X' and fields[line[2]] == 'X':
            return 'X'
        elif fields[line[0]] == 'O' and fields[line[1]] == 'O' and fields[line[2]] == 'O':
            return 'O'
        else:
            False


def computer_step(fields: dict[str: bool | str]) -> str:
    '''
    Рандомно выберает свободное поле и возвращает его номер в str
    '''
    sleep(0.2)
    free_fields = [field for field in fields.keys() if fields[field] is False]
    choised_field = choice(free_fields)
    return choised_field


def current_player(figure: Surface, figures) -> str:
    '''
    На основании значения в переменной figure возвращает строковое
    представление текущей фигуры
    '''
    if figure == figures['O']:
        return 'O'
    else:
        return 'X'


def drow_figure(figure: Surface, field: str, screen: Surface) -> None:
    '''
    Отрисовывает фигуру на поле в необходимых координатах

    figure: Текущая фигура "X" или "O"
    field: Поле, для выбора координат для отрисовки фигуры
    '''
    coordinates = {
        '1': (3, 3),
        '2': (203, 3),
        '3': (403, 3),
        '4': (3, 203),
        '5': (203, 203),
        '6': (403, 203),
        '7': (3, 403),
        '8': (203, 403),
        '9': (403, 403),
    }
    screen.blit(source=figure, dest=coordinates[field])
