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
