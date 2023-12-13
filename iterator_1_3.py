import csv


class SimpleIterator:
    def __init__(self, label="leopard", file_name="data.csv"):
        self.label = label
        self.file_name = file_name
        self.counter = 0
        self.data = []
        with open(self.file_name) as r_file:
            file_reader = csv.reader(r_file, delimiter=";")
            for i in file_reader:
                if i[2] == self.label:
                    self.data.append(i[0])
            self.limit = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            i = self.counter
            self.counter += 1
            return self.data[i]
        else:
            raise StopIteration


if __name__ == "__main__":
    """using a SimpleIterator function"""
    s = SimpleIterator()
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))
