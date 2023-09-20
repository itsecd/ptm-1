import math


def draw_pyramid(rows: int) -> None:
    """
    функция рисует пирамиду
    :param rows: кол-во строк
    :return: ничего
    """
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(i, 0, -1):
            print(j, end="")
        for j in range(2, i + 1):
            print(j, end="")
        print()


def draw_circle(radius: int) -> None:
    """
    функция рисует круг
    :param radius: радиус
    :return: ничего
    """
    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            if math.sqrt(i ** 2 + j ** 2) <= radius + 0.5:
                print("*", end="")
            else:
                print(" ", end="")
        print()


def draw_christmas_tree(height: int) -> None:
    """
    функция рисует ёлку
    :param height: высота
    :return: ничего
    """
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))
    trunk_height = height // 3
    trunk_width = height // 3
    for i in range(trunk_height):
        print(" " * (height - trunk_width // 2 - 1) + "*" * trunk_width)


def draw_square(side_length: int) -> None:
    """
    функция рисует квадрат
    :param side_length: длина стороны
    :return: ничего
    """
    if side_length < 2:
        print("Слишком маленькая сторона для квадрата.")
        return
    for i in range(side_length):
        print("/" * side_length)
