import csv
import os


def create_main_ann(directory: str):
    """
    Функция создания файла-аннотации для изначального датасета. Принимает на вход абсолютный путь к одной из папок
    изначального датасета и, пробегая по всем файлам составляет аннотацию.
    """
    name = ""
    columns = ("Path1", "Path2", "Class")
    with open("data.csv", "w") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(columns)
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            for fln in os.listdir(f):
                fl = os.path.join(f, fln)
                if os.path.isfile(fl) and fl.endswith(".txt"):
                    name = fl[-12] + fl[-11] + fl[-10]
                    if name == 'bad':
                        cont = (fl, name + "/" + fl[-8] + fl[-7] + fl[-6] + fl[-5], name)
                        writer.writerow(cont)
                    else:
                        name = fl[-13] + fl[-12] + fl[-11] + fl[-10]
                        cont = (fl, name + '/' + fl[-8] + fl[-7] + fl[-6] + fl[-5], name)
                        writer.writerow(cont)
