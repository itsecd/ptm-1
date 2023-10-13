from rich.console import Console
import os
from rich import print
import time

console = Console()


def auto():
    print('Made by rus152')
    print('Файл токена не найден. Начинается первоначальная настройка')

    try:
        os.mkdir(os.getenv('APPDATA') + '\TurnOffBot')
    except (IOError) and (Exception):
        print()

    print('')
    toknum = int()
    while toknum < 3:
        print('Введете свой токен. (Взять токен для своего бота можно у оффициального бота BotFather)')
        tokenin = input()
        print('')
        toknum == 0
        print(
            'Ваш токен: ' + tokenin + '? Это верно?(Для избежания дальнейших пролем с запуском, удостоверьтесь, что токен введён правильно) \n [Да/Нет]')
        print('')
        yes_or_notnum = int()
        while yes_or_notnum < 2:
            yes_or_not = input()
            if (yes_or_not == 'Да') or (yes_or_not == 'да'):
                toknum = toknum + 3
                break
            if (yes_or_not == 'Нет') or (yes_or_not == 'нет'):
                print('')
                break
            else:
                print('Введите (Да) или (Нет)')
    f = open(os.getenv('APPDATA') + '\TurnOffBot\\token', 'w')
    f.write(tokenin)
    f.close()

    print('Первоначальная настройка завершена.')
    time.sleep(5)
    console.clear()
