import os


class DataIter:
    def __init__(self, cls: str, dataset_path: str):
        self.mark = cls
        self.path = dataset_path
        self.path_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        name = "".join([str(self.path_num).zfill(4), ".txt"])
        full_path = os.path.join(self.path, self.mark, name)
        if os.path.isfile(full_path):
            self.path_num += 1
            return full_path
        else:
            print("None")
            raise StopIteration
