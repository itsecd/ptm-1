import os 
import csv


annotation_2_path = "C://Users/79376/python/annotation2.csv"

def get_picture(mark:str, counter:int) -> list:
    '''возвращает путь до следующего элемента нужного класса и номер его строки'''
    with open(annotation_2_path, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter='|')

        count = 0
        for row in file_reader:
            if (count > counter):
                if (row[2] == mark):
                    return (row[0], count)
            count += 1
        return (None, -1)

if __name__ == '__main__':
    count = 0
    a = get_picture("zebra", 120)
    count = a[1]
    print(a[0])