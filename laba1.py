import csv
import requests
from bs4 import BeautifulSoup


HEADERS = {"User-Agent": "Windows 10"}


def change_years(year: int, url: str) -> str:
    """Function that changes the year in the url.

    Args:
        year (int): The year that need to change in the url.
        url (str): Site url.

    Returns:
        str: Changed url.
    """
    url = url.replace(str(year - 1), str(year))
    return url


def redact_days(output: list[str]) -> str:
    """A function that edits the day number in the output array.

    Args:
        output (list[str]): List that contains output information.

    Returns:
        str: String that contains day's number.
    """
    if int(output[0]) < 10:
        return "0" + output[0]
    else:
        return output[0]


def month_num_to_str(month: int) -> str:
    """A function that returns the month number in the desired format for output to a csv file.

    Args:
        month (int): The number of the month.

    Returns:
        str: The number of the month converted to a string.
    """
    if month < 10:
        return "0" + str(month)
    else:
        return str(month)


def check_month(url: str) -> int:
    """A function that returns the maximum month of the current year.

    Args:
        url (str): Url site.
    Returns:
        int: Max month number.
    """
    month = 1
    while True:
        html_text = requests.get(url, HEADERS).text
        parse = BeautifulSoup(html_text, "lxml")
        is_error_element = parse.find("div", class_="grey digit")
        if is_error_element:
            month -= 1
            break
        else:
            month += 1
            url = url[0:39] + "/" + str(month) + "/"
    return month


def change_months(url:str, month: int, change_type: int) -> str:
    """A function that replaces the month value in the url.

    Args:
        url (str): Url site.
        month (int): Month.
        change_type (int): Type of change.
    Returns:
        str: Changed url.
    """
    if change_type == 2:
        url = url[0:39] + "/1/"
    else:
        url = url[0:39] + "/" + str(month) + "/"
    return url

if __name__ == "__main__":
    url = "https://www.gismeteo.ru/diary/4618/2008/1/"
    year = 2008
    max_year = year
    current_url = url
    while True:
        html_text = requests.get(current_url, HEADERS).text
        parse = BeautifulSoup(html_text, "lxml")
        is_error_element = parse.find("div", class_="grey digit")
        if is_error_element:
            max_year -= 1
            break
        else:
            max_year += 1
            current_url = current_url.replace(str(max_year - 1), str(max_year))
    current_url = current_url.replace(str(max_year + 1), str(max_year))
    last_month = check_month(current_url)
    for current_year in range(year, max_year + 1):
        url = change_years(current_year, url)
        max_month = 12
        if current_year == max_year:
            max_month = last_month
        for current_month in range(1, max_month + 1):
            is_last_month = 0
            if current_month == max_month:
                url = change_months(url, current_month, 1)
                is_last_month = 1
            else:
                url = change_months(url, current_month, 1)
            html_text = requests.get(url, HEADERS).text
            soup = BeautifulSoup(html_text, "lxml")
            rows = soup.find_all("tr", align="center")
            for i in range(len(rows)):
                data = rows[i].find_all("td")
                output = []
                numbers = [0, 1, 2, 5, 6, 7, 10]
                for j in numbers:
                    output.append(data[j].text)
                with open("dataset.csv", "a", encoding="utf-8") as csvfile:
                    writer = csv.writer(csvfile, lineterminator='\n')
                    writer.writerow(
                        (
                            str(current_year) + "-" 
                            + month_num_to_str(current_month) + "-" 
                            + redact_days(output),
                            output[1],
                            output[2],
                            output[3],
                            output[4],
                            output[5],
                            output[6],
                        )
                    )
            if is_last_month == 1:
                url = change_months(url, current_month, 2)
