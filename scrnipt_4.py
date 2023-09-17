import os
import csv
import re
import datetime
from typing import List, Optional


# Написать скрипт, содержащий функцию, 
# принимающую на вход дату (тип datetime) и возвращающий данные для этой даты (из файла) или 
# None если данных для этой даты нет. Функция должна быть представлена в четырёх версиях в зависимости от 
# типа входных файлов, из которых будут прочитаны данные (пункты 0–3). 
# 
# Написать функцию next(), 
# которая будет при первом вызове возвращать данные для самой ранней возможной даты (возвращается кортеж (дата, данные)), 
# а при каждом следующем вызове данные для следующей по порядку даты. Если попадается дата, для которой данные отсутствуют, 
# то она игнориуруется и возвращаются данные для следующей валидной даты.

def next(path_to_csv: str, count: int) -> Optional[List[str]]:
    """
    the next function takes count and outputs dates.

    :param count: number of dates.
    :param path_to_csv: the path to the file folder
    :return: None
    """
    with open(path_to_csv+'/dataset.csv', 'r', encoding='utf-8') as csvfile:
        file_reader = list(csv.reader(csvfile))
        if (file_reader[count] == None):
            return None
        else:
            return file_reader[count]

def search_dataset(date: datetime.date,  path_to_csv: str) -> None:
    """
    the function accepts data, searches for it in the file of the corresponding script

    :param date: the date by sorted.
    :param path_to_csv: the path to the file folder
    :return: None
    """
    with open(path_to_csv+"/dataset.csv", mode='r', encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile) 
        for row in file_reader:
            if (row[0] == str(date)):
                print(*row)
                break
        else:
            return None

def search_scrnipt_1(date: datetime.date,  path_to_csv: str) -> None:
    """
    the function accepts data, searches for it in the file of the corresponding script

    :param date: the date by sorted.
    :param path_to_csv: the path to the file folder
    :return: None
    """
    with open(path_to_csv +'/scrnipt_1/X.csv', 'r', encoding='utf-8') as csvfile:
        file_reader = list(csv.reader(csvfile))
        for i in range(len(file_reader)):
            if (file_reader[i][0] == str(
                    date)):  # ищем в фале Х запоминаем номер строки, выводим данные по номеру строки в фале Y
                tmp = i
                break
        else:
            return None
    with open(path_to_csv+'/scrnipt_1/Y.csv', 'r', encoding='utf-8') as csvfile:
        file_reader = list(csv.reader(csvfile))
        print(*file_reader[tmp])

def search_scrnipt_2(date: datetime.date, path_to_csv: str) -> None:
    """
    the function accepts data, searches for it in the file of the corresponding script

    :param date: the date by sorted.
    :param path_to_csv: the path to the file folder
    :return: None
    """
    ways = os.listdir(path_to_csv+"/scrnipt_2")
    date = str(date)
    for i in range(len(ways)):
        if (ways[i][:4] == date[:4]):  # Ищем файл у которого аткой же год
            with open(path_to_csv + "/scrnipt_2/" + ways[i], 'r', encoding='utf-8') as csvfile:
                file_reader = csv.reader(csvfile)
                for row in file_reader:
                    if (row[0] == date):
                        print(*row)
                        break
    else:
        return None

def search_scrnipt_3(date: datetime.date, path_to_csv: str) -> None:
    """
    the function accepts data, searches for it in the file of the corresponding script

    :param date: the date by sorted.
    :param path_to_csv: the path to the file folder
    :return: None
    """
    ways = os.listdir(path_to_csv+"/scrnipt_3")
    list1 = []
    date = str(date)
    date = re.sub(r'[-]', '_', date)
    for i in range(len(ways)):  
        if (ways[i][:7] == date[:7]):
            list1.append(ways[i])
    if (list1 == None): return None
    for i in range(len(list1)):
        if (int(list1[i][11:13]) >= int(date[8:10]) >= int(
                list1[i][8:10])):  
            with open(path_to_csv + "/scrnipt_3/" + list1[i], 'r', encoding='utf-8') as csvfile:
                file_reader = csv.reader(csvfile)
                date = re.sub(r'[_]', '-', date)
                for row in file_reader:
                    if (row[0] == date):
                        print(*row)
                        break
    else:
        return None

def run_4(path_to_csv: str=os.path.join("C:/", "PYTHON", "PTM-1", "File_folder")) -> None:
    """
    The main function of the script.
    
    :param path_to_csv: the path to the file folder
    :return: None
    """
    date = datetime.date(2022, 9, 7)
    search_dataset(date, path_to_csv)
    search_scrnipt_1(date, path_to_csv)
    search_scrnipt_2(date, path_to_csv)
    search_scrnipt_3(date, path_to_csv)

    with open(path_to_csv+'/dataset.csv', 'r', encoding='utf-8') as csvfile:
        count = 0
        while (count != 50):
            next(path_to_csv, count)
            count += 1

    print("\nscript_4 has finished working\n")