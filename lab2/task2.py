import codecs
import csv
import os


def copy_to_new_directory(path_old: str, path_new: str):
    """
    Функция копирования исходного датасета в другую директорию. Принимает на вход старый и новый путь к текстовым
     файлам. Пробегая по каждому, осуществляет копирование.
    """
    for filename in os.listdir(path_old):
        f = os.path.join(path_old, filename)
        if os.path.isfile(f) and filename.endswith('.txt'):
            number = f[-8] + f[-7] + f[-6] + f[-5]
            name = f[-12] + f[-11] + f[-10]
            if name != 'bad':
                name = f[-13] + f[-12] + f[-11] + f[-10]
            file = codecs.open(u'' + f, "r", "utf-8")
            ln = file.read()
            file.close()
            file = codecs.open(u'' + path_new + "/" + name + "_" + number + ".txt", "w", "utf-8")
            file.write(ln)
            file.close()


def create_new_dir_ann(directory: str):
    """
    Функция создания аннотации для нового датасета. Принимает на вход путь и, пробегая по файлам, заполняет таблицу.
    Метка класса берётся из названия файла.
    """
    name = ""
    columns = ("Path1", "Path2", "Class")
    with open("data1.csv", "w") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(columns)
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f) and filename.endswith('.txt'):
                name = f[-12] + f[-11] + f[-10]
                if name == 'bad':
                    cont = (f, 'dataset1/' + name + '_' + f[-8] + f[-7] + f[-6] + f[-5], name)
                    writer.writerow(cont)
                else:
                    name = f[-13] + f[-12] + f[-11] + f[-10]
                    cont = (f, "dataset1/" + name + '_' + f[-8] + f[-7] + f[-6] + f[-5], name)
                    writer.writerow(cont)
