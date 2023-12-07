import os
import csv


def create_csv(path: str, path_to: str) -> None:
    """The function accepts the path to the files: path"""
    info = os.listdir(path + "/")
    data = []
    for i in info:
        info_data = os.listdir(path + "/" + i)
        for j in info_data:
            absolute = os.path.abspath(path + "/" + i + "/" + j)
            relative = os.path.relpath(path + "/" + i + "/" + j)
            data.append([absolute, relative, i])
    with open(path_to + ".csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(data)


if __name__ == "__main__":
    create_csv("dataset")
