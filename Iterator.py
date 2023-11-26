import os
import csv


annotation_2_path = "C://Users/79376/python/annotation2.csv"


class Iterator:
    def __init__(self, mark: str) -> None:
        
        self.counter = 0
        self.mark = mark
        with open(annotation_2_path, encoding = 'utf-8') as r_file:
            self.file_reader = list(csv.reader(r_file, delimiter = '|'))
        self.limit = len(self.file_reader)

    def __iter__(self):
        return self

    def __next__(self):

        if(self.counter < self.limit):
            self.counter += 1
            while (self.counter < self.limit) and (self.file_reader[self.counter][2] != self.mark):    
                self.counter += 1
            
            if (self.counter == self.limit):
                raise StopIteration
            
            return self.file_reader[self.counter][0]
        else:
            raise StopIteration



if __name__ == '__main__':
    picture = Iterator("zebra")
    print(next(picture))
    print(next(picture))
    print(next(picture))
    print(next(picture))
    
