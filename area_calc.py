import math


def calculate_circle_area(radius: float) -> float:
    """
    Вычисление площади окружности.
    :param radius: Радиус окружности.
    """
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")

    area = math.pi * radius ** 2
    return area


def calculate_triangle_area(base: float, height: float) -> float:
    """
    Вычисление площади треугольника.
    :param base: Основание треугольника.
    :param height: Высота треугольника.
    """
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")

    area = 0.5 * base * height
    return area


def calculate_rectangle_area(length: float, width: float) -> float:
    """
    Вычисление площади прямоугольника.
    :param length: Длина прямоугольника.
    :param width: Ширина прямоугольника.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")

    area = length * width
    return area


def main() -> None:
    """
    Основная функция.
    """
    try:
        radius = float(input("Enter the radius of the circle: "))
        circle_area = calculate_circle_area(radius)
        print(f"The area of the circle is: {circle_area:.2f}")

        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        triangle_area = calculate_triangle_area(base, height)
        print(f"The area of the triangle is: {triangle_area:.2f}")

        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        rectangle_area = calculate_rectangle_area(length, width)
        print(f"The area of the rectangle is: {rectangle_area:.2f}")

    except ValueError as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()