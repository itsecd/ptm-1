import requests
import time
from rich import print
from rich.console import Console


def main():
    timeout = 1
    internet = False
    console = Console()

    while not internet:
        print('Проверка соединения')
        try:
            requests.head("http://www.google.com/", timeout=timeout)
            print('Соединение с интернетом есть')
            internet = True
            time.sleep(2)
            console.clear()
        except requests.ConnectionError:
            print("Интернета нет, повторная попытка через несколько секунд.")
            time.sleep(5)
            console.clear()
