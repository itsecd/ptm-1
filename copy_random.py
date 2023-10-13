import os
import shutil
import random
import csv


def copy_random(path: str, path_to: str) -> None:
    """Функция принимает путь: path и метку класса: label"""
    if not os.path.isdir(path_to):
        os.mkdir(path_to)
    data = []
    info = os.listdir(path + "/")
    for i in info:
        info_directiry = os.listdir(path + "/" + i)
        for j in info_directiry:
            control = True
            while control:
                rand_temp = random.randint(0, 10000)
                rand = str(rand_temp)
                control = os.path.exists(path_to + "/" + rand + ".jpg")
            shutil.copy(
                os.path.join(path, i + "/" + j),
                os.path.join(path_to + "/", rand + ".jpg"),
            )
            absolute = os.path.abspath(path_to + "/" + rand + ".jpg")
            relative = os.path.relpath(path_to + "/" + rand + ".jpg")
            data.append([absolute, relative, i])
    with open(path_to+".csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(data)


def main():
    copy_random("dataset/")


if __name__ == "__main__":
    main()
