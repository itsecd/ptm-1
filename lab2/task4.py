import os


def find(mark: str, number: int) -> str:
    """
    Функция проверяет наличие файла и возвращает путь к нему, в случае, если данный файл существует.
    """
    path = "dataset/" + mark + "/" + str(number).zfill(4) + ".txt"
    if os.path.isfile(path):
        return path
    else:
        return None
