import csv
import os


def create_csv(path: str) -> None:
    """Function creates a csv file

    Args:
        path (str): path to folder
    """
    info = os.listdir(path)
    data = []
    for i in info:
        info_data = os.listdir(path + i)
        for j in info_data:
            absolute_path = os.path.abspath(path + i + "/" + j)
            relative_path = os.path.relpath(path + i + "/" + j)
            data.append([absolute_path, relative_path, i])
    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(data)


if __name__ == "__main__":
    create_csv("dataset/")