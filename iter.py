import csv


class Iterator:
    def __init__(self, directory: str, name: str) -> None:
        """Initializes an object of the class.
        Args:
            directory (str): Full path to the folder.
            name (str): Object class.
        """
        self.directory = directory
        self.name = name
        self.count = -1
        self.read_list = []
        with open(directory, "r", encoding="utf-8") as f:
            r = csv.DictReader(
                f, 
                fieldnames=["Absolut_path", "Relative_patch", "Class"], 
                delimiter="|")
            for i in r:
                if i["Class"] == name:
                    self.read_list.append(i["Absolut_path"])

    def __iter__(self):
        """Return iterator object.
        Returns:
            self: Iterator object.
        """
        return self

    def __next__(self) -> str:
        """Return the next element in the sequence.
        Raises:
            StopIteration: Stopping the iterator.
        Returns:
           str: Patch to the file.
        """
        if self.count < len(self.read_list):
            self.count += 1
            return self.read_list[self.count]
        elif self.count == len(self.read_list):
            raise StopIteration
