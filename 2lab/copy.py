import os
import shutil


def copy_files(path: str, label: str) -> None:
    """Функция принимает путь к файлам: path и метку класса: label"""
    if not os.path.isdir("dataset_copy"):
        os.mkdir("dataset_copy")
    data = os.listdir(path)
    for i in data:
        shutil.copy(os.path.join(path, i), os.path.join("dataset_copy/", label + "_" + i))


def main():
    copy_files("dataset/tiger/", "tiger")
    copy_files("dataset/leopard/", "leopard")


if __name__ == "__main__":
    main()