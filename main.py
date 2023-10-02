import csv
import requests
import datetime

from pprint import pprint
from first_task import new_csv
from second_task import Year_csv
from the_third_task import Week_csv
from the_fourth_task import search_dataset_csv


if __name__ == "__main__":
    data = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
    print("за сколько дней вы хотите увидеть курс доллара?:")
    count = 1
    max_count = int(input())
    week_start = data['Date']
    week_start = datetime.datetime.fromisoformat(week_start)
    week_count = 1
    start_date = data['Date']
    start_date = datetime.datetime.fromisoformat(start_date)
    print('Give the date:')
    str_date = str(input())
    with open("dataset.csv", mode="w+", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        file_writer.writerow(["Дата", "Курс Доллара"])
        while count <= max_count:
            Date = data['Date']
            Date = datetime.datetime.fromisoformat(Date)
            print(Date.strftime('%Y-%m-%d'))
            pprint(data['Valute']['USD']['Value'])
            file_writer.writerow([Date.strftime('%Y-%m-%d'), data['Valute']['USD']['Value']])
            if start_date.month != Date.month:
                end_date = data['Date']
                end_date = datetime.datetime.fromisoformat(end_date)
                Year_csv(w_file, start_date, end_date)
                start_date = Date
            week_count += 1
            if week_count == 7:
                week_end = data['Date']
                week_end = datetime.datetime.fromisoformat(week_end)
                Week_csv(w_file, week_start, week_end)
                week_start = Date
                week_count = 1
            data = requests.get('https:' + data['PreviousURL']).json()
            count += 1
        new_csv(w_file, str_date)
        search_dataset_csv(str_date, w_file)
