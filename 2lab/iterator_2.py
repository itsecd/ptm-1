import csv
import os


class SimpleIterator:
    """Класс итератор - задается итерируемый объект и dataset"""

    def __init__(self, label: str, dataset_name: str):
        self.label = label
        self.dataset_name = dataset_name
        self.counter = 0
        self.data = []
        array = os.listdir(self.dataset_name)
        for i in array:
            name = i.find(self.label)
            if name != -1:
                self.data.append(os.path.abspath(i))
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
    s = SimpleIterator("tiger", "dataset_copy")
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))


if __name__ == "__main__":
    main()
