import os


class DataIter:
    def __init__(self, cls: str, dataset_path: str):
        self.mark = cls
        self.path = dataset_path
        self.path_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if os.path.isfile(self.path + self.mark + "/" + str(self.path_num).zfill(4) + ".txt"):
            self.path_num += 1
            return self.path + self.mark + "/" + str(self.path_num-1).zfill(4) + ".txt"
        else:
            print("None")
            raise StopIteration
