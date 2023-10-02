import datetime
import csv

def search_dataset_csv(str_date, w_file):
    search_date = datetime.datetime.fromisoformat(str_date)
    reader = csv.DictReader(w_file)
    w_file.seek(0)
    for row in reader:
        if row['Дата'] == search_date.strftime('%Y-%m-%d'):
            search = (row['Дата'], row['Курс Доллара'])
            search_tuple(search)
def search_X_Y_csv(w_file_y, w_file_x, str_date):
    search_date = datetime.datetime.fromisoformat(str_date)
    reader_X = csv.DictReader(w_file_x)
    reader_Y = csv.DictReader(w_file_y)
    w_file_x.seek(0)
    w_file_y.seek(0)
    count = 1
    for row in reader_X:
        if row['Дата'] == search_date.strftime('%Y-%m-%d'):
            for rowe in reader_Y:
                if count == 1:
                    search = (row['Дата'], rowe['Курс Доллара'])
                    search_tuple(search)
                count -= 1
        count += 1

def search_tuple(search):
    search_all = tuple()
    search_all += search
    print("Comon", search)




