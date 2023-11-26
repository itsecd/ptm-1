import os
from shutil import copy
from random import randint


zebra_path = "C://Users/79376/python/dataset/zebra"
dataset_path ="C://Users/79376/python/dataset"
bay_horse_path = "C://Users/79376/python/dataset/bay_horse"
second_dataset_path = "C://Users/79376/python/dataset2"
third_dataset_path = "C://Users/79376/python/dataset3"


def check_number(number: int, path: str) -> bool:
    '''Проверяет на совпадение сгенерированного номера с уже существующими'''
    files = []
    for filename1 in os.listdir(path):
        files.append((os.path.join(path, filename1)))
    
    for i in files:
        if os.path.split(i)[1] == str(number).zfill(5) + '.jpg':
            return False
    
    return True


def create_dataset(source_path: str, destination_path: str) -> None:
    '''Создает новый датасет по третему заданию'''
    if not os.path.exists(third_dataset_path):
        os.mkdir(third_dataset_path)  
    
    files = []
    for filename1 in os.listdir(source_path):
        files.append((os.path.join(source_path, filename1)))

    for filename2 in files:
        filename = os.path.split(filename2)[1]
        copy(filename2, destination_path, follow_symlinks=True)
        while True:
            number = randint(0, 10000)
            if check_number(number, destination_path):
                break
        os.rename(os.path.join(destination_path, filename), 
                  os.path.join(destination_path, 
                               str(number).zfill(5) + '.jpg'))


if __name__ == '__main__':

    create_dataset(second_dataset_path, third_dataset_path)