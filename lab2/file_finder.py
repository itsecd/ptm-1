import os


def find(mark: str, number: int, directory: str) -> str:
    """
    Функция проверяет наличие файла и возвращает путь к нему, в случае, если данный файл существует.
    :param mark: Тип обзора
    :param number: номер обзора в датасете
    :param directory: Путь к папке
    :return: путь
    """
    name = "".join([str(number).zfill(4), ".txt"])
    path = os.path.join(directory, mark)
    path = os.path.join(path, name)
    if os.path.isfile(path):
        return path
    else:
        return None
