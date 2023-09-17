import os
class Iterator:

    def __init__(self, name_of_file: str):
        self.name_of_file = name_of_file
        self.counter = 0
        self.list = []
        file = open(self.name_of_file, "r", encoding='utf-8')
        for row in file:
            self.list.append(row)
        file.close
    def __iter__(self):
        return self
    def __next__(self) -> int:
        if self.counter < len(self.list):
            tmp = self.list[self.counter]
            self.counter += 1
            return tmp
        else:
            raise StopIteration

def run_5(path_to_csv: str=os.path.join("C:/", "PYTHON", "PTM-1", "File_folder")) -> None:
    '''Основная функция работы скрипта'''
    file_name = path_to_csv + "/scrnipt_2/20220901_20220130.csv"
    s_iter1 = Iterator(file_name)
    for val in s_iter1:
        print(val, end="")
    print("\nscript_5 has finished working\n")