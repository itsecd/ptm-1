import csv
import os
import random
import shutil
import tqdm


def copy_dataset(directory_obj: str, c_directory_obj: str, name: str) -> None:
    """Copies all files from one folder to another, return NONE.
    Args:
        directory_obj (str): the path of the source folder.
        c_directory_obj (str): folder path to copy.
        name (str): object class.
    """
    c_directory_obj1 = f"{c_directory_obj}dataset_3"
    if not os.path.isdir(c_directory_obj1):
        os.makedirs(c_directory_obj1)
    r_list = list(range(1, 10001))
    random.shuffle(r_list)
    r_list = [str(i) for i in r_list] 
    c_data = os.listdir(c_directory_obj1)
    if c_data:
        c_data = list(map(lambda sub:int(''.join([ele for ele in sub if ele.isnumeric()])), c_data))
        c_data = [str(i) for i in c_data]
        for i in c_data:
            r_list.remove(i)     
    j = 0
    copy_list = []
    data = os.listdir(directory_obj)
    for i in tqdm.tqdm(data):
        so = str(r_list[j])
        so = f"{name}.{so}"
        copy_list.append(so)
        shutil.copy(directory_obj + "\\" + i, c_directory_obj1 + "\\" + so + '.jpeg')
        j += 1
    write_csv_copy(c_directory_obj1, name, copy_list)


def write_csv_copy(c_directory_obj: str, name: str, copy_list: list) -> None:
    """Writes the absolute and relative path of the image to csv, return NONE.
    Args:
        c_directory_obj (str): folder path to copy.
        name (str): object class.
        copy_list (list): numbers of copied objects.
    """
    file = f"{c_directory_obj}rand.csv"
    f = open(file, "a", encoding="utf-8", newline="")
    f_writer = csv.DictWriter(f, fieldnames=["Absolut_path", "Relative_patch", "Class"], delimiter="|")
    r_directory_obj = "dataset_3"
    for i in copy_list:
        f_writer.writerow({"Absolut_path": c_directory_obj + "\\" + i, "Relative_patch":  r_directory_obj + "\\" + i, "Class": name})


def main() -> None:
    """Separates code blocks."""
    c_directory = "D:\Lab Python\\"
    directory_rose = "D:\Lab Python\Lab_1\dataset\ rose"
    directory_tulip = "D:\Lab Python\Lab_1\dataset\ tulip"
    copy_dataset(directory_rose, c_directory, "rose")
    copy_dataset(directory_tulip, c_directory, "tulip")


if __name__ == "__main__":
	main()
