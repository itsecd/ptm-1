import csv

class Iterator:

    """Класс итератор - задаётся итерируемый объект и датасет"""
    
    def __init__(self, label: str,file: str) -> None:
        self.label = label
        self.file = file
        self.score = 0
        self.data = []
        with open(self.file) as reading_file:
            file_reader = csv.reader(reading_file, delimiter=";")
            for i in file_reader:
                if i[2] == self.label:
                    self.data.append(i[0])
            self.full = len(self.data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.score < self.full:
            i = self.score
            self.score += 1
            return self.data[i]
        else:
            raise StopIteration

def main():
    instance = Iterator("dog", "dataset_csv.csv")
    print(next(instance))
    print(next(instance))
    print(next(instance))
    print(next(instance))

if __name__ == "__main__":
    main()