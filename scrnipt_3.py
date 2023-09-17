import csv
import os


def check_file(path_sc3: str) -> None:
    """
    The function accepts a file, if there is no file, it creates it.

    :param path_sc3: file.
    :return: None.
    """
    if not os.path.isdir(path_sc3):
        os.mkdir(path_sc3)


def sort_week(all_date: list, path_to_csv: str) -> None:
    """
    The function that takes data and sorts it by week

    :param all_data: list with all dates.
    :param path_to_csv: folder path.
    :return: None.
    """
    day = len(all_date)
    week = []
    count = 0
    while (day != 0):
        if (day >= 7):
            for i in range(7):
                week.append(all_date[count])
                count += 1
            sort_file(week, path_to_csv)
            day -= 7
        elif (day < 7):
            for i in range(day):
                week.append(all_date[count])
                count += 1
            sort_file(week, path_to_csv)
            day = 0
        week = []


def sort_file(week: list, path_to_csv: str) -> None:
    """
    The function that takes weeks and sorts them by files.

    :param week: list with weeks.
    :param path_to_csv: folder path.
    :return: None.
    """
    date_1 = week[0][0][8:10]
    date_2 = week[-1][0][8:10]
    name_file = path_to_csv + '/scrnipt_3/' + str(week[0][0][:4]) + "_" + str(
        week[0][0][5:7]) + "_" + date_1 + "_" + date_2 + ".csv"
    print(name_file)
    with open(name_file, 'w', newline='', encoding='utf-8') as file_scr3:
        writer = csv.writer(file_scr3)
        for i in range(len(week)):
            writer.writerow(week[i])


def run_3(path_to_csv: str=os.path.join("C:/", "PYTHON", "PTM-1", "File_folder")) -> None:
    """
    The main function of the script.

    Write a script that will split the original csv file into N files, 
    where each individual file will correspond to one week. 
    Files are named by the first and last date they contain.

    :param path_to_csv: the path to the file folder
    :return: None
    """
    path_sc3 = "File_folder/scrnipt_3"
    check_file(path_sc3)
    set1 = set()
    with open(path_to_csv + '/dataset.csv', 'r', newline='', encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            set1.add(row[0][:4])
    set1 = sorted(list(set1), reverse=True)

    with open(path_to_csv + '/dataset.csv', 'r', newline='', encoding='utf-8') as csvfile:
        file_reader = list(csv.reader(csvfile))
        all_data = []
        month, year = 9, 2022
        while (year != 2009):
            for row in file_reader:
                if (int(row[0][5:7]) == month):
                    all_data.append(row)
                elif (int(row[0][5:7]) > month):
                    month = int(row[0][5:7])
                    year -= 1
                elif (int(row[0][5:7]) < month):
                    print(month, year)
                    month -= 1
                    if (month == 1):
                        pass
                    sort_week(all_data, path_to_csv)
                    all_data = []
                    all_data.append(row)

    print("\nscript_3 has finished working\n")


  