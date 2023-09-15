import os
import random

import shutil
import csv


def create_dir_copy_randNames(class_name: str, path: str, dst: str) -> None:
    """Create array with rand num in 0 to 10000 length of names in source dir 
    and copy with that names to dst dir;
    and create descriprion .csv file like in task 1"""

    dir = os.path.join(path, class_name)
    names = os.listdir(dir)

    names = list(filter(lambda tmp: ".jpg" in tmp, names))

    tmp = random.sample(range(1, 10001), len(names))
    for i in range(len(names)):
        s = os.path.join(os.path.join(path, class_name), names[i])
        d = os.path.join(dst, f'{tmp[i]}.jpg')
        shutil.copy2(s, d)

    names = os.listdir(dst)
    with open(os.path.join(dst, f"{class_name}_annotation.csv"), 'w') as file_csv:
        names = list(filter(lambda tmp: ".jpg" in tmp, names))
        for i in names:
            file_csv.write(os.path.abspath(i) + "," +
                           os.path.join(dst, i) + "," + class_name)
            file_csv.write("\n")
    file_csv.close


def create_dir_copy_randNames_both(class_name1: str, class_name2: str, path: str, dst: str) -> None:
    """Create array with rand num in 0 to 10000 length of names in source dir 
    and copy with that names to dst dir;
    and create descriprion .csv file like in task 1"""

    dir = os.path.join(path, class_name1)
    names1 = os.listdir(dir)
    names1 = list(filter(lambda tmp: ".jpg" in tmp, names1))
    print("len 1", len(names1))
    dir = os.path.join(path, class_name2)
    names2 = os.listdir(dir)
    names2 = list(filter(lambda tmp: ".jpg" in tmp, names2))
    print("len 2", len(names2))
    tmp = random.sample(range(1, 10001), len(names1)+len(names2))
    names = names1 + names2
    print("Total len", len(names))
    for i in range(len(names1)):

        s = os.path.join(os.path.join(path, class_name1), names[i])
        d = os.path.join(dst, f'{tmp[i]}.jpg')
        shutil.copy2(s, d)
    for j in range(len(names1), len(names)):
        s = os.path.join(os.path.join(path, class_name2), names[j])
        d = os.path.join(dst, f'{tmp[j]}.jpg')
        shutil.copy2(s, d)
    names = os.listdir(dst)
    with open(os.path.join(dst, "both_random_annotation.csv"), 'w') as file_csv:
        names = list(filter(lambda tmp: ".jpg" in tmp, names))
        for k in range(len(names1)):
            file_csv.write(os.path.abspath(
                names[k]) + "," + os.path.join(dst, names[k]) + ","+class_name1)
            file_csv.write("\n")
        for m in range(len(names1), len(names)):
            file_csv.write(os.path.abspath(
                names[m]) + "," + os.path.join(dst, names[m]) + ","+class_name2)
            file_csv.write("\n")
    file_csv.close


def create_dir(path: str) -> str:
    """this function create 'dataset' directory
     in path gived by user
     and return path of new_dataset dir"""
    if not os.path.isdir(os.path.join(path, 'dataset')):
        os.mkdir(os.path.join(path, 'dataset'))
    return os.path.join(path, 'dataset')


def iterator3(class_name: str, path: str) -> str:
    """Just interater for direcrory"""
    tmp1 = []
    with open(os.path.join(path, 'annotation.csv')) as file:
        reader = csv.reader(file, delimiter=';', quotechar=';',
                            quoting=csv.QUOTE_MINIMAL)
        for it in reader:
            if (it[2] == class_name):
                tmp1.append(os.path.basename(it[1]))
        print(tmp1)
    file.close
    for i in range(len(tmp1)):
        yield tmp1[i]
    return None


class Iterator3_img:
    def __init__(self, path: str, class_name: str):
        """init function"""
        self.tmp1 = []
        with open(os.path.join(path, 'annotation.csv')) as file:
            reader = csv.reader(file, delimiter=';', quotechar=';',
                                quoting=csv.QUOTE_MINIMAL)
            for it in reader:
                if (it[2] == class_name):
                    self.tmp1.append(os.path.basename(it[1]))
        file.close
        self.limit = len(self.tmp1)
        self.counter = 0

    def __next__(self):
        """next operator"""
        if self.counter < self.limit:
            self.counter += 1
            return self.tmp1[self.counter - 1]
        else:
            raise StopIteration


def run_3(class_name: str, dst: str, class_name1="test1", class_name2="test2") -> None:
    """function for launching func"""
    print(3)
    tmp = create_dir(dst)
    create_dir_copy_randNames(class_name, tmp)
