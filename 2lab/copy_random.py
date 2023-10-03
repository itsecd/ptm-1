import csv
import os
import random
import shutil


def create_file_paths(path: str, label: str) -> None:
    """Function creates a directory with random names and 
    creates csv file
    
    Args:
        path (str): path to folder
        label (str): name folder
    """
    if not os.path.isdir("dataset_copy_random"):
        os.mkdir("dataset_copy_random")
    data = []
    images = os.listdir(path)
    for i in images:
        is_path = True
        while is_path:
            number = str(random.randint(0, 10000))
            is_path = os.path.exists("dataset_copy_random/" + number + ".jpg")
        shutil.copy(os.path.join(path, i), os.path.join("dataset_copy_random/", number + ".jpg"))
        absolute_path = os.path.abspath("dataset_copy_random/" + number + ".jpg")
        relative_path = os.path.relpath("dataset_copy_random/" + number + ".jpg")
        data.append([absolute_path, relative_path, label])
    with open("data_copy.csv", "a+", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(data)


def main():
    create_file_paths("dataset/tiger", "tiger")
    create_file_paths("dataset/leopard", "leopard")


if __name__ == "__main__":
    main()