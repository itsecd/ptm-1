import os


def sort_by_label(label: str, dataset_name: str) -> list:
    """Function sorts the directory by label

    Args:
        label (str): sort label
        dataset_name(str): sort folder

    Returns:
        list[str]: sorted list
    """
    data = []
    array = os.listdir(dataset_name)
    for i in array:
        name = i.find(label)
        if name != -1:
            data.append(os.path.abspath(i))
    return data


if __name__ == "__main__":
    data = sort_by_label("tiger", "dataset_copy")
    for i in range(10):
        print(data[i])