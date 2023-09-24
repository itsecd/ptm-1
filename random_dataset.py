import csv
import os
import random
import shutil

import get_path


def random_copy(class_name:str)-> None:
    """записывает фотографии в файл с рандомными номерами

    Args:
        class_name (str): название класса
    """
    with open("random_annotation.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
        file_writer.writerow(["Абсолютный путь", "Относительный путь", "Класс"])
        for i in range(1050):
            rand_number = random.randint(0, 10000)
            if (os.path.isfile(get_path.get_absolute_way(class_name, i, "download")) == True):
                while(os.path.isfile(get_path.get_absolute_way(class_name, rand_number, "random")) == True):
                    rand_number = random.randint(0, 10000)
                shutil.copyfile(get_path.get_absolute_way(class_name, i, "download"), get_path.get_absolute_way(class_name, rand_number, "random"))
                file_writer.writerow([get_path.get_absolute_way(class_name, i, "download"), get_path.random_relative_way(rand_number), class_name])


def main():
    print("Start")
    if not os.path.isdir("dataset/random_dataset"):
        os.mkdir("dataset/random_dataset")
    class_name = "rose"
    random_copy(class_name)
    class_name = "tulip"
    random_copy(class_name)
    print("The end")
        
    
if __name__ == "__main__":
    main()