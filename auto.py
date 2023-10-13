from rich.console import Console
import os
from rich import print
import time

console = Console()


def auto():
    print('Made by rus152')
    print('Файл токена не найден. Начинается первоначальная настройка')

    try:
        os.mkdir(os.getenv('APPDATA') + 'TurnOffBot')
    except IOError and Exception:
        print()

    print('')
    token = int()
    while token < 3:
        print('Введете свой токен. (Взять токен для своего бота можно у официального бота BotFather)')
        token2 = input()
        print('')
        print(
            'Ваш токен: ' + token2 + '? Это верно?(Для избежания дальнейших пробоем с запуском, удостоверьтесь, '
                                     'что токен введён правильно) \n [Да/Нет]')
        print('')
        yes_or_not_num = int()
        while yes_or_not_num < 2:
            yes_or_not = input()
            if (yes_or_not == 'Да') or (yes_or_not == 'да'):
                token = token + 3
                break
            if (yes_or_not == 'Нет') or (yes_or_not == 'нет'):
                print('')
                break
            else:
                print('Введите (Да) или (Нет)')
    f = open(os.getenv('APPDATA') + 'TurnOffBot\\token', 'w')
    f.write(token2)
    f.close()

    print('Первоначальная настройка завершена.')
    time.sleep(5)
    console.clear()
