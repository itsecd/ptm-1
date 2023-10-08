import pandas as pd


def write_to_file(input_file: str, file_for_x: str, file_for_y: str) -> None:
    """
         output_directory:
         input_file: Start file with dataset
         Nothing
        """
    df = pd.read_csv(input_file)
    df["Day"].to_csv(file_for_x, index=False)
    df["Exchange rate"].to_csv(file_for_y, index=False)


if __name__ == "__main__":
    my_file_for_dates = "X.csv"
    my_file_for_data = "Y.csv"
    file = "C:/Users/esh20/Desktop/dataset.csv"

    write_to_file(file, my_file_for_dates, my_file_for_data)
