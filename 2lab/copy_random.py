import os
import shutil
import random
import csv


def copy_random(path: str, label: str) -> None:
    """Функция принимает путь: path и метку класса: label"""
    if not os.path.isdir("dataset_copy_random"):
        os.mkdir("dataset_copy_random")
    data = []
    info = os.listdir(path)
    for i in info:
        control = True
        while control:
            rand_temp = random.randint(0, 10000)
            rand = str(rand_temp)
            control = os.path.exists("dataset_copy_random/" + rand + ".jpg")
        shutil.copy(
            os.path.join(path, i), os.path.join("dataset_copy_random/", rand + ".jpg")
        )
        absolute = os.path.abspath("dataset_copy_random/" + rand + ".jpg")
        relative = os.path.relpath("dataset_copy_random/" + rand + ".jpg")
        data.append([absolute, relative, label])
    with open("data_copy.csv", "a+", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(data)


def main():
    copy_random("dataset/tiger", "tiger")
    copy_random("dataset/leopard", "leopard")


if __name__ == "__main__":
    main()
