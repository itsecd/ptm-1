import os


class MyIter:
    def __init__(self, cls: str):
        self.mark = cls
        self.path_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if os.path.isfile("dataset/" + self.mark + "/" + str(self.path_num).zfill(4) + ".txt"):
            self.path_num += 1
            return "dataset/" + self.mark + "/" + str(self.path_num-1).zfill(4) + ".txt"
        else:
            print("None")
            raise StopIteration
