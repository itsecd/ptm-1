import numpy
import pandas as pd
import datetime
import os

from typing import Union


def formatted_file(dataset_file: str) -> pd.DataFrame:
    """Форматирование файла
    Возвращает фрейм данных с добавлением столбцов"""
    df = pd.read_csv(dataset_file)
    df["Date"] = pd.to_datetime(df.Date, format="%Y-%m-%d")
    df["Date"] = df["Date"].dt.date
    return df


def get_data(dataset_file: str, date: datetime.date) -> Union[numpy.float64, None]:
    """dataset_file - файл с набором данных
    date: необходимая дата
    возвращает значение необходимой даты"""
    if os.path.exists(dataset_file):

        df = formatted_file(dataset_file)
        for i in range(0, df.shape[0], 1):
            if str(df["Date"].iloc[i]).replace("-", "") == str(date).replace("-", ""):
                return df.iloc[i]["Course"]
        return None
    raise FileNotFoundError


def get_data_xy(x_csv: str, y_csv: str, date: datetime.date) -> Union[numpy.float64, None]:
    """ X_csv: Файл с Датами"
     Y_csv: файл с курсом Доллара"
     date: необходимая дата
     возвращает значение необходимой даты"""
    if os.path.exists(x_csv) and os.path.exists(y_csv):
        df_x = pd.read_csv(x_csv)
        df_y = pd.read_csv(y_csv)
        index = -1
        for i in range(0, df_x.shape[0], 1):
            if df_x["Date"].iloc[i].replace("-", "") == str(date).replace("-", ""):
                index = i
                break
        if index >= 0:
            return df_y.iloc[index]["Course"]
        return None
    raise FileNotFoundError


def get_data_from_week_and_years(week_year_csv: str, date: datetime.date) -> Union[numpy.float64, None]:
    """ week_year_csv: каталог с отсортированным файлом по неделям\годам
    date: необходимая дата
    возвращает значение необходимой даты"""
    if os.path.exists(week_year_csv):
        for root, dirs, files in os.walk(week_year_csv):
            for filename in files[0: -1:]:
                df = pd.read_csv(os.path.join(root, filename))

                for i in range(0, df.shape[0], 1):
                    if df["Date"].iloc[i].replace("-", "") == str(date).replace("-", ""):
                        return df.iloc[i]["Course"]
            return None
    raise FileNotFoundError


def tuple_for_next_data() -> tuple:
    """кортеж с данными и  обменным курсом для этих данных"""
    dataset_file = "C:/Users/User/Desktop/dataset.csv"
    if os.path.exists(dataset_file):
        df = pd.read_csv(dataset_file)
        for data in df["Date"]:
            i = df.index[df["Date"] == data]
            yield data, *df.loc[i]["Course"].values
    raise FileNotFoundError


if __name__ == "__main__":
    try:
        dataset_csv = "C:/Users/esh20/Desktop/dataset.csv"
        X_csv = "C:/Users/User/Desktop/PYTHON/Lab2/1/X.csv"
        Y_csv = "C:/Users/User/Desktop/PYTHON/Lab2/1/Y.csv"
        weeks_csv = "C:/Users/User/Desktop/PYTHON/Lab2/3/"
        years_csv = "C:/Users/User/Desktop/PYTHON/Lab2/2/"
        existing_date = datetime.date(2022, 9, 15)
        nonexistent_date = datetime.date(1991, 5, 12)
        it = tuple_for_next_data()
        while True:
            print(next(it))
    except FileNotFoundError:
        print("No such file exists!")
