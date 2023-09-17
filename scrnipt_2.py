import csv
import os
import re


def check_file(path_sc2: str) -> None:
    """
    The function accepts a file, if there is no file, it creates it.

    :param path_sc2: file.
    :return: None.
    """
    if not os.path.isdir(path_sc2):
        os.mkdir(path_sc2)


def write_file(date_1: str, date_2: str, list_years: list, path_to_csv: str) -> None:
    """
    The function that creates a csv and writes data from list_years.

    :param date_1: start date.
    :param date_2: end date.
    :param list_years: list with dates.
    :param path_to_csv: folder path.
    :return: None.
    """
    name_file = path_to_csv + '/scrnipt_2/' + date_1 + "_" + date_2 + ".csv"
    print("create file: ", name_file)
    with open(name_file, 'w', newline='', encoding='utf-8') as namefile:
        writer = csv.writer(namefile)
        for i in range(len(list_years)):
            writer.writerow(list_years[i])


def run_2(path_to_csv: str=os.path.join("C:/", "PYTHON", "PTM-1", "File_folder")) -> None:
    """
    The main function of the script.

    Write a script that will split the original csv file into N files,
    where each individual file will correspond to one year.
    Files are named by the first and last date they contain.
    (if the file contains data from the first of January 2001 to December 31, 2001, 
    then the file is called 20010101_20011231.csv)

    :param path_to_csv: the path to the file folder.
    :return: None.
    """
    path_sc2 = path_to_csv + "/scrnipt_2"
    check_file(path_sc2)
    set1 = set()
    list1_years = []
    with open(path_to_csv + '/dataset.csv', 'r',  encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            set1.add(row[0][:4])
    set1 = sorted(list(set1), reverse=True)
    n = len(set1)

    with open(path_to_csv + '/dataset.csv', 'r', encoding='utf-8') as csvfile:
        file_reader = list(csv.reader(csvfile))
        for i in range(n):
            for j in range(len(file_reader)):
                if (file_reader[j][0][:4] == set1[i]): list1_years.append(file_reader[j])
            print(list1_years[0][0])
            date_1 = str(re.sub(r'[-]', '', list1_years[0][0]))
            date_2 = str(re.sub(r'[-]', '', list1_years[-1][0]))
            write_file(date_1, date_2, list1_years, path_to_csv)
            list1_years = []

    print("\nscript_2 has finished working\n")
