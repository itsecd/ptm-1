import csv

from the_fourth_task import search_X_Y_csv


def new_csv(w_file, str_date):
    ' Принимает dataset и разбивает на Х и Y'
    with open("X.csv", "w+", encoding='utf-8') as w_file_x:
        with open("Y.csv", "w+", encoding='utf-8') as w_file_y:
            file_writer_X = csv.writer(w_file_x, delimiter=",", lineterminator="\r")
            file_writer_Y = csv.writer(w_file_y, delimiter=",", lineterminator='')
            w_file.seek(0)
            for row in w_file:
                a = row.split(',')
                file_writer_Y.writerow([a[1]])
                file_writer_X.writerow([a[0]])
            search_X_Y_csv(w_file_y, w_file_x, str_date)


