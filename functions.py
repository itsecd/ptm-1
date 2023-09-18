import math
import os
import requests
import json
import csv
import logging
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes


def swap(val_1: int, val_2: int) -> None:
    """
    функция печатает 2 значения, затем меняет их местами и снова печатает
    :param val_1: первое число
    :param val_2: второе число
    :return: ничего
    """
    print('var_1:', val_1, 'var_2:', val_2)
    tmp_val = val_1
    val_1 = val_2
    val_2 = tmp_val
    print('var_1:', val_1, 'var_2:', val_2)


def all_permutations(val_1: int, val_2: int, val_3: int) -> None:
    """
    функция находит все перестановки трёх чисел
    :param val_1: первое число
    :param val_2: второе число
    :param val_3: третье число
    :return: ничего
    """
    arr = list()
    arr.append(val_1)
    arr.append(val_2)
    arr.append(val_3)
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                if i != j & j != k & k != i:
                    print(arr[i], arr[j], arr[k])


def encrypt(text_bytes: bytes, key_bytes: bytes) -> bytes:
    """
    функция шифрует текст с помощью ключа
    :param text_bytes: текст
    :param key_bytes: ключ
    :return: зашифрованный текст
    """
    padder = padding.ANSIX923(128).padder()
    padded_text = padder.update(text_bytes) + padder.finalize()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key_bytes), mode=modes.CBC(iv))
    encryptor = cipher.encryptor()
    encrypted_text = iv + encryptor.update(padded_text) + encryptor.finalize()
    return encrypted_text


def decrypt(encrypted_text: bytes, key_bytes: bytes) -> bytes:
    """
    функция шифрует зашифрованный текст с помощью ключа
    :param encrypted_text: зашифрованный текст
    :param key_bytes: ключ
    :return: расшифрованный текст
    """
    encrypted_text, iv = encrypted_text[16:], encrypted_text[:16]
    cipher = Cipher(algorithms.AES(key_bytes), mode=modes.CBC(iv))
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(encrypted_text) + decryptor.finalize()
    unpadder = padding.ANSIX923(128).unpadder()
    text = unpadder.update(decrypted_text) + unpadder.finalize()
    return text


def count_unique_words(filename: str) -> int:
    """
    функция читает файл и находит кол-во уникальных слов
    :param filename: имя файла
    :return: кол-во уникальных слов
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            words = text.split()
            word_count = {}
            for word in words:
                word = ''.join(c for c in word if c.isalnum())
                if word:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
            for word, count in word_count.items():
                print(f"{word}: {count}")
            return len(word_count)
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def caesar_cipher(alf: str, alf_cipher: str, text: str) -> str:
    """
    функция реализует шифра цезаря
    :param alf: текущий алфавит текста
    :param alf_cipher: желаемый алфавит
    :param text: текст
    :return: текст с изменённым алфавитом
    """
    encoded_text = ""
    text = text.lower()
    for symbol in text:
        flag = False
        for j in range(len(alf)):
            if symbol == alf[j]:
                encoded_text += alf_cipher[j]
                flag = True
        if not flag:
            encoded_text += symbol
    return encoded_text


def factorial(val: int) -> int:
    """
    функция находит факториал
    :param val: число
    :return: факториал числа
    """
    if val == 0:
        return 1
    else:
        result = 1
        for i in range(1, val + 1):
            result *= i
        return result


def bubble_sort(arr: list) -> None:
    """
    функция реализует сортировку пузырьком
    :param arr: массив
    :return: ничего
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def insertion_sort(arr: list) -> None:
    """
    функция реализует сортировку вставками
    :param arr: массив
    :return: ничего
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def selection_sort(arr: list) -> None:
    """
    функция реализует сортировку выбором
    :param arr: массив
    :return: ничего
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def merge_sort(arr: list) -> None:
    """
    функция реализует сортировку слиянием
    :param arr: массив
    :return: ничего
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def quick_sort(arr: list) -> list:
    """
    функция реализует быструю сортировку
    :param arr: массив
    :return: ничего
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


memo = {}


def fibonacci(n: int) -> int:
    """
    функция вычисляет n-ое число фибоначчи
    :param n: номер числа
    :return: n-ое число фибоначчи
    """
    if n in memo:
        return memo[n]
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    memo[n] = result
    return result


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


def write_string_to_csv(data_string: str, file_name: str = "res_file.csv") -> None:
    """
        функция дописывает в конец csv файла строку data_string
        data_string - строка, которую записываем
        file_name - название файла, в который записываем
    """
    try:
        with open(file_name, 'a', newline='') as file_name:
            writer = csv.writer(file_name)
            writer.writerow({data_string})
    except OSError as error:
        logging.error(f'Ошибка, не удалось открыть файл: {error}')


def get_curency_course(curency: str = 'USD', start_url_string: str = 'https://www.cbr-xml-daily.ru/daily_json.js') \
        -> None:
    """
    функция получает курс заданной валюты на момент конкретной даты
    и записывает в файл до тех пор, пока не дойдёт до последней возможной даты
    curency - валюта, для которой получаем курс
    start_url_string - стартовая ссылка, с которой начинаем парсить
    """
    response = requests.get(start_url_string)
    url_text = json.loads(response.text)
    while True:
        date = url_text['Date'][:10]
        curency_course = url_text['Valute'][curency]['Value']
        print(f'Программа на данный момент на дате: {date}')
        res_string = date + ', ' + str(curency_course)
        write_string_to_csv(res_string)
        prev_url_string = "https:" + url_text['PreviousURL']
        prev_response = requests.get(prev_url_string)
        url_text = json.loads(prev_response.text)
        if not prev_response.ok:
            print(f'Программа дошла до последней возможной даты')
            break


def is_prime(n: int) -> bool:
    """
    функция определяет является ли число простым
    :param n: число
    :return: bool является ли число простым
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def find_primes_in_range(start: int, end: int) -> list:
    """
    функция находит все простые числа в диапазоне от start до end
    :param start: начало диапазона
    :param end: конец диапазона
    :return: все простые числа в диапазоне
    """
    if start < 2:
        start = 2
    primes = list()
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes
