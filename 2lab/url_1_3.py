import csv


def compare_label(path: str, name: str, label: str):
    """Function compares two labels
    
    Args:
        path (str): path to file
        name(str): path label
        label (str): label to compare with
    """
    if name == label:
        return path
    else:
        return None


def sort_by_label(label: str, file_name: str) -> list:
    """Function sorts csv file by label
    
    Args:
        label (str): sort label
        file_name(str): sort file

    Returns:
        list[str]: sorted list
    """
    data = []
    with open(file_name) as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        for i in file_reader:
            path = compare_label(i[0], i[2], label)
            if path:
                data.append(path)
    return data


def main():
    data_1 = sort_by_label("tiger", "data.csv")
    data_2 = sort_by_label("leopard", "data_copy.csv")
    for i in range(10):
        print(data_1[i])
    for i in range(10):
        print(data_2[i])


if __name__ == "__main__":
    main()