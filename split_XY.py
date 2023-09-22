import csv 
import os


def check_file(path_fol: str, path_sc1: str) -> None:
    """
    The function accepts a folder and a file, if there is no folder, 
    it creates it, if there is no file, it creates it.

    :param path_fol: folder.
    :param path_sc1: file.
    :return: None.
    """
    if not os.path.isdir(path_fol):
        os.mkdir(path_fol)
    if not os.path.isdir(path_sc1):
        os.mkdir(path_sc1)


def run_split_XY(path_to_csv: str=os.path.join("C:/", "PYTHON",
                                         "PTM-1", "File_folder")) -> None:
    """
    The main function of the script.

    :param path_to_csv: the path to the file folder.
    :return: None.
    """
    path_fol, path_sc1 = "File_folder", "File_folder/dataset_XY" 
    check_file(path_fol, path_sc1) 
    list_tmp = [] 
    with open(path_to_csv + '/dataset.csv', 'r',
               encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile) 
        for row in file_reader: 
            list_tmp.append(row)

    with open(path_to_csv + "/dataset_XY/X.csv", 'w',
               newline='', encoding='utf-8') as csvfile_x:
        for i in range(0, len(list_tmp)):
            all_data = [list_tmp[i][0]]
            writer = csv.writer(csvfile_x)
            writer.writerow(all_data)

    with open(path_to_csv + "/dataset_XY/Y.csv", 'w',
               newline='', encoding='utf-8') as csvfile_y:
        for i in range(0, len(list_tmp)):
            all_data = list_tmp[i][1:]
            writer = csv.writer(csvfile_y)
            writer.writerow(all_data)

    print("\nsplit_XY.py has finished working\n")