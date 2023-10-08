import argparse
import pandas as pd


def formatted_file(input_file: str) -> pd.DataFrame:
    """
     Reads a CSV file and formats it for further work.
     
     @param input_file - Path to the CSV file.
     
     @return DataFrame with the data from the CSV file.
    """
    df = pd.read_csv(input_file)
    df["Day"] = pd.to_datetime(df.Day, format="%Y-%m-%d")
    df["Day1"] = df["Day"].dt.date
    df["Year"] = df["Day"].dt.year
    df["Week"] = df["Day"].dt.isocalendar().week
    return df


def clear_file(df: pd.DataFrame) -> pd.DataFrame:
    """
     Removes unnecessary data from file to.
     
     @param df - Dataframe to be cleared.
     
     @return DataFrame  without the year, week and day columns.
    """
    del df["Year"]
    del df["Week"]
    del df["Day1"]
    return df


def range_of_years(input_file: str) -> list:
    """
     Returns list of start and end years of input file.
     
     @param input_file - path to file to be processed.
     
     @return list of year range of input file.
    """
    df = formatted_file(input_file)
    start_range = df["Year"].iat[0]
    end_range = df["Year"].iat[-1]
    return [start_range, end_range]


def max_week(df: pd.DataFrame) -> int:
    """
     Function to find the minimum week in DataFrame.   

     @param df - DataFrame with data from CSV.
     
     @return value of the maximum week in DataFrame.
    """
    start_range = df[df["Week"] == df["Week"].max()]
    value = start_range["Week"].values[0]
    return value


def min_week(df: pd.DataFrame) -> int:
    """
     Function to find the minimum week in data frame.
     
     @param df - DataFrame with data from CSV.
     
     @return value of the minimum week in DataFrame.
    """
    end_range = df[df["Week"] == df["Week"].min()]
    value = end_range["Week"].values[0]
    return value


def write_to_file(input_file: str) -> None:
    """
     Write data to file. 
     
     @param input_file - name of the file to.
    """
    df = formatted_file(input_file)
    range_of_years_list = range_of_years(input_file)
    for years in range(range_of_years_list[0], range_of_years_list[1] - 1, -1):
        lf = df[df["Year"] == years]
        for weeks in range(
                max_week(lf), min_week(lf) - 1, -1):
            try:
                sf = lf[lf["Week"] == weeks]
                if sf.empty:
                    break
                elif sf.shape[0] == 1:
                    data = str(sf["Day1"].iloc[0]).replace("-", "") + "_" + str(sf["Day1"].iloc[0]).replace("-", "")
                else:
                    data = str(sf["Day1"].iloc[0]).replace("-", "") + "_" + str(sf["Day1"].iloc[-1]).replace("-", "")
                clear_file(sf)
                sf.to_csv(data + ".csv", index=False)
            except Exception as e:
                print(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process data files")
    parser.add_argument("--file", help="Path to the CSV file", required=True)

    args = parser.parse_args()

    FILE = args.file
    write_to_file(FILE)
