import datetime
import csv


def search_dataset_csv(str_date, w_file) -> None:
    """
    Принимает на вход данные и передает отсортированные данные в функцию, для записи в тело кортежа.
    :param w_file: Входные данные.
    :param str_date: Дата.
    """
    search_date = datetime.datetime.fromisoformat(str_date)
    reader = csv.DictReader(w_file)
    w_file.seek(0)
    for row in reader:
        if row['Дата'] == search_date.strftime('%Y-%m-%d'):
            search = (row['Дата'], row['Курс Доллара'])
            search_tuple(search)


def search_x_y_csv(w_file_y, w_file_x, str_date) -> None:
    """
    Принимает на вход данные x и y, пытается объединить их для дальнейшей записи в кортеж.
    :param w_file_x: Входные данные x.
    :param w_file_y: Входные данные y.
    :param str_date: Дата.
    """
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


def search_tuple(search) -> None:
    """
    Принимает на вход данные и записывает их в кортеж (функция не дописана(((().
    :param search: Входные данные.
    """
    search_all = tuple()
    search_all += search
    print("Comon", search)




