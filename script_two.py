import csv
import os
import first_script
from tqdm import tqdm
from os.path import relpath
from tqdm.notebook import tqdm_notebook


FILE_NAME = "test_csv.csv"
SECOND_FILE_NAME = "test_csv_two.csv"
DATASET_TWO = "dataset_two"
ABSOLUTE_PATH = "adsolut_path"
RELATIVE_PATH = "relative_path"
QUOTE = "quote"


def process_file(path_dir: str) -> None:
    """The function is designed to process a CSV file.

    Args:
        path_dir (str): Path to the directory.
    """
    out_directory = os.path.dirname(__file__)
    os.chdir(path_dir)
    with open(SECOND_FILE_NAME, mode="w") as w_file:
        writer = csv.writer(w_file, dialect="excel", delimiter=",", lineterminator="\r")
        writer.writerow((ABSOLUTE_PATH, RELATIVE_PATH, QUOTE))
    if not os.path.isfile(FILE_NAME):   first_script.first_script(path_dir)
    with open(FILE_NAME, "r") as csv_file:
        reader = csv.reader(csv_file)
        list = list(reader)
        if not os.path.isdir(DATASET_TWO):
            os.makedirs(DATASET_TWO)
        pbar = tqdm(list, ncols=100, colour="green")
        content = False
        for element in pbar:
            if content:
                print(element[0])
                os.chdir(out_directory)
                with open(element[1], "rb") as f:
                    text = f.read()
                    namefile = element[1].split("/")
                os.chdir(path_dir)
                with open(os.path.join(DATASET_TWO, element[2] + "_" + namefile[2]), "wb") as f:
                    f.write(text)
                with open(SECOND_FILE_NAME, mode="a") as w_file:
                    writer = csv.writer(w_file, dialect="excel", delimiter=",", lineterminator="\r")
                    writer.writerow([path_dir + DATASET_TWO + element[2] + "_" + namefile[2],
                                     path_dir + DATASET_TWO + element[2] + "_" + namefile[2], element[2]])

            content = True