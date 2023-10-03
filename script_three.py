import csv
import os
import random
import script_two
from tqdm import tqdm


def script_three(path_dir: str) -> None:
    """The function creates new files in the "dataset_three" directory
     based on files from "dataset_two",
     and also writes information about the created files to a CSV file.

    Args:
        path_dir (str): Path to the directory.
    """
    os.chdir(path_dir)
    file_name = "test_csv_three.csv"
    names = [i for i in range(10000)]
    out_directory = os.path.dirname(__file__)
    if not os.path.isdir("dataset_three"):
        os.makedirs("dataset_three")
    if not os.path.isdir("dataset_two"):
        script_two.script_two(path_dir)
    with open(file_name, mode="w") as w_file:
        writer = csv.writer(w_file, dialect="excel", delimiter=",", lineterminator="\r")
        writer.writerow(("absolut path", "relativ path", "quote"))
        pbar = tqdm(os.listdir("dataset_two"), ncols=100, colour="green")
        for element in pbar:
            name = random.choice(names)
            names.remove(name)
            with open(os.path.join("dataset_two", element), "rb") as f:
                text = f.read()
            with open(os.path.join("dataset_three", str(name) + ".txt"), "wb") as f:
                f.write(text)
            directory = os.path.join(path_dir, "dataset_three", str(name) + ".txt")
            writer.writerow([directory, os.path.join("dataset_two", element), element[0]])