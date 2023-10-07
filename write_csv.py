import csv
import os

def write_csv(directory_obj: str, file: str, name: str):
    """Writes the absolute and relative path of the image to csv, return NONE.
    Args:
        directory_obj (str): full path to the folder.
        file (str): the path to the file to save.
        name (str): object class.
    """
    file = f"{file}annotation.csv"
    f = open(file, "a", encoding="utf-8", newline="")
    f_writer = csv.DictWriter(f, fieldnames=["Absolut_path", "Relative_patch", "Class"], delimiter="|")

    data = os.listdir(directory_obj)
    r_directory_obj = "dataset"

    for i in data:
        f_writer.writerow({"Absolut_path": directory_obj + "\\" + i, "Relative_patch":  r_directory_obj + "\\" + name + "\\" + i, "Class": name})

def main():
    """Separates code blocks."""
    directory_rose = "D:\Lab Python\Lab_1\dataset\ rose"
    directory_tulip = "D:\Lab Python\Lab_1\dataset\ tulip"
    file = "D:\Lab Python\\"

    write_csv(directory_rose, file, "rose")
    write_csv(directory_tulip, file, "tulip")

if __name__ == "__main__":
	main()
