import csv


class SimpleIterator:
    """Класс итератор - задается итерируемый объект и файл"""

    def __init__(self, label: str, file_name: str):
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


def main():
    s = SimpleIterator("leopard", "data.csv")
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))


if __name__ == "__main__":
    main()
