import os
import shutil


def copy(path: str, label: str) -> None:
    """Функция принимает путь к файлам: path и метку класса: label"""
    if not os.path.isdir("dataset_copy"):
        os.mkdir("dataset_copy")
    info = os.listdir(path)
    for i in info:
        shutil.copy(
            os.path.join(path, i), os.path.join("dataset_copy/", label + "_" + i)
        )


def main():
    copy("dataset/tiger/", "tiger")
    copy("dataset/leopard/", "leopard")


if __name__ == "__main__":
    main()
