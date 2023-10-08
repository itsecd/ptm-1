import pandas as pd
from typing import NoReturn


def formatted_file(input_file: str) -> pd.DataFrame:
    """
         input_file: file with dataset
         DataFrame with added column
        """
    df = pd.read_csv(input_file)

    df["Day"] = pd.to_datetime(df.Day, format="%Y-%m-%d")
    df["Day1"] = df["Day"].dt.date
    df["Year"] = df["Day"].dt.year
    return df


def write_to_file(input_file: str, year: int) -> NoReturn:
    """
         input_file: file with dataset
         list with first and last year in the dataset
        """
    df = formatted_file(input_file)

    df = df[df["Year"] == year]
    data = str(df["Day1"].iloc[0]).replace("-", "") + "_" + str(df["Day1"].iloc[df.shape[0] - 1]).replace("-", "")
    del df["Year"]
    del df["Day1"]
    df.to_csv(data + ".csv", index=False)


def range_of_date(input_file: str) -> list:
    """
         input_file: file with dataset
         list with first and last year in the dataset
        """
    df = formatted_file(input_file)

    start_range = df["Year"].iat[0]
    end_range = df["Year"].iat[-1]
    return [start_range, end_range]


if __name__ == "__main__":

    file = "C:/Users/esh20/Desktop/dataset.csv"

    range_of_years = range_of_date(file)
    for years in range(range_of_years[0], range_of_years[1] - 1, -1):
        write_to_file(file, years)
