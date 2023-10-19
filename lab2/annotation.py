import os
import csv


def create_main_ann(path: str) -> None:
    """
    Функция создания файла-аннотации для изначального датасета. Принимает на вход абсолютный путь к одной из папок
    изначального датасета и, пробегая по всем файлам составляет аннотацию.
    :param path: Путь к папке с датасетом
    :return: None
    """
    columns = ("Path1", "Path2", "Class")
    with open("data.csv", "w") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(columns)
        for directories in os.listdir(path):
            directory = os.path.join(path, directories)
            for files in os.listdir(directory):
                file = os.path.join(directory, files)
                if os.path.isfile(file) and file.endswith(".txt"):
                    rev_type = file[-12] + file[-11] + file[-10]
                    if rev_type == "bad":
                        file_info = (file, rev_type + "/" + file[-8] + file[-7] + file[-6] + file[-5], rev_type)
                        writer.writerow(file_info)
                    else:
                        rev_type = file[-13] + file[-12] + file[-11] + file[-10]
                        file_info = (file, rev_type + "/" + file[-8] + file[-7] + file[-6] + file[-5], rev_type)
                        writer.writerow(file_info)
