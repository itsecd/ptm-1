import csv
import os


class Iterator:
    def __init__(self, path_to_file: str, class_name: str) -> None:
        """Initializing an iterator class object

        Args:
            path_to_file (str): The path to the csv file
            class_name (str): Name of the image class

        Raises:
            FileNotFoundError: Exception, if there is no csv file with this path
        """
        
        self.class_name = class_name
        self.path_to_file = path_to_file
        self.list = []
        self.counter = 0

        if os.path.exists(self.path_to_file):
            with open(self.path_to_file, "r", encoding="utf8") as file:
                read = csv.DictReader(
                    file, fieldnames=["The Absolute Way", "Relative Way", "Class"], delimiter=";")

                for row in read:
                    if row["Class"] == self.class_name:
                        self.list.append(
                            [row["The Absolute Way"], row["Relative Way"], row["Class"]])

        else:
            raise FileNotFoundError

    def __iter__(self):
        return self

    def __next__(self) -> str:
        """The function of switching to the next instance of the list in the class object

        Raises:
            StopIteration: If the counter reaches the border of the list, it throws an exception and stops the iterator

        Returns:
            str: The path to the picture 
        """
       
        if self.counter < len(self.list):
            self.counter += 1
            return self.list[self.counter][0]

        elif self.counter == len(self.list):
            raise StopIteration
