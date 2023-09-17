import os
import csv
import re
import datetime
from typing import List, Optional


def next(path_to_csv: str, count: int) -> Optional[List[str]]:
    """
    the next function takes count and outputs dates.

    the next() function, 
    which will return data for the earliest possible date 
    on the first call (the tuple (date, data) is returned), 
    and at each next call, the data for the next date in order. 
    If there is a date for which there is no data, 
    then it is ignored and data is returned for the next valid date.

    :param count: number of dates.
    :param path_to_csv: the path to the file folder
    :return: None
    """
    with open(path_to_csv+'/dataset.csv', 'r', 
              encoding='utf-8') as csvfile:
        file_reader = list(csv.reader(csvfile))
        if (file_reader[count] == None):
            return None
        else:
            return file_reader[count]


def search_dataset(date: datetime.date,  path_to_csv: str) -> None:
    """
    the function accepts data, searches for it in 
    the file of the corresponding script

    :param date: the date by sorted.
    :param path_to_csv: the path to the file folder
    :return: None
    """
    with open(path_to_csv+"/dataset.csv", mode='r',
               encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile) 
        for row in file_reader:
            if (row[0] == str(date)):
                print(*row)
                break
        else:
            return None


def search_scrnipt_1(date: datetime.date,  path_to_csv: str) -> None:
    """
    the function accepts data, searches for it in 
    the file of the corresponding script

    :param date: the date by sorted.
    :param path_to_csv: the path to the file folder
    :return: None
    """
    with open(path_to_csv +'/scrnipt_1/X.csv', 'r',
               encoding='utf-8') as csvfile:
        file_reader = list(csv.reader(csvfile))
        for i in range(len(file_reader)):
            if (file_reader[i][0] == str(
                    date)):
                tmp = i
                break
        else:
            return None
    with open(path_to_csv+'/scrnipt_1/Y.csv', 'r',
               encoding='utf-8') as csvfile:
        file_reader = list(csv.reader(csvfile))
        print(*file_reader[tmp])


def search_scrnipt_2(date: datetime.date, path_to_csv: str) -> None:
    """
    the function accepts data, searches for it in 
    the file of the corresponding script

    :param date: the date by sorted.
    :param path_to_csv: the path to the file folder
    :return: None
    """
    ways = os.listdir(path_to_csv+"/scrnipt_2")
    date = str(date)
    for i in range(len(ways)):
        if (ways[i][:4] == date[:4]):
            with open(path_to_csv + "/scrnipt_2/" + ways[i], 'r',
                       encoding='utf-8') as csvfile:
                file_reader = csv.reader(csvfile)
                for row in file_reader:
                    if (row[0] == date):
                        print(*row)
                        break
    else:
        return None


def search_scrnipt_3(date: datetime.date, path_to_csv: str) -> None:
    """
    the function accepts data, searches for it in 
    the file of the corresponding script

    :param date: the date by sorted.
    :param path_to_csv: the path to the file folder
    :return: None
    """
    ways = os.listdir(path_to_csv+"/scrnipt_3")
    list_tmp = []
    date = str(date)
    date = re.sub(r'[-]', '_', date)
    for i in range(len(ways)):  
        if (ways[i][:7] == date[:7]):
            list_tmp.append(ways[i])
    if (list_tmp == None): return None
    for i in range(len(list_tmp)):
        if (int(list_tmp[i][11:13]) >= int(date[8:10]) >= int(
                list_tmp[i][8:10])):  
            with open(path_to_csv + "/scrnipt_3/" + list_tmp[i], 'r', 
                      encoding='utf-8') as csvfile:
                file_reader = csv.reader(csvfile)
                date = re.sub(r'[_]', '-', date)
                for row in file_reader:
                    if (row[0] == date):
                        print(*row)
                        break
    else:
        return None


def run_4(path_to_csv: str=os.path.join("C:/", "PYTHON",
                                         "PTM-1", "File_folder")) -> None:
    """
    The main function of the script.

    a script containing a function
    that accepts a date as input (datetime type) and 
    returns data for this date (from a file)
    or None if there is no data for this date. 
    The function should be presented in four versions, depending on
    the type of input files from which the data will be read (paragraphs 0-3). 

    :param path_to_csv: the path to the file folder
    :return: None
    """
    date = datetime.date(2022, 9, 7)
    search_dataset(date, path_to_csv)
    search_scrnipt_1(date, path_to_csv)
    search_scrnipt_2(date, path_to_csv)
    search_scrnipt_3(date, path_to_csv)

    with open(path_to_csv+'/dataset.csv', 'r',
               encoding='utf-8') as csvfile:
        count = 0
        while (count != 50):
            next(path_to_csv, count)
            count += 1

    print("\nscript_4 has finished working\n")