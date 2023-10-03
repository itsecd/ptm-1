import csv
import os


def path(label: str, dataset_name: str) -> list:
    """Функция принимает метку класса: label и имя файла: file_name"""
    data = []
    array = os.listdir(dataset_name)
    for i in array:
        name = i.find(label)
        if name != -1:
            data.append(os.path.abspath(i))
    return data


def main():
    data = path("tiger", "dataset_copy")
    for i in range(10):
        print(data[i])


if __name__ == "__main__":
    main()
