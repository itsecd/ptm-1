import os
import shutil
import random
import csv

def random_copying(path: str,path_copier: str):

    """Функция принимает путь к файлам: path и путь к новой директории: path_new"""

    if not os.path.exists(path_copier):
        os.mkdir(path_copier)

    source = os.listdir(path + "/")
    data = []

    for i in source:
        source_data = os.listdir(path + "/" + i)
        for j in source_data:
            exist = True
            
            while(exist):
                rand = random.randint(0, 10000)
                value = str(rand)
                exist = os.path.exists(path_copier + "/" + value + ".jpg")    
    
            shutil.copy(os.path.join(path + "/", i + "/" + j), os.path.join(path_copier + "/", value + ".jpg"))            
               
def main():
    random_copying("dataset", "dataset_another")

if __name__ == "__main__":
    main()