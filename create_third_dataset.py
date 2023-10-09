import csv
import os
import random
import process_csv_file
from tqdm import tqdm


DATASET_TWO = "dataset_two"
DATASET_THREE = "dataset_three"
ABSOLUTE_PATH = "adsolut_path"
RELATIVE_PATH = "relative_path"
QUOTE = "quote"


def create_files(path_dir: str) -> None:
    """The function creates new files in the DATASET_THREE directory
     based on files from DATASET_TWO,
     and also writes information about the created files to a CSV file.

    Args:
        path_dir (str): Path to the directory.
    """
    os.chdir(path_dir)
    file_name = "test_csv_three.csv"
    names = [i for i in range(10000)]
    if not os.path.isdir(DATASET_THREE):
        os.makedirs(DATASET_THREE)
    if not os.path.isdir(DATASET_TWO):
        process_csv_file.process_file(path_dir)
    with open(file_name, mode="w") as w_file:
        writer = csv.writer(w_file, dialect="excel", delimiter=",", lineterminator="\r")
        writer.writerow((ABSOLUTE_PATH, RELATIVE_PATH, QUOTE))
        pbar = tqdm(os.listdir(DATASET_TWO), ncols=100, colour="green")
        for element in pbar:
            name = random.choice(names)
            names.remove(name)
            with open(os.path.join(DATASET_TWO, element), "rb") as f:
                text = f.read()
            with open(os.path.join(DATASET_THREE, str(name) + ".txt"), "wb") as f:
                f.write(text)
            directory = os.path.join(path_dir, DATASET_THREE, str(name) + ".txt")
            writer.writerow([directory, os.path.join(DATASET_TWO, element), element[0]])