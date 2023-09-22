from random import randint, shuffle


def print_board(board):
    """
    Распечать доску судоку.
    :param board: Доска судоку 9x9, представленная в виде списка целых чисел.
    :return: None.
    """

    board_string = ""
    for i in range(9):
        for j in range(9):
            board_string += str(board[i][j]) + " "
            if (j + 1) % 3 == 0 and j != 0 and j + 1 != 9:
                board_string += "| "

            if j == 8:
                board_string += "\n"

            if j == 8 and (i + 1) % 3 == 0 and i + 1 != 9:
                board_string += "- - - - - - - - - - - \n"
    print(board_string)


def find_empty(board):
    """
    Найти пустую ячейку на доске судоку.
    :param board: Доска судоку 9x9, представленная в виде списка целых чисел.
    :return: (tuple[int, int]|None) Позиция первой пустой ячейки, найденной как
            кортеж индексов строк и столбцов, или «None», если пустая ячейка не найдена.
    """

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def valid(board, pos, num):
    """
    Проверяет, допустимо ли число в ячейке доски судоку.
    :param board: Доска судоку 9x9, представленная в виде списка целых чисел.
    :param pos: Положение ячейки, которую нужно проверить как кортеж индексов строк и столбцов.
    :param num: Номер для проверки.
    :return: True, если число допустимо в ячейке, в противном случае — False.
    """

    for i in range(9):
        if board[i][pos[1]] == num:
            return False

    for j in range(9):
        if board[pos[0]][j] == num:
            return False

    start_i = pos[0] - pos[0] % 3
    start_j = pos[1] - pos[1] % 3
    for i in range(3):
        for j in range(3):
            if board[start_i + i][start_j + j] == num:
                return False
    return True


def solve(board):
    """
    Решает доску судоку, используя алгоритм возврата.
    :param board: Доска судоку 9x9, представленная в виде списка целых чисел.
    :return: True - если доска судоку разрешима, в противном случае - False.
    """

    empty = find_empty(board)
    if not empty:
        return True

    for nums in range(1, 10):
        if valid(board, empty, nums):
            board[empty[0]][empty[1]] = nums
            # рекурсивный шаг
            if solve(board):
                return True
            # это число неверно, поэтому мы устанавливаем его обратно на 0
            board[empty[0]][empty[1]] = 0
    return False


def generate_board():
    """
    Генерирует случайную доску судоку с меньшим количеством начальных чисел.
    :return: (list[list[int]]) Доска судоку 9x9, представленная в виде списка целых чисел.
    """

    board = [[0 for i in range(9)] for j in range(9)]

    # заполнить диагональные поля
    for i in range(0, 9, 3):
        nums = list(range(1, 10))
        shuffle(nums)
        for row in range(3):
            for col in range(3):
                board[i + row][i + col] = nums.pop()

    # заполните оставшиеся ячейки возвратом
    def fill_cells(board, row, col):
        """
        Заполняет оставшиеся ячейки доски судоку с возвратом.
        :param board: Доска судоку 9x9, представленная в виде списка целых чисел.
        :param row: Индекс текущей строки для заполнения.
        :param col: Индекс текущего столбца для заполнения.
        :return: True - если оставшиеся ячейки успешно заполнены, в противном случае — False.
        """

        if row == 9:
            return True
        if col == 9:
            return fill_cells(board, row + 1, 0)

        if board[row][col] != 0:
            return fill_cells(board, row, col + 1)

        for num in range(1, 10):
            if valid(board, (row, col), num):
                board[row][col] = num

                if fill_cells(board, row, col + 1):
                    return True

        board[row][col] = 0
        return False

    fill_cells(board, 0, 0)

    # Удалите большее количество ячеек, чтобы создать головоломку с меньшим количеством начальных чисел.
    for _ in range(randint(55, 65)):
        row, col = randint(0, 8), randint(0, 8)
        board[row][col] = 0

    return board


if __name__ == "__main__":
    board = generate_board()
    print_board(board)
    solve(board)
    print_board(board)
