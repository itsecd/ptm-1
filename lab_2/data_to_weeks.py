import csv
import datetime
import os
from typing import NoReturn


def get_year_from_data(data: list[list[str]], index: int) -> int:
    """Gets the year from csv file

    Args:
        data (list[list[str]]): A list with dates and data
        index (int): The index of the string that points on list in the list

    Returns:
        int: Value of year
    """
    date = data[index][0]
    year = ""
    for numbers in date:
        if numbers != "-":
            year += numbers
        else:
            break
    return int(year)


def get_month_from_data(data: list[list[str]], index: int) -> int:
    """Gets the month from csv file

    Args:
        data (list[list[str]]): A list with dates and data
        index (int): The index of the string that points on list in the list
    Returns:
        int: Value of month
    """
    date = data[index][0]
    month = ""
    dash_counter = 0
    for numbers in date:
        if numbers == "-":
            dash_counter += 1
            continue
        if dash_counter == 1:
            month += numbers
        elif dash_counter == 2:
            break
    return int(month)


def get_day_from_data(data: list[list[str]], index: int) -> int:
    """Gets the day from csv file

    Args:
        data (list[list[str]]): A list with dates and data
        index (int): The index of the string that points on list in the list

    Returns:
        int: Value of day
    """
    date = data[index][0]
    day = ""
    dash_counter = 0
    for numbers in date:
        if numbers == "-":
            dash_counter += 1
            continue
        if dash_counter == 2:
            day += numbers
    return int(day)


def name_for_file(first_part: str, second_part: str) -> str:
    """Creates a name for file

    Args:
        first_part (str): First part of future file"s name
        second_part (str): Second part of future file"s name
    Returns:
        str: Name in special format
    """
    f_p = first_part.replace("-", "") + "_"
    s_p = second_part.replace("-", "") + ".csv"
    return os.path.join("data_to_weeks_output", f_p + s_p)


def week_border(data: list[list[str]], index) -> list[str]:
    """A function that makes a list consisting of the days of one week
    Args:
        data (list[list[str]]): A list with dates and data
        index (_type_): The index of the string that points on list in the list

    Returns:
        list[str]: A list of the days of one week
    """
    date = datetime.date(get_year_from_data(data, index), get_month_from_data(
        data, index), get_day_from_data(data, index))
    weekday = date.isoweekday()
    week = []
    if weekday == 1:
        week.append(str(date))
        for i in range(1, 7):
            week.append(str(date + datetime.timedelta(days=i)))
        return week
    elif weekday != 7 and weekday != 1:
        for i in range(weekday - 1, 0, -1):
            week.append(str(date - datetime.timedelta(days=i)))
        week.append(str(date))
        for i in range(1, 8 - weekday):
            week.append(str(date + datetime.timedelta(days=i)))
        return week
    elif weekday == 7:
        for i in range(6, 0, -1):
            week.append(str(date - datetime.timedelta(days=i)))
        week.append(str(date))
        return week


def weeks_writer(data: list[list[str]]) -> NoReturn:
    """A function that splits the original csv file into N files, where each individual file will correspond to one week.
    Args:
        data (list[list[str]]): A list with dates and data
    """
    first_part_of_name = ""
    second_part_of_name = ""
    output = []
    border = week_border(data, 0)
    is_first = True
    for i in range(len(data)):
        day_in_week = False
        for date in border:
            if data[i][0] == date:
                if is_first:
                    first_part_of_name = data[i][0]
                    is_first = False
                day_in_week = True
                second_part_of_name = data[i][0]
                output.append(data[i])
                break
        if day_in_week == False:
            border = week_border(data, i)
            with open(name_for_file(first_part_of_name, second_part_of_name), "w", encoding="utf-8") as csv_file:
                writer = csv.writer(csv_file, lineterminator="\n")
                for j in output:
                    writer.writerow((j))
                output = []
                output.append(data[i])
                first_part_of_name = data[i][0]


def data_to_weeks(file_name: str):
    """Function that reads the csv file

    Args:
        file_name (str): Path to file

    Raises:
        FileNotFoundError: File does not exist
    """
    if os.path.exists(file_name):
        if not os.path.exists("data_to_weeks_output"):
            os.mkdir("data_to_weeks_output")
        with open(file_name, "r", encoding="utf-8") as csvfile:
            reader_object = list(csv.reader(csvfile, delimiter=","))
            weeks_writer(reader_object)
    else:
        raise FileNotFoundError

if __name__ == "__main__":
    try:
        file_name = "result.csv"
        data_to_weeks(file_name)
    except FileNotFoundError:
        print("No such file exists!")