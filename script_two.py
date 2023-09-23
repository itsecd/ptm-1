import csv
import os
from tqdm import tqdm
from os.path import relpath
import first_script

file_name = "test_csv.csv"
file_name_two = "test_csv_two.csv"
from tqdm.notebook import tqdm_notebook


def script_two(path_dir: str) -> str:
    out_directory = os.path.dirname(__file__)
    os.chdir(path_dir)
    with open(file_name_two, mode="w") as w_file:
        writer = csv.writer(w_file, dialect='excel', delimiter=",", lineterminator="\r")
        writer.writerow(("absolut path", "relativ path", "quote"))  # Заголовки столбца
    if not os.path.isfile(file_name):   first_script.first_script(path_dir)
    with open("test_csv.csv", "r") as fh:
        reader = csv.reader(fh)
        spisok = list(reader)  # надо сделать приведение к list, так как сsv вернет итератор
        if not os.path.isdir("dataset_two"):
            os.makedirs("dataset_two")
        pbar = tqdm(spisok, ncols=100, colour='green')
        content = False
        for element in pbar:
            if content:
                #element2 = element[1].split("/")
                #element2 = element2[1] + element2[2]
                print(element[0])
                os.chdir(out_directory)
                with open(element[1], "rb") as f:
                    text = f.read()
                    namefile = element[1].split("/")
                os.chdir(path_dir)
                with open(os.path.join("dataset_two", element[2] + "_" + namefile[2]), "wb") as f:
                    f.write(text)
                with open(file_name_two, mode="a") as w_file:
                    writer = csv.writer(w_file, dialect='excel', delimiter=",", lineterminator="\r")
                    writer.writerow([path_dir + "/dataset_two/" + element[2] + "_" + namefile[2],
                                     path_dir + "dataset_two/" + element[2] + "_" + namefile[2], element[2]])

            content = True