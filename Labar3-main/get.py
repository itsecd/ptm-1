import numpy
import pandas as pd
import datetime
import os
from typing import Union
import autopep8


def formatted_file(input_file: str) -> pd.DataFrame:
    df = pd.read_csv(input_file)
    df["Day"] = pd.to_datetime(df.Day, format="%Y-%m-%d")
    df["Day"] = df["Day"].dt.date
    return df


def get_data(input_file: str, date: datetime.date) -> Union[numpy.float64, None]:
    """
         input_file: file with dataset
         date: necessary date
         return: value for necessary date
        """
    if os.path.exists(input_file):
        df = formatted_file(input_file)
        for i in range(0, df.shape[0], 1):
            if str(df["Day"].iloc[i]).replace("-", "") == str(date).replace("-", ""):
                return df.iloc[i]["Exchange rate"]
        return None
    raise FileNotFoundError


def get_data_xy(input_file_x: str, input_file_y: str,
                date: datetime.date) -> Union[numpy.float64, None]:
    """
        input_file_x: file with column "Data"
        input_file_y: file with column "Exchange rate"
        date: necessary date
        return: value for necessary date
        """
    if os.path.exists(input_file_x) and os.path.exists(input_file_y):

        df_x = pd.read_csv(input_file_x)
        df_y = pd.read_csv(input_file_y)
        index = -1

        for i in range(0, df_x.shape[0], 1):
            if df_x["Day"].iloc[i].replace("-", "") == str(date).replace("-", ""):
                index = i
                break

        if index >= 0:
            return df_y.iloc[index]["Exchange rate"]
        return None

    raise FileNotFoundError

def get_data_from_week_and_years(input_directory: str, date: datetime.date) -> Union[numpy.float64, None]:
    """
        input_directory: directory with sorted file by weeks or years
        date: necessary date
        return: value for necessary date
        """
    if os.path.exists(input_directory):
         for root, dirs, files in os.walk(input_directory):
             for filename in files[0: -1:]:
                 df = pd.read_csv(os.path.join(root, filename))

                 for i in range(0, df.shape[0], 1):
                     if df["Day"].iloc[i].replace("-", "") == str(date).replace("-", ""):
                         return df.iloc[i]["Exchange rate"]

         return None
    raise FileNotFoundError


def tuple_for_next_data() -> tuple:
    """
    tuple with data and exchange rate for this data
       """
    input_file = "C:/Users/esh20/Desktop/dataset.csv"
    if os.path.exists(input_file):
        df = pd.read_csv(input_file)
        for data in df["Day"]:
            i = df.index[df["Day"] == data]
            yield data, *df.loc[i]["Exchange rate"].values
    raise FileNotFoundError


if __name__ == "__main__":
    try:
        file = "C:/Users/esh20/Desktop/dataset.csv"
        file_x = "C:/Users/esh20/PycharmProjects/Lab2/1/X.csv"
        file_y = "C:/Users/esh20/PycharmProjects/Lab2/1/Y.csv"
        directory_for_weeks = "C:/Users/esh20/PycharmProjects/Lab2/3/"
        directory_for_years = "C:/Users/esh20/PycharmProjects/Lab2/2/"

        existing_date = datetime.date(2022, 9, 15)
        nonexistent_date = datetime.date(1991, 5, 12)

        it = tuple_for_next_data()
        while True:
            print(next(it))

    except FileNotFoundError:
        print("No such file exists!")
        