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
    '''функция next, принимает count, выводит значение по индексу'''
    with open(path_to_csv+'/dataset.csv', 'r', encoding='utf-8') as csvfile:
        file_reader = list(csv.reader(csvfile))
        if (file_reader[count] == None):
            return None
        else:
            return file_reader[count]
            #print(*file_reader[count])

def work_0(date: datetime.date,  path_to_csv: str) -> None:
    "принимает данные, ищет их в файле соответствующего скрипта"
    with open(path_to_csv+"/dataset.csv", mode='r', encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile) 
        for row in file_reader:
            if (row[0] == str(date)):  # если одинаковые даты - выводим
                print(*row)
                break
        else:
            return None

def work_1(date: datetime.date,  path_to_csv: str) -> None:
    "принимает данные, ищет их в файле соответствующего скрипта"
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

def work_2(date: datetime.date, path_to_csv: str) -> None:
    "принимает данные, ищет их в файле соответствующего скрипта"
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

def work_3(date: datetime.date, path_to_csv: str) -> None:
    "принимает данные, ищет их в файле соответствующего скрипта"
    ways = os.listdir(path_to_csv+"/scrnipt_3")
    list1 = []
    date = str(date)
    date = re.sub(r'[-]', '_', date)
    for i in range(len(ways)):  # выбираем одинаковые года и месяцы, записываем файлы в лист
        if (ways[i][:7] == date[:7]):
            list1.append(ways[i])
    if (list1 == None): return None
    for i in range(len(list1)):
        if (int(list1[i][11:13]) >= int(date[8:10]) >= int(
                list1[i][8:10])):  # если число находится в диапозоне недели то выводим его
            with open(path_to_csv + "/scrnipt_3/" + list1[i], 'r', encoding='utf-8') as csvfile:
                file_reader = csv.reader(csvfile)
                date = re.sub(r'[_]', '-', date)
                for row in file_reader:
                    if (row[0] == date):
                        print(*row)
                        break
    else:
        return None

def run_4(path_to_csv: str=os.path.join("C:/", "PYTHON", "PythonLab2", "File_folder")) -> None:
    '''Основная функция работы скрипта'''
    date = datetime.date(2022, 9, 7)
    work_0(date, path_to_csv)
    work_1(date, path_to_csv)
    work_2(date, path_to_csv)
    work_3(date, path_to_csv)

    with open(path_to_csv+'/dataset.csv', 'r', encoding='utf-8') as csvfile:
        count = 0
        while (count != 50):
            next(path_to_csv, count)
            count += 1

    print("\nscript_4 has finished working\n")