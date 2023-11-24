import csv
import os

def Creating_csv(path: str,path_new: str) -> None:
    
    """Функция принимает путь к файлам: path и путь к новой директории: path_new"""

    data = []
    
    source = os.listdir(path + "/")
    
    for i in source:
        source_info = os.listdir(path + "/" + i)
        for j in source_info:
            absolute = os.path.abspath(path + "/" + i + "/" + j)
            regarding = os.path.relpath(path + "/" + i + "/" + j)
            data.append([absolute, regarding, i])
    with open(path_new + ".csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(data)
def main():
    Creating_csv("dataset", "dataset_csv")

if __name__ == "__main__":
    main()