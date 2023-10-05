import datetime
import numpy
import os
import pandas as pd
from typing import Union


def formatted_file(input_file: str) -> pd.DataFrame:

    df = pd.read_csv(input_file)
    df["Day"] = pd.to_datetime(df.Day, format="%Y-%m-%d")
    df["Day"] = df["Day"].dt.date
    return df


def get_data(input_file: str, date: datetime.date) -> Union[numpy.float64, None]:

    if os.path.exists(input_file):
        df = formatted_file(input_file)
        for i in range(0, df.shape[0], 1):
            if str(df["Day"].iloc[i]).replace("-", "") == str(date).replace("-", ""):
                return df.iloc[i]["Exchange rate"]
        return None
    raise FileNotFoundError


def get_data_xy(input_file_x: str, input_file_y: str,
                date: datetime.date) -> Union[numpy.float64, None]:

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

def tuple_for_next_data() -> tuple:
    
    input_file = "C:/Users/artyo/Desktop/dataset.csv"
    if os.path.exists(input_file):
        df = pd.read_csv(input_file)
        for data in df["Day"]:
            i = df.index[df["Day"] == data]
            yield data, *df.loc[i]["Exchange rate"].values
    raise FileNotFoundError


if __name__ == "__main__":
    try:
        file = "C:/Users/artyo/Desktop/dataset.csv"
        file_x = "C:/Users/artyo/PycharmProjects/labs/lab2/1/X.csv"
        file_y = "C:/Users/artyo/PycharmProjects/labs/lab2/1/Y.csv"
        directory_for_weeks = "C:/Users/artyo/PycharmProjects/labs/lab2/3/"
        directory_for_years = "C:/Users/artyo/PycharmProjects/labs/lab2/2/"

        existing_date = datetime.date(2022, 9, 15)
        nonexistent_date = datetime.date(1991, 5, 12)

        # print(get_data(file, existing_date))
        # print(get_data(file, nonexistent_date))
        #
        # print(get_data_xy(file_x, file_y, existing_date))
        # print(get_data_xy(file_x, file_y, nonexistent_date))
        import time
        t1 = time.time()
        print(get_data_from_week_and_years_new(directory_for_weeks, existing_date))
        t2 = time.time()
        print(get_data_from_week_and_years(directory_for_weeks, existing_date))
        t3 = time.time()
        dt1 = t3-t2
        dt2 = t2-t1
        print(dt1, dt2, dt1/dt2)
        # print(get_data_from_week_and_years(directory_for_weeks, nonexistent_date))
        #
        #print(get_data_from_week_and_years(directory_for_years, existing_date))
        # print(get_data_from_week_and_years(directory_for_years, nonexistent_date))

        # it = tuple_for_next_data()
        # while True:
        #     print(next(it))

    except FileNotFoundError:
        print("No such file exists!")
