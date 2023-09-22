from sudokutools import valid, solve, find_empty, generate_board
from copy import deepcopy
from sys import exit
import pygame
import time
import random

pygame.init()


class Board:
    def __init__(self, window):
        """
        Инициализирует объект Board.
        :param window: Объект окна Pygame.
        """
        # Создайте новую доску судоку и создайте ее решенную версию.
        self.board = generate_board()
        self.solvedBoard = deepcopy(self.board)
        solve(self.solvedBoard)
        # Создайте двумерный список объектов Tile, представляющих доску судоку.
        self.tiles = [
            [Tile(self.board[i][j], window, i * 60, j * 60) for j in range(9)]
            for i in range(9)
        ]
        self.window = window

    def draw_board(self):
        """
        Рисует доску судоку в окне Pygame.
        """
        for i in range(9):
            for j in range(9):
                # Нарисовать вертикальные линии через каждые три столбца.
                if j % 3 == 0 and j != 0:
                    pygame.draw.line(
                        self.window,
                        (0, 0, 0),
                        (j // 3 * 180, 0),
                        (j // 3 * 180, 540),
                        4,
                    )
                # Нарисовать горизонтальные линии через каждые три ряда.
                if i % 3 == 0 and i != 0:
                    pygame.draw.line(
                        self.window,
                        (0, 0, 0),
                        (0, i // 3 * 180),
                        (540, i // 3 * 180),
                        4,
                    )
                # Нарисовать объект Tile на доске.
                self.tiles[i][j].draw((0, 0, 0), 1)

                # Отобразите значение плитки, если оно не равно 0 (пусто).
                if self.tiles[i][j].value != 0:
                    self.tiles[i][j].display(
                        self.tiles[i][j].value, (21 + j * 60, 16 + i * 60), (0, 0, 0)
                    )
        # Нарисовать горизонтальную линию внизу доски.
        pygame.draw.line(
            self.window,
            (0, 0, 0),
            (0, (i + 1) // 3 * 180),
            (540, (i + 1) // 3 * 180),
            4,
        )

    def deselect(self, tile):
        """
        Отменяет выбор всех плиток, кроме данной плитки.
        :param tile: Плитка, которая должна оставаться выделенной.
        :return: None
        """
        for i in range(9):
            for j in range(9):
                if self.tiles[i][j] != tile:
                    self.tiles[i][j].selected = False

    def redraw(self, keys, wrong, time):
        """
        Перерисовывает доску судоку в окне игры, выделяя выбранные,
        правильные и неправильные плитки,отображая текущий неправильный счетчик и время,
        а также отображая текущие ключи для каждой плитки.
        :param keys: Словарь, содержащий (x, y) в качестве ключей и потенциальные значения
        :param wrong: Текущий неправильный подсчет.
        :param time: Текущее время истекло.
        :return: None
        """
        # залейте окно белым цветом
        self.window.fill((255, 255, 255))
        # нарисовать доску судоку
        self.draw_board()
        for i in range(9):
            for j in range(9):
                if self.tiles[j][i].selected:
                    # выделить выбранные плитки зеленым цветом
                    self.tiles[j][i].draw((50, 205, 50), 4)
                elif self.tiles[i][j].correct:
                    # выделите правильные плитки темно-зеленым цветом
                    self.tiles[j][i].draw((34, 139, 34), 4)
                elif self.tiles[i][j].incorrect:
                    # выделите неправильные плитки красным цветом
                    self.tiles[j][i].draw((255, 0, 0), 4)

        if len(keys) != 0:
            for value in keys:
                # отображать потенциальные значения для каждой плитки
                self.tiles[value[0]][value[1]].display(
                    keys[value],
                    (21 + value[0] * 60, 16 + value[1] * 60),
                    (128, 128, 128),
                )

        if wrong > 0:
            # отображать текущий неправильный счетчик в виде значка «X» и числа
            font = pygame.font.SysFont("Bauhaus 93", 30)
            text = font.render("X", True, (255, 0, 0))
            self.window.blit(text, (10, 554))

            font = pygame.font.SysFont("Bahnschrift", 40)
            text = font.render(str(wrong), True, (0, 0, 0))
            self.window.blit(text, (32, 542))

        # отображать текущее прошедшее время в виде числа
        font = pygame.font.SysFont("Bahnschrift", 40)
        text = font.render(str(time), True, (0, 0, 0))
        self.window.blit(text, (388, 542))
        pygame.display.flip()  # update the game window

    def visualSolve(self, wrong, time):
        """
        Рекурсивно решает доску судоку визуально, выделяя правильные
        и неправильные плитки по мере их заполнения.
        :param wrong: Текущий неправильный подсчет.
        :param time: Текущее время истекло.
        :return: True, если доска успешно решена, в противном случае False.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        empty = find_empty(self.board)
        if not empty:
            return True

        for nums in range(9):
            if valid(self.board, (empty[0], empty[1]), nums + 1):
                # заполните текущую пустую плитку действительным числом
                self.board[empty[0]][empty[1]] = nums + 1
                self.tiles[empty[0]][empty[1]].value = nums + 1
                self.tiles[empty[0]][empty[1]].correct = True
                # задержка, чтобы замедлить анимацию решения
                pygame.time.delay(63)
                # перерисовать окно игры с обновленным полем
                self.redraw(
                    {}, wrong, time
                )

                if self.visualSolve(wrong, time):
                    return True


                self.board[empty[0]][empty[1]] = 0
                self.tiles[empty[0]][empty[1]].value = 0
                self.tiles[empty[0]][empty[1]].incorrect = True
                self.tiles[empty[0]][empty[1]].correct = False
                pygame.time.delay(63)
                self.redraw(
                    {}, wrong, time
                )

    def hint(self, keys):
        """
        Предоставляет подсказку, заполняя случайную пустую плитку правильным номером.
        :param keys: Словарь, содержащий (x, y) в качестве ключей и потенциальных значений
        :return: True, если подсказка успешно предоставлена, False, если доска уже решена.
        """
        while True:
            i = random.randint(0, 8)
            j = random.randint(0, 8)
            if self.board[i][j] == 0:
                if (j, i) in keys:
                    del keys[(j, i)]
                # заполните выбранную пустую плитку правильным номером
                self.board[i][j] = self.solvedBoard[i][j]
                self.tiles[i][j].value = self.solvedBoard[i][j]
                return True
            # доска уже решена, поэтому подсказок дать невозможно.
            elif self.board == self.solvedBoard:
                return False

class Tile:
    def __init__(
        self,
        value,
        window,
        x1,
        y1,
    ):
        """
        Инициализирует объект Tile.
        :param value: Значение, которое будет отображаться на плитке.
        :param window: Поверхность, на которой будет нарисована плитка.
        :param x1: Координата X верхнего левого угла плитки.
        :param y1: Координата Y верхнего левого угла плитки.
        """

        self.value = value
        self.window = window
        self.rect = pygame.Rect(x1, y1, 60, 60)
        self.selected = False
        self.correct = False
        self.incorrect = False

    def draw(self, color, thickness):
        """
        Рисовать плитку в окне с цветной рамкой.
        :param color: Значение цвета RGB границы.
        :param thickness: Толщина границы.
        :return: None
        """

        pygame.draw.rect(self.window, color, self.rect, thickness)

    def display(
        self,
        value,
        position,
        color,
    ):
        """
        Отображает значение плитки в центре плитки.
        :param value: Значение, которое будет отображаться.
        :param position: The (x, y) coordinates of the center of the Tile.
        :param color: The RGB color value of the text.
        :return: None.
        """

        font = pygame.font.SysFont("lato", 45)
        text = font.render(str(value), True, color)
        self.window.blit(text, position)

    def clicked(self, mousePos):
        """
        Проверяет, щелкнута ли мышью по плитке.
        :param mousePos: Координаты (x, y) мыши.
        :return: True, если щелкнуть плитку, в противном случае — False.
        """

        if self.rect.collidepoint(mousePos):
            self.selected = True
        return self.selected


def main():
    # Настройте окно pygame
    screen = pygame.display.set_mode((540, 590))
    screen.fill((255, 255, 255))
    pygame.display.set_caption("Sudoku Solver")
    icon = pygame.image.load("assets/thumbnail.png")
    pygame.display.set_icon(icon)

    # Отображение текста «Генерация случайной сетки» при создании случайной сетки.
    font = pygame.font.SysFont("Bahnschrift", 40)
    text = font.render("Generating", True, (0, 0, 0))
    screen.blit(text, (175, 245))

    font = pygame.font.SysFont("Bahnschrift", 40)
    text = font.render("Random Grid", True, (0, 0, 0))
    screen.blit(text, (156, 290))
    pygame.display.flip()

    # Инициализировать переменные
    wrong = 0
    board = Board(screen)
    selected = (-1, -1)
    keyDict = {}
    solved = False
    startTime = time.time()

    # Цикл, пока судоку не будет решена
    while not solved:
        # Получите прошедшее время и отформатируйте его для отображения в окне.
        elapsed = time.time() - startTime
        passedTime = time.strftime("%H:%M:%S", time.gmtime(elapsed))

        # Проверьте, решена ли судоку
        if board.board == board.solvedBoard:
            solved = True

        # Обработка событий
        for event in pygame.event.get():
            elapsed = time.time() - startTime
            passedTime = time.strftime("%H:%M:%S", time.gmtime(elapsed))
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                # Проверьте, нажата ли плитка
                mousePos = pygame.mouse.get_pos()
                for i in range(9):
                    for j in range(9):
                        if board.tiles[i][j].clicked(mousePos):
                            selected = (i, j)
                            board.deselect(board.tiles[i][j])
            elif event.type == pygame.KEYDOWN:
                # Обрабатывать нажатия клавиш
                if board.board[selected[1]][selected[0]] == 0 and selected != (-1, -1):
                    if event.key == pygame.K_1:
                        keyDict[selected] = 1

                    if event.key == pygame.K_2:
                        keyDict[selected] = 2

                    if event.key == pygame.K_3:
                        keyDict[selected] = 3

                    if event.key == pygame.K_4:
                        keyDict[selected] = 4

                    if event.key == pygame.K_5:
                        keyDict[selected] = 5

                    if event.key == pygame.K_6:
                        keyDict[selected] = 6

                    if event.key == pygame.K_7:
                        keyDict[selected] = 7

                    if event.key == pygame.K_8:
                        keyDict[selected] = 8

                    if event.key == pygame.K_9:
                        keyDict[selected] = 9
                    elif (
                        event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE
                    ):
                        if selected in keyDict:
                            board.tiles[selected[1]][selected[0]].value = 0
                            del keyDict[selected]
                    elif event.key == pygame.K_RETURN:
                        if selected in keyDict:
                            if (
                                keyDict[selected]
                                != board.solvedBoard[selected[1]][selected[0]]
                            ):
                                wrong += 1
                                board.tiles[selected[1]][selected[0]].value = 0
                                del keyDict[selected]


                            board.tiles[selected[1]][selected[0]].value = keyDict[
                                selected
                            ]
                            board.board[selected[1]][selected[0]] = keyDict[selected]
                            del keyDict[selected]

                # Обработка клавиши подсказки
                if event.key == pygame.K_h:
                    board.hint(keyDict)

                # Обработка клавиши пробела
                if event.key == pygame.K_SPACE:
                    # Отмените выбор всех плиток и очистите keyDict.
                    for i in range(9):
                        for j in range(9):
                            board.tiles[i][j].selected = False
                    keyDict = {}

                    # Решите судоку визуально и восстановите правильность всех плиток.
                    elapsed = time.time() - startTime
                    passedTime = time.strftime("%H:%M:%S", time.gmtime(elapsed))
                    board.visualSolve(wrong, passedTime)
                    for i in range(9):
                        for j in range(9):
                            board.tiles[i][j].correct = False
                            board.tiles[i][j].incorrect = False

                    solved = True

        board.redraw(keyDict, wrong, passedTime)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


main()
pygame.quit()
