import csv

class Iterator:
    def __init__(self, directory: str, name: str):
        """Сonstructor of the class object, return NONE.
        Args:
            directory (str): full path to the folder.
            name (str): object class.
        """
        self.directory = directory
        self.name = name
        self.count = -1
        self.read_list = []

        with open(directory, "r", encoding="utf-8") as f:
            r = csv.DictReader(
                f, fieldnames=["Absolut_path", "Relative_patch", "Class"], delimiter="|")

            for i in r:
                if i["Class"] == name:
                    self.read_list.append(i["Absolut_path"])

    def __iter__(self):
        """Return iterator object.
        Returns:
            self: iterstor object.
        """
        return self

    def __next__(self):
        """Return the next element in the sequence.
        Raises:
            StopIteration: stopping the iterator.
        Returns:
           str: patch to the file.
        """
        if self.count < len(self.read_list):
            self.count += 1
            return self.read_list[self.count]

        elif self.count == len(self.read_list):
            raise StopIteration


def main():
    """Separates code blocks."""
    s = Iterator("D:\Lab Python\dataset_2copy.csv", "rose")

    print(type(next(s)))
    print(next(s))
    print(next(s))

    t = Iterator("D:\Lab Python\dataset_2copy.csv", "tulip")

    print(next(t))
    print(next(t))
    print(next(t))

if __name__ == "__main__":
	main()
