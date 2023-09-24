import os
import csv

from typing import Optional


class Iterator_Task1:
    """It's constructor"""
    def __init__(self, path: str) -> None:
        self.file_names = os.listdir(os.path.join('dataset', path))
        self.counter = 0
        self.limit = len(self.file_names)
        self.path = path


    def __next__(self) -> Optional[str]:
        """It's method that return next iterator"""
        if self.counter < self.limit:
            self.counter += 1
            return os.path.join(self.path, self.file_names[self.counter-1])
        else:
            raise StopIteration


    def __iter__(self):
        return self


class Iterator_Task2:
    """It's constructor"""
    def __init__(self, path: str) -> None:
        self.file_names = os.listdir(os.path.join(path))
        self.limit = len(self.file_names)
        self.counter = 0
        self.path = path


    def __next__(self) -> Optional[str]:
        """It's method that return next iterator"""
        if self.counter < self.limit:
            self.counter += 1
            return os.path.join(self.path, self.file_names[self.counter - 1])
        else:
            raise StopIteration


    def __iter__(self):
        return self


class IteratorTask3:
    """It's constructor"""
    def __init__(self, class_name: str, path: str, annotation_name: str) -> None:
        self.file_names = list()
        with open(os.path.join(path, annotation_name), encoding='UTF-16') as file:
            reader = csv.reader(file, delimiter=',')
            for file_info in reader:
                if file_info[1] == class_name:
                    self.file_names.append()
        self.limit = len(self.file_names)
        self.counter = 0
        self.path = path


    def __next__(self) -> Optional[str]:
        """It's method that return next iterator"""
        if self.counter < self.limit:
            self.counter += 1
            return os.path.join(self.path, self.file_names[self.counter - 1])
        else:
            raise StopIteration


    def __iter__(self):
        return self