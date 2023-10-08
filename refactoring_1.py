import argparse
import datetime
import time
from typing import Union
import numpy
import os
import pandas as pd


def formatted_file(input_file: str) -> pd.DataFrame:
    """
     Reads a file and formats it for further work."
     
     @param input_file - Path to the CSV file.
     
     @return DataFrame with the data from the CSV file.
    """
    df = pd.read_csv(input_file)
    df["Day"] = pd.to_datetime(df.Day, format="%Y-%m-%d")
    df["Day"] = df["Day"].dt.date
    return df


def get_data(input_file: str, date: datetime.date) -> Union[numpy.float64, None]:
    """
     Get the data from the file that corresponds to the date.
     
     @param input_file - Path to the CSV file.
     @param date - Date to look for in the file. If it's a date it will be treated as the start of the day
     
     @return A numpy array of the data or None if not found.
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
     Get the data from the file that corresponds to the date.
     
     @param input_file_x - Path to the CSV file with date.
     @param input_file_y - Path to the CSV file with data.
     @param date - Date to look for in the file.
     
     @return A numpy array of the data or None if not found.
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
     Get the data from the file that corresponds to the date.
     
     @param input_directory - Directory to search for data.
     @param date - Date to look for in the file.
     
     @return A numpy array of the data or None if not found.
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

def get_data_from_week_and_years_new(input_directory: str, date: datetime.date) -> Union[numpy.float64, None]:
    """
     Get the data from the file that corresponds to the date.
     
     @param input_directory - Directory to search for data.
     @param date - Date to look for in the file.
     
     @return A numpy array of the data or None if not found.
    """
    int_datetime = int(date.strftime('%Y%m%d'))
    if os.path.exists(input_directory):
        for root, dirs, files in os.walk(input_directory):
            for filename in files[0: -1:]:
                words = filename.split('_')
                words[1] = words[1].split('.', 1)[0]
                for word in range(int(words[0]), int(words[1]) - 1, -1):
                    if word == int_datetime:
                        df = pd.read_csv(os.path.join(root, filename))
                        for i in range(0, df.shape[0], 1):
                            if df["Day"].iloc[i].replace("-", "") == str(date).replace("-", ""):
                                return df.iloc[i]["Exchange rate"]
                    pass
    raise FileNotFoundError

def tuple_for_next_data(input_directory: str) -> tuple:
    """
     Yield data and exchanges for the next day.
     
     @param input_directory - Path to the directory containing the data
     
     @return Tuple of data.
    """
    if os.path.exists(input_directory):
        df = pd.read_csv(input_directory)
        for data in df["Day"]:
            i = df.index[df["Day"] == data]
            yield data, *df.loc[i]["Exchange rate"].values
    raise FileNotFoundError


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process data files")
    parser.add_argument("--file", help="Path to the CSV file", required=True)
    parser.add_argument("--file_x", help="Path to the CSV file X", required=True)
    parser.add_argument("--file_y", help="Path to the CSV file Y", required=True)
    parser.add_argument("--dir_weeks", help="Path to directory with weekly data", required=True)
    parser.add_argument("--dir_years", help="Path to directory with yearly data", required=True)
    parser.add_argument("--existing_date", help="Date for existing data (YYYY-MM-DD)", required=True)
    parser.add_argument("--nonexistent_date", help="Date for nonexistent data (YYYY-MM-DD)", required=True)

    args = parser.parse_args()

    FILE = args.file
    FILE_X = args.file_x
    FILE_Y = args.file_y
    DIRECTORY_FOR_WEEKS = args.dir_weeks
    DIRECTORY_FOR_YEARS = args.dir_years
    EXISTING_DATE = datetime.datetime.strptime(args.existing_date, "%Y-%m-%d").date()
    NONEXISTENT_DATE = datetime.datetime.strptime(args.nonexistent_date, "%Y-%m-%d").date()

    try:
        print(get_data(FILE, EXISTING_DATE))
        print(get_data(FILE, NONEXISTENT_DATE))
        print(get_data_xy(FILE_X, FILE_Y, EXISTING_DATE))
        print(get_data_xy(FILE_X, FILE_Y, NONEXISTENT_DATE))
        print(get_data_from_week_and_years(DIRECTORY_FOR_WEEKS, EXISTING_DATE))
        print(get_data_from_week_and_years(DIRECTORY_FOR_WEEKS, NONEXISTENT_DATE))
        print(get_data_from_week_and_years(DIRECTORY_FOR_YEARS, EXISTING_DATE))
        print(get_data_from_week_and_years(DIRECTORY_FOR_YEARS, NONEXISTENT_DATE))
        it = tuple_for_next_data()
        while True:
            print(next(it))
    except FileNotFoundError:
        print("No such file exists!")
        