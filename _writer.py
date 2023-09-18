import csv
import os

from tqdm import tqdm


def write_annotation(path_to_dataset: str, csv_path: str) -> str or None:
    """Write paths to csv file

    Args:
        path_to_dataset (str): Path to the dataset
        csv_path (str): Name of the csvfile

    Returns:
        str or None: Returns path to csvfile or None 
    """
    if not csv_path.find(".csv"):
        field_names = ["The Absolute Way", "Relative Way", "Class"]
        with open(csv_path, "w", newline="", encoding="utf8") as f:
            printer = csv.DictWriter(
                f, fieldnames=field_names, delimiter=";")
            printer.writeheader()

        class_name = "cat"
        path_to_cat = os.path.join(path_to_dataset, class_name)
        num_files = len([f for f in os.listdir(path_to_cat)
                        if os.path.isfile(os.path.join(path_to_cat, f))])

        for i in tqdm(range(0, num_files)):
            with open(csv_path, "a", newline="", encoding="utf8") as f:
                print_in_file = csv.DictWriter(
                    f, fieldnames=field_names, delimiter=";")

                path = os.path.join(path_to_cat, f"{str(i).zfill(4)}.jpg")

                if os.path.isfile(path):
                    print_in_file.writerow({"The Absolute Way": path,
                                            "Relative Way": os.path.relpath(path),
                                            "Class": class_name})

        class_name = "dog"
        path_to_dog = os.path.join(path_to_dataset, class_name)
        num_files = len([f for f in os.listdir(path_to_dog)
                        if os.path.isfile(os.path.join(path_to_dog, f))])

        for i in tqdm(range(0, num_files)):
            with open(csv_path, "a", newline="", encoding="utf8") as f:
                print_in_file = csv.DictWriter(
                    f, fieldnames=field_names, delimiter=";")

                path = os.path.join(path_to_dog, f"{str(i).zfill(4)}.jpg")

                if os.path.isfile(path):
                    print_in_file.writerow({"The Absolute Way": path,
                                            "Relative Way": os.path.relpath(path),
                                            "Class": class_name})

    else:
        field_names = ["The Absolute Way", "Relative Way", "Class"]
        with open(csv_path, "w", newline="", encoding="utf8") as f:
            printer = csv.DictWriter(
                f, fieldnames=field_names, delimiter=";")
            printer.writeheader()

        class_name = "cat"
        path_to_cat = os.path.join(path_to_dataset, class_name)
        num_files = len([f for f in os.listdir(path_to_cat)
                        if os.path.isfile(os.path.join(path_to_cat, f))])

        for i in tqdm(range(0, num_files)):
            with open(csv_path, "a", newline="", encoding="utf8") as f:
                print_in_file = csv.DictWriter(
                    f, fieldnames=field_names, delimiter=";")

                path = os.path.join(path_to_cat, f"{str(i).zfill(4)}.jpg")

                if os.path.isfile(path):
                    print_in_file.writerow({"The Absolute Way": path,
                                            "Relative Way": os.path.relpath(path),
                                            "Class": class_name})

        class_name = "dog"
        path_to_dog = os.path.join(path_to_dataset, class_name)
        num_files = len([f for f in os.listdir(path_to_dog)
                        if os.path.isfile(os.path.join(path_to_dog, f))])

        for i in tqdm(range(0, num_files)):
            with open(csv_path, "a", newline="", encoding="utf8") as f:
                print_in_file = csv.DictWriter(
                    f, fieldnames=field_names, delimiter=";")

                path = os.path.join(path_to_dog, f"{str(i).zfill(4)}.jpg")

                if os.path.isfile(path):
                    print_in_file.writerow({"The Absolute Way": path,
                                            "Relative Way": os.path.relpath(path),
                                            "Class": class_name})
        
        return csv_path
                    


def main() -> None:
    """Main function"""
    path_to_dataset = "C:/Users/User/nuck figgers/dataset"
    csv_path = "dataset.csv"
    write_annotation(path_to_dataset, csv_path)


if __name__ == "__main__":
    main()
