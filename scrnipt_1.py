import csv 
import os

def check_file(path_fol: str, path_sc1: str) -> None:
    '''Принимает имя пути, если файла нет создает''' 
    if not os.path.isdir(path_fol): os.mkdir(path_fol) 
    if not os.path.isdir(path_sc1): os.mkdir(path_sc1)

def run_1(path_to_csv: str=os.path.join("C:/", "PYTHON", "PTM-1", "File_folder")) -> None:
    '''Основная функция работы скрипта''' 
    path_fol, path_sc1 = "File_folder", "File_folder/scrnipt_1" 
    check_file(path_fol, path_sc1) 
    list1 = [] 
    with open(path_to_csv + '/dataset.csv', 'r', encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile) 
        for row in file_reader: 
            list1.append(row)

    with open(path_to_csv + "/scrnipt_1/X.csv", 'w', newline='', encoding='utf-8') as csvfile_x:
        for i in range(0, len(list1)):
            all_data = [list1[i][0]]
            writer = csv.writer(csvfile_x)
            writer.writerow(all_data)

    with open(path_to_csv + "/scrnipt_1/Y.csv", 'w', newline='', encoding='utf-8') as csvfile_y:
        for i in range(0, len(list1)):
            all_data = list1[i][1:]
            writer = csv.writer(csvfile_y)
            writer.writerow(all_data)

    print("\nscript_1 has finished working\n")