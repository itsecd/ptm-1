import os
import csv
import random
from array import array


def create_csv(path: str) -> None:
    """Функция принимает путь к файлам: path"""
    info = os.listdir(path)
    data = []
    for i in info:
        info_data = os.listdir(path + i)
        for j in info_data:
            absolute = os.path.abspath(path+i+"/" + j)
            relative = os.path.relpath(path+i+"/" + j)
            data.append([absolute, relative, i])
    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(data)


def main():
    create_csv("dataset/")


if __name__ == "__main__":
    main()
