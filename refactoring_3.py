import pandas as pd


def formatted_file(input_file: str) -> pd.DataFrame:
    df = pd.read_csv(input_file)
    df["Day"] = pd.to_datetime(df.Day, format="%Y-%m-%d")
    df["Day1"] = df["Day"].dt.date  # превращаю Str to datatime64[ns]
    df["Year"] = df["Day"].dt.year
    df["Week"] = df["Day"].dt.isocalendar().week
    return df


def clear_file(df: pd.DataFrame) -> pd.DataFrame:
    del df["Year"]
    del df["Week"]
    del df["Day1"]
    return df


def range_of_years(input_file: str) -> list:
    df = formatted_file(input_file)
    start_range = df["Year"].iat[0]
    end_range = df["Year"].iat[-1]
    return [start_range, end_range]


def max_week(df: pd.DataFrame) -> int:
    start_range = df[df["Week"] == df["Week"].max()]
    value = start_range["Week"].values[0]
    return value


def min_week(df: pd.DataFrame) -> int:
    end_range = df[df["Week"] == df["Week"].min()]
    value = end_range["Week"].values[0]
    return value


def write_to_file(input_file: str) -> None:
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
    file = "C:/Users/artyo/Desktop/dataset.csv"
    write_to_file(file)
