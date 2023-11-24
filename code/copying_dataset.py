import os
import shutil
import csv

def copying_dataset(path: str, path_copier: str):
    """
    Возвращает копию папки с изображениями

            Параметры:
                    path(str): Путь к папке
                    path_copier(str): Путь к новой папке
    """

    if not os.path.exists(path_copier):
        os.mkdir(path_copier)

    source = os.listdir(path + "/")
    data = []

    for i in source:
        source_data = os.listdir(path + "/" + i)

        for j in source_data:
            shutil.copy(os.path.join(path + "/" + i, j),
                        os.path.join(path_copier + "/", i + "__" + j))
            

def main():
    copying_dataset("dataset", "dataset_copier")


if __name__ == "__main__":
    main()