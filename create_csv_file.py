import os
import cv2
import csv
import numpy as np
import time


zebra_path = "C://Users/79376/python/dataset/zebra"
dataset_path ="C://Users/79376/python/dataset"
bay_horse_path = "C://Users/79376/python/dataset/bay_horse"
second_dataset_path = "C://Users/79376/python/dataset2"
third_dataset_path = "C://Users/79376/python/dataset3"

annotation_path = "C://Users/79376/python/annotation.csv"
annotation_2_path = "C://Users/79376/python/annotation2.csv"
test_path = "C://Users/79376/python/test.csv"


images = []


for filename1 in os.listdir(zebra_path):
    images.append(cv2.imread(os.path.join(zebra_path, filename1)))


def is_similar(image1: np.ndarray, image2: np.ndarray) -> bool:
    '''Сравнивает две картинки'''
    return image1.shape == image2.shape and not(np.bitwise_xor(image1,image2).any())


def defining_mark(image: np.ndarray) -> bool:
    '''Проверяет является ли картинка проверяемым типом'''
    for im in images:
        if(is_similar(im, image)):
            return True


    return False


def create_annotation_file(path: str, path_destination: str) -> None:
    '''Записывает объекты из передaнного файла в csv-файл'''
    with open(path_destination, mode = "a", encoding = 'utf-8') as w_file:
        file_writer = csv.writer(w_file, 
                                 delimiter = "|", lineterminator = "\r")
        
        for filename1 in os.listdir(path):
            
            if (defining_mark(cv2.imread(os.path.join(path, filename1)))):
                file_writer.writerow([os.path.join(path, filename1), 'zebra'])
            else:
                file_writer.writerow([os.path.join(path, filename1), 'bay_horse'])   


if __name__ == "__main__":
    create_annotation_file(zebra_path, annotation_path)  
    create_annotation_file(bay_horse_path, annotation_path)  
    create_annotation_file(second_dataset_path, annotation_path)
    create_annotation_file(third_dataset_path, annotation_path)

    print(time.perf_counter())
    create_annotation_file(third_dataset_path, annotation_2_path)
    print(time.perf_counter())
  

