from email import generator
import random
import os
import shutil
import csv

from task2 import create_dir

def get_element(class_name: str) -> generator:
    '''This function return us list of names in dataset class'''
    for file_name in os.listdir(os.path.join("dataset", class_name)):
        yield file_name

def create_randomname_file(annotation_name: str, dir_copy: str, dataset_path: str):
    '''This function create the copy of dataset in another directory with names which are random numbers 
    and create csv file with 2 parameters: file name(random number) and class of that file'''
    file_number = list(range(10001))
    random.shuffle(file_number)
    counter = 1
    create_dir(dir_copy)
    for dataset_class in os.listdir(dataset_path):
        for file_name in get_element(dataset_class):
            shutil.copy(os.path.join(os.path.join(dataset_path, dataset_class),
                        file_name),  os.path.join(dir_copy, f"{file_number[counter]}.jpg"))

            with open(os.path.join(dir_copy, annotation_name), mode="a", encoding="UTF-16", newline='') as file:
                file_writer = csv.writer(file, delimiter=",")
                file_writer.writerow(
                    [f"{file_number[counter]}.jpg", dataset_class])
            counter += 1

def run3(annotation_name: str, dir_copy: str):
    ''' This function call previous to run it in main'''
    create_randomname_file(annotation_name, dir_copy)
