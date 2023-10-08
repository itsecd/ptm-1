import pandas as pd

from typing import NoReturn


def formatted_file(dataset_csv: str) -> pd.DataFrame:
    """Возвращает фрейм  данных с добавлением столбцов"""
    df = pd.read_csv(dataset_csv)
    df["Date"] = pd.to_datetime(df.Date, format="%Y-%m-%d")
    df["Date1"] = df["Date"].dt.date
    df["Year"] = df["Date"].dt.year
    return df


def write_to_file(dataset_csv: str, year: int) -> NoReturn:
    """Принимает файл dataset и разбивает на годы"""
    df = formatted_file(dataset_csv)

    df = df[df["Year"] == year]
    data = str(df["Date1"].iloc[0]).replace("-", "") + "_" + str(df["Date1"].iloc[df.shape[0] - 1]).replace("-", "")
    del df["Year"]
    del df["Date1"]
    df.to_csv(data + ".csv", index=False)


def range_of_date(dataset_csv: str) -> list:
    """Диапазон значений временных в наборе данных
    input_file - файл с набором данных
    возвращает список с первым и последним годом в наборе данных"""
    df = formatted_file(dataset_csv)

    start_range = df["Year"].iat[0]
    end_range = df["Year"].iat[-1]
    return [start_range, end_range]


if __name__ == "__main__":
    file = "C:/Users/User/Desktop/dataset.csv"
    range_of_years = range_of_date(file)
    for years in range(range_of_years[0], range_of_years[1] - 1, -1):
        write_to_file(file, years)
