import os
from shutil import copy


zebra_path = "C://Users/79376/python/dataset/zebra"
dataset_path ="C://Users/79376/python/dataset"
bay_horse_path = "C://Users/79376/python/dataset/bay_horse"
second_dataset_path = "C://Users/79376/python/dataset2"

def create_dataset(source_path: str, destination_path: str) -> None:
    '''Создает новый датасет по второму заданию'''
    if not os.path.exists(destination_path):
        os.mkdir(destination_path)  

    files = []
    for filename1 in os.listdir(source_path):
        files.append((os.path.join(source_path, filename1)))

    mark = os.path.split(source_path)

    for filename in files:
        copy(filename, destination_path, follow_symlinks=True)
        number = os.path.split(filename)
        os.rename(os.path.join(destination_path, number[1]), os.path.join(destination_path, mark[1] + number[1]))

    



if __name__ == '__main__':
    
    create_dataset(zebra_path, second_dataset_path)
    create_dataset(bay_horse_path, second_dataset_path)