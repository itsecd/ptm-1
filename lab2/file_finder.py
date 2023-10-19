import os


def find(mark: str, number: int, directory: str) -> str:
    """
    Функция проверяет наличие файла и возвращает путь к нему, в случае, если данный файл существует.
    :param mark: Тип обзора
    :param number: номер обзора в датасете
    :param directory: Путь к папке
    :return: путь
    """
    path = directory + mark + "/" + str(number).zfill(4) + ".txt"
    if os.path.isfile(path):
        return path
    else:
        return None
