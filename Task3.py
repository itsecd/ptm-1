import os
import random  
import shutil
import csv

from typing import Optional  
from Task2 import create_dir


def get_element(class_name: str) -> Optional[str]:
    """This function gradually returns us files of class"""
    for file_name in os.listdir(os.path.join("dataset", class_name)):
        yield file_name


def create_randomname_file(annotation_name: str, dir_copy: str) -> None:
    """This function copies files from dataset to new directory for copies
    and renames files changing filename to a random number from 0 to 10000
    and create csv annotation with 2 parameters: new name of file and class of file"""
    file_number = list(range(10001))
    random.shuffle(file_number) 
    counter = 1
    create_dir(dir_copy)
    for dataset_class in os.listdir("dataset"):
        for file_name in get_element(dataset_class):
            shutil.copy(os.path.join(os.path.join("dataset", dataset_class), file_name),
                        os.path.join(dir_copy, f"{file_number[counter]}.jpg"))

            with open(os.path.join(dir_copy, annotation_name), mode="a", encoding="UTF-16", newline='') as file: 
                file_writer = csv.writer(file, delimiter=",")  
                file_writer.writerow([f"{file_number[counter]}.jpg", dataset_class])
            counter += 1


def run3(annotation_name: str, dir_copy: str) -> None:
    """This function calls previous function in main"""
    create_randomname_file(annotation_name, dir_copy)