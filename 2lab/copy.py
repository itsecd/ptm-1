import os
import shutil


def copy_files(path="dataset/tiger/", label="tiger") -> None:
    """Function creates a directory with the name in order

    Args:
        path (str): path to folder
        label (str): name folder
    """
    if not os.path.isdir("dataset_copy"):
        os.mkdir("dataset_copy")
    data = os.listdir(path)
    for i in data:
        shutil.copy(os.path.join(path, i), os.path.join("dataset_copy/", label + "_" + i))


if __name__ == "__main__":
    copy_files()  