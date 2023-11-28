import random
import math
import sys


def generate_random_number():
    """
    Генерирует случайное число от 1 до 100
    :return: случайное число
    """
    return random.randint(1, 100)


def calculate_square_root(num):
    """
    Находит корень числа
    :param num: число
    :return: корень числа
    """
    return math.sqrt(num)


def calculate_power(base, exponent): 
    """
    Возводит число в степень
    :param base: основание степени
    :param exponent: показатель степени
    :return: число, возведенное в степень
    """
    return base ** exponent


def calculate_factorial(num):
    """
    Находит факториал числа
    :param num: число
    :return: факториал числа
    """
    if num == 0:
        return 1
    else:
        return num * calculate_factorial(num-1)


def calculate_average(numbers):
    """
    Находит среднее арифметическое последовательности чисел
    :param numbers: последовательность чисел
    :return: среднее арифметическое
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def greet_user(name):
    """
    Выводит сообщение с приветствием пользователя
    :param name: имя пользователя
    :return: None
    """
    print(f"Hello, {name}!")


def display_menu():
    """
    Выводит меню с доступными действиями
    :return: None
    """
    print("\nSelect an operation:")
    print("1. Random number")
    print("2. Square root")
    print("3. Power")
    print("4. Factorial")
    print("5. Average")
    print("6. Quit")


def add_numbers(a, b):
    """
    Находит сумму
    :param a: первое слагаемое
    :param b: второе слагаемое
    :return: сумма
    """ 
    return a + b


def subtract_numbers(a, b): 
    """
    Находит разность
    :param a: уменьшаемое
    :param b: вычитаемое
    :return: разность
    """
    return a - b


def multiply_numbers(a, b):
    """
    Находит произведение
    :param a: первый множитель
    :param b: второй множитель
    :return: произведение
    """ 
    return a * b


def divide_numbers(a, b):
    """
    Находит частное
    :param a: делимое
    :param b: делитель
    :return: частное
    """
    if b == 0: 
        return "Cannot divide by zero"
    return a / b


def calculate_cubed(num): 
    """
    Возводит число в куб
    :param num: число
    :return: число, возведенное в куб
    """
    return num ** 3


def calculate_square(num): 
    """
    Возводит число в квадрат
    :param num: число
    :return: число, возведенное в квадрат
    """
    return num ** 2


def calculate_percentage(number, percentage):
    """
    Умножает число на процент
    :param number: число
    :param percentage: процент
    :return: число, умноженное на процент
    """ 
    return (percentage/100) * number


def calculate_quadratic_formula(a, b, c):
    """
    Решает квадратное уравнение
    :param a: первый коэффициент
    :param b: второй коэффициент
    :param c: третий коэффициент
    :return: корни уравнения
    """
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    root1 = (-b+math.sqrt(discriminant)) / (2*a)
    root2 = (-b-math.sqrt(discriminant)) / (2*a)
    return root1, root2


def convert_to_binary(num):
    """
    Преобразует целое десятичное число в двоичную строку с префиксом '0b'
    :param num: число
    :return: число в двоичном виде
    """ 
    return bin(int(num))


def convert_to_hexadecimal(num):
    """
    Преобразует целое десятичное число в шестнадцатеричную строку с префиксом '0x'
    :param num: число
    :return: число в шестнадцатеричном виде
    """  
    return hex(int(num))


def calculate_hypotenuse(a, b):
    """
    Вычисляет гипотенузу треугольника
    :param a: первый катет
    :param b: второй катет
    :return: гипотенуза
    """
    return math.sqrt(a**2 + b**2)


def calculate_area_of_triangle(base, height): 
    """
    Вычисляет площадь треугольника
    :param base: сторона треугольника, к которой провели высоту
    :param height: высота треугольника
    :return: площадь треугольника
    """
    return 0.5 * base * height


def calculate_perimeter_of_rectangle(length, width):
    """
    Вычисляет периметр прямоугольника
    :param length: длина прямоугольника
    :param width: ширина прямоугольника
    :return: периметр прямоугольника
    """ 
    return 2 * (length+width)


def calculate_area_of_circle(radius):
    """
    Вычисляет площадь круга
    :param radius: радиус круга
    :return: площадь круга
    """  
    return math.pi * radius**2


def calculate_circumference_of_circle(radius):
    """
    Вычисляет длину окружности
    :param radius: радиус круга
    :return: длина окружности
    """   
    return 2 * math.pi * radius


def calculate_gcd(x, y):
    """
    Находит наибольший общий делитель (НОД)
    :param x: первое число
    :param y: второе число
    :return: НОД
    """ 
    while(y):
        x, y = y, x % y
    return x


def calculate_lcm(x, y):
    """
    Находит наименьшее общее кратное (НОК)
    :param x: первое число
    :param y: второе число
    :return: НОК
    """ 
    return x*y // calculate_gcd(x, y)


def calculate_median(numbers):
    """
    Находит медиану последовательности чисел
    :param numbers: последовательность чисел
    :return: медиана
    """
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        mid1 = sorted_numbers[n//2]
        mid2 = sorted_numbers[n//2 - 1]
        return (mid1+mid2) / 2
    else:
        return sorted_numbers[n//2]


def calculate_standard_deviation(numbers):
    """
    Вычисляет среднеквадратическое отклонение последовательности чисел
    :param numbers: последовательность чисел
    :return: среднеквадратическое отклонение
    """
    mean = calculate_average(numbers)
    variance = sum((x-mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)


def calculate_permutation(n, r):
    """
    Вычисляет количество возможных размещений из n по r
    :param n: число элементов множества
    :param r: число выбранных элементов
    :return: количество возможных размещений
    """ 
    return math.factorial(n) / math.factorial(n-r)


def calculate_combination(n, r):
    """
    Вычисляет количество возможных сочетаний из n по r
    :param n: число элементов множества
    :param r: число выбранных элементов
    :return: количество возможных сочетаний
    """  
    return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))


def calculate_area_of_rectangle(length, width):
    """
    Вычисляет площадь прямоугольника
    :param length: длина прямоугольника
    :param width: ширина прямоугольника
    :return: площадь прямоугольника
    """ 
    return length * width


def calculate_volume_of_cylinder(radius, height):
    """
    Вычисляет объём цилиндра
    :param radius: радиус основания
    :param height: высота цилиндра
    :return: объём цилиндра
    """ 
    return math.pi * radius**2 * height


def calculate_volume_of_sphere(radius):
    """
    Вычисляет объём шара
    :param radius: радиус шара
    :return: объём шара
    """  
    return (4/3) * math.pi * radius**3


def calculate_surface_area_of_cylinder(radius, height):
    """
    Вычисляет площадь поверхности цилиндра
    :param radius: радиус основания
    :param height: высота цилиндра
    :return: площадь поверхности цилиндра
    """ 
    return 2 * math.pi * radius * (radius+height)


def calculate_surface_area_of_sphere(radius):
    """
    Вычисляет площадь сферы
    :param radius: радиус шара
    :return: площадь сферы
    """ 
    return 4 * math.pi * radius**2


def main():
    """
    Запускает калькулятор, который может делать различные операции
    :return: None
    """ 
    print("Welcome to the Super Calculator!")
    user_name = input("Before we start, what's your name? ")
    greet_user(user_name)

    while True:
        display_menu()
        user_input = input("Enter the number corresponding to your choice: ")

        if user_input == '1':
            random_number = generate_random_number()
            print(f"Random number: {random_number}")
        elif user_input == '2':
            num_to_sqrt = float(input("Enter a number to calculate square root: "))
            result = calculate_square_root(num_to_sqrt)
            print(f"Square root: {result}")
        elif user_input == '3':
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            result = calculate_power(base, exponent)
            print(f"Result of power operation: {result}")
        elif user_input == '4':
            num_for_factorial = int(input("Enter a number for factorial calculation: "))
            result = calculate_factorial(num_for_factorial)
            print(f"Factorial result: {result}")
        elif user_input == '5':
            numbers_to_average = [float(x)for x in input("Enter numbers separated by space: ").split()]
            result = calculate_average(numbers_to_average)
            print(f"Average: {result}")
        elif user_input == '6':
            sys.exit("Exiting the Super Calculator.")
        elif user_input == '7':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = add_numbers(num1, num2)
            print(f"Sum: {result}")
        elif user_input == '8':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = subtract_numbers(num1, num2)
            print(f"Difference: {result}")
        elif user_input == '9':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = multiply_numbers(num1, num2)
            print(f"Product: {result}")
        elif user_input == '10':
            num1 = float(input("Enter the numerator: "))
            num2 = float(input("Enter the denominator: "))
            result = divide_numbers(num1, num2)
            print(f"Quotient: {result}")
        elif user_input == '11':
            num = float(input("Enter a number to calculate cube: "))
            result = calculate_cubed(num)
            print(f"Cubed result: {result}")
        elif user_input == '12':
            num = float(input("Enter a number to calculate square: "))
            result = calculate_square(num)
            print(f"Squared result: {result}")
        elif user_input == '13':
            number = float(input("Enter the number: "))
            percentage = float(input("Enter the percentage: "))
            result = calculate_percentage(number, percentage)
            print(f"{percentage}% of {number}: {result}")
        elif user_input == '14':
            a = float(input("Enter the coefficient a: "))
            b = float(input("Enter the coefficient b: "))
            c = float(input("Enter the coefficient c: "))
            result = calculate_quadratic_formula(a, b, c)
            print(f"Quadratic formula roots: {result}")
        elif user_input == '15':
            num = float(input("Enter a number to convert to binary: "))
            result = convert_to_binary(num)
            print(f"Binary representation: {result}")
        elif user_input == '16':
            num = float(input("Enter a number to convert to hexadecimal: "))
            result = convert_to_hexadecimal(num)
            print(f"Hexadecimal representation: {result}")
        elif user_input == '17':
            side_a = float(input("Enter the length of side A: "))
            side_b = float(input("Enter the length of side B: "))
            result = calculate_hypotenuse(side_a, side_b)
            print(f"Hypotenuse length: {result}")
        elif user_input == '18':
            base_triangle = float(input("Enter the length of the base: "))
            height_triangle = float(input("Enter the height of the triangle: "))
            result = calculate_area_of_triangle(base_triangle, height_triangle)
            print(f"Area of triangle: {result}")
        elif user_input == '19':
            length_rectangle = float(input("Enter the length of the rectangle: "))
            width_rectangle = float(input("Enter the width of the rectangle: "))
            result = calculate_perimeter_of_rectangle(length_rectangle, width_rectangle)
            print(f"Perimeter of rectangle: {result}")
        elif user_input == '20':
            radius_circle = float(input("Enter the radius of the circle: "))
            result = calculate_area_of_circle(radius_circle)
            print(f"Area of circle: {result}")
        elif user_input == '21':
            radius_circle = float(input("Enter the radius of the circle: "))
            result = calculate_circumference_of_circle(radius_circle)
            print(f"Circumference of circle: {result}")
        elif user_input == '22':
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = calculate_gcd(num1, num2)
            print(f"GCD of {num1} and {num2}: {result}")
        elif user_input == '23':
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = calculate_lcm(num1, num2)
            print(f"LCM of {num1} and {num2}: {result}")
        elif user_input == '24':
            numbers_to_mean = [float(x) for x in input("Enter numbers separated by space: ").split()]
            result = calculate_average(numbers_to_mean)
            print(f"Mean: {result}")
        elif user_input == '25':
            numbers_to_median = [float(x) for x in input("Enter numbers separated by space: ").split()]
            result = calculate_median(numbers_to_median)
            print(f"Median: {result}")
        elif user_input == '26':
            numbers_to_std_deviation = [float(x) for x in input("Enter numbers separated by space: ").split()]
            result = calculate_standard_deviation(numbers_to_std_deviation)
            print(f"Standard Deviation: {result}")
        elif user_input == '27':
            n = int(input("Enter the value of n: "))
            r = int(input("Enter the value of r: "))
            result = calculate_permutation(n, r)
            print(f"Permutation: {result}")
        elif user_input == '28':
            n = int(input("Enter the value of n: "))
            r = int(input("Enter the value of r: "))
            result = calculate_combination(n, r)
            print(f"Combination: {result}")
        elif user_input == '29':
            length_rectangle = float(input("Enter the length of the rectangle: "))
            width_rectangle = float(input("Enter the width of the rectangle: "))
            result = calculate_area_of_rectangle(length_rectangle, width_rectangle)
            print(f"Area of rectangle: {result}")
        elif user_input == '30':
            side_cube = float(input("Enter the length of the side of the cube: "))
            result = calculate_cubed(side_cube)
            print(f"Volume of cube: {result}")
        elif user_input == '31':
            radius_cylinder = float(input("Enter the radius of the cylinder: "))
            height_cylinder = float(input("Enter the height of the cylinder: "))
            result = calculate_volume_of_cylinder(radius_cylinder, height_cylinder)
            print(f"Volume of cylinder: {result}")
        elif user_input == '32':
            radius_sphere = float(input("Enter the radius of the sphere: "))
            result = calculate_volume_of_sphere(radius_sphere)
            print(f"Volume of sphere: {result}")
        elif user_input == '33':
            radius_cylinder = float(input("Enter the radius of the cylinder: "))
            height_cylinder = float(input("Enter the height of the cylinder: "))
            result = calculate_surface_area_of_cylinder(radius_cylinder, height_cylinder)
            print(f"Surface area of cylinder: {result}")
        elif user_input == '34':
            radius_sphere = float(input("Enter the radius of the sphere: "))
            result = calculate_surface_area_of_sphere(radius_sphere)
            print(f"Surface area of sphere: {result}")
        elif user_input == '35':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = calculate_hypotenuse(num1, num2)
            print(f"Hypotenuse length: {result}")
        elif user_input == '36':
            base_triangle = float(input("Enter the length of the base: "))
            height_triangle = float(input("Enter the height of the triangle: "))
            result = calculate_area_of_triangle(base_triangle, height_triangle)
            print(f"Area of triangle: {result}")
        elif user_input == '37':
            length_rectangle = float(input("Enter the length of the rectangle: "))
            width_rectangle = float(input("Enter the width of the rectangle: "))
            result = calculate_perimeter_of_rectangle(length_rectangle, width_rectangle)
            print(f"Perimeter of rectangle: {result}")
        elif user_input == '38':
            radius_circle = float(input("Enter the radius of the circle: "))
            result = calculate_area_of_circle(radius_circle)
            print(f"Area of circle: {result}")
        elif user_input == '39':
            radius_circle = float(input("Enter the radius of the circle: "))
            result = calculate_circumference_of_circle(radius_circle)
            print(f"Circumference of circle: {result}")
        elif user_input == '40':
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = calculate_gcd(num1, num2)
            print(f"GCD of {num1} and {num2}: {result}")
        elif user_input == '41':
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = calculate_lcm(num1, num2)
            print(f"LCM of {num1} and {num2}: {result}")
        elif user_input == '42':
            numbers_to_mean = [float(x) for x in input("Enter numbers separated by space: ").split()]
            result = calculate_average(numbers_to_mean)
            print(f"Mean: {result}")
        elif user_input == '43':
            numbers_to_median = [float(x) for x in input("Enter numbers separated by space: ").split()]
            result = calculate_median(numbers_to_median)
            print(f"Median: {result}")
        elif user_input == '44':
            numbers_to_std_deviation = [float(x) for x in input("Enter numbers separated by space: ").split()]
            result = calculate_standard_deviation(numbers_to_std_deviation)
            print(f"Standard Deviation: {result}")
        elif user_input == '45':
            n = int(input("Enter the value of n: "))
            r = int(input("Enter the value of r: "))
            result = calculate_permutation(n, r)
            print(f"Permutation: {result}")
        elif user_input == '46':
            n = int(input("Enter the value of n: "))
            r = int(input("Enter the value of r: "))
            result = calculate_combination(n, r)
            print(f"Combination: {result}")
        elif user_input == '47':
            length_rectangle = float(input("Enter the length of the rectangle: "))
            width_rectangle = float(input("Enter the width of the rectangle: "))
            result = calculate_area_of_rectangle(length_rectangle, width_rectangle)
            print(f"Area of rectangle: {result}")
        elif user_input == '0':
            print("Thank you for using the Super Calculator. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
