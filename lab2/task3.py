import codecs
import csv
import os
from random import randint


def copy_to_new_dir_with_random_naming(path: str, path_new: str):
    """
    Функция копирования исходного датасета в новую директорию с присваиванием случайного номера.
    Также, чтобы не потерять метку класса, создаёт файл-аннотацию для нового датасета.
    """
    columns = ("Path1", "Path2", "Class")
    with open("data2.csv", "w") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(columns)
        for filename in os.listdir(path):
            f = os.path.join(path, filename)
            for fln in os.listdir(f):
                fl = os.path.join(f, fln)
                if os.path.isfile(fl) and fl.endswith('.txt'):
                    new_name = str(randint(0, 9999)).zfill(4)
                    name = fl[-12] + fl[-11] + fl[-10]
                    if name == 'bad':
                        cont = (path_new + "/" + new_name, 'dataset3/' + new_name, name)
                        writer.writerow(cont)
                    else:
                        name = fl[-13] + fl[-12] + fl[-11] + fl[-10]
                        cont = (path_new + "/" + new_name, "dataset3/" + new_name, name)
                        writer.writerow(cont)
                    file = codecs.open(u'' + fl, "r", "utf-8")
                    ln = file.read()
                    file.close()
                    file = codecs.open(u'' + path_new + "/" + new_name + ".txt", "w", "utf-8")
                    file.write(ln)
                    file.close()
