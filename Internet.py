import requests
import time
from rich import print
from rich.console import Console


def check_internet_connection(timeout=1, max_retries=5):
    console = Console()
    retries = 0

    while retries < max_retries:
        print('Проверка соединения')
        try:
            requests.head("https://www.google.com/", timeout=timeout)
            print('Соединение с интернетом есть')
            time.sleep(2)
            console.clear()
            return True
        except requests.ConnectionError:
            retries += 1
            print("Интернета нет, повторная попытка через несколько секунд.")
            time.sleep(5)
            console.clear()

    print("Не удалось установить соединение после всех попыток.")
    return False


if __name__ == "__main__":
    check_internet_connection()
