import csv


def url(path: str, name: str, label: str):
    """Функция принимает путь к фалу: path
    метку класса по этому пути: name
    метку с которой нужжно сравнить: label"""
    if name == label:
        return path
    else:
        return None


def path(label: str, file_name: str) -> list:
    """Функция принимает метку класса: label и имя файла: file_name"""
    data = []
    with open(file_name) as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        for i in file_reader:
            path = url(i[0], i[2], label)
            if path != None:
                data.append(path)
    return data


def main():
    data_1 = path("tiger", "data.csv")
    data_2 = path("leopard", "data_copy.csv")
    for i in range(10):
        print(data_1[i])
    for i in range(10):
        print(data_2[i])


if __name__ == "__main__":
    main()
