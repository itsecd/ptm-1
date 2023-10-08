import pandas as pd
import autopep8


def formatted_file(input_file: str) -> pd.DataFrame:
    """
        input_file:  file with dataset
        DataFrame with added column
       """
    df = pd.read_csv(input_file)

    df["Day"] = pd.to_datetime(df.Day, format="%Y-%m-%d")
    df["Day1"] = df["Day"].dt.date
    df["Year"] = df["Day"].dt.year
    df["Week"] = df["Day"].dt.isocalendar().week
    return df


def clear_file(df: pd.DataFrame) -> pd.DataFrame:
    """
         DataBase with added column
         DataBase withou added column
        """
    del df["Year"]
    del df["Week"]
    del df["Day1"]
    return df


def range_of_years(input_file: str) -> list:
    """
         input_file: file with dataset
         list with first and last year from DataBase
        """
    df = formatted_file(input_file)

    start_range = df["Year"].iat[0]
    end_range = df["Year"].iat[-1]
    return [start_range, end_range]


def max_week(df: pd.DataFrame) -> int:
    """
       DataFrame
       Number of max week from single year
       """
    start_range = df[df["Week"] == df["Week"].max()]
    value = start_range["Week"].values[0]
    return value


def min_week(df: pd.DataFrame) -> int:
    """
         DataFrame
         Number of min week from single year
        """
    end_range = df[df["Week"] == df["Week"].min()]
    value = end_range["Week"].values[0]
    return value


def write_to_file(input_file: str) -> None:
    """
        output_directory:
        input_file: file with dataset
        Nothing
        """
    df = formatted_file(input_file)
    range_of_years_list = range_of_years(input_file)

