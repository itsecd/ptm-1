import requests
from bs4 import BeautifulSoup as BS
import csv
import os


def pars_all_group() -> None:
    '''
    Парсинг с ssau.ru ссылок на расписания всех групп и дальнейшая запись в соответствующие csv-файлы
    '''
    os.makedirs('AllGroupShedule', exist_ok=True)
    for num_course in range(1, 6):
        url = f'https://ssau.ru/rasp/faculty/492430598?course={num_course}'
        response = requests.get(url)
        soup = BS(response.content, 'html.parser')
        list_url = []
        list_group = []
        for item in soup.find_all('a', class_="btn-text group-catalog__group"):
            list_url.append(item.get('href'))
            span_item = item.find('span')
            list_group.append(span_item.contents[0])

        for i in range(len(list_url)):
            with open(f"AllGroupShedule/AllGroup_course_{num_course}.csv", "a", newline="", encoding="utf-8") as file:
                printer = csv.writer(file, delimiter=";")
                printer.writerow([
                    "https://ssau.ru" + str(list_url[i]),
                    str(list_group[i])
                ])


def find_schedule_url(num_group: str, selectedWeek: str, selectedWeekday: str) -> str:
    '''
    Поиск среди спарсенных ссылок необхимой
    Функция возвращает ссылку в виде строки
    '''
    with open(f"AllGroupShedule/AllGroup_course_{num_group[1]}.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            if row[1] == num_group:
                result = f"{row[0]}&selectedWeek={selectedWeek}&selectedWeekday={selectedWeekday}"
                return result


def pars_shedule(url: str) -> str:
    '''
    Парсинг рассписания по ссылке и форматирование под красивый вид результирующей строки
    '''
    result = ""
    current_date = ""
    list_lessons = []
    list_lessons_time = [
        "8:00 - 9:35",
        "9:45 - 11:20",
        "11:30 - 13:05",
        "13:30 - 15:05",
        "15:15 - 16:50",
        "17:00 - 18:35"
    ]
    list_lessons_type = []
    response = requests.get(url)
    soup = BS(response.content, "html.parser")
    current_date = soup.find(class_="week-nav-current_date")
    result += f"Расписание на {current_date.contents[0]}\n\n"
    for item in soup.find_all(class_="schedule__item schedule__item_show"):
        index = 1
        last_num_of_lessons = len(list_lessons)
        while index != 5:
            try:
                name_lesson = item.find(
                    class_=f"body-text schedule__discipline lesson-color lesson-color-type-{index}")
                list_lessons.append(str(name_lesson.contents[0]))
                if last_num_of_lessons < len(list_lessons):
                    if index == 1:
                        list_lessons_type.append("(ЛЕКЦИЯ)")
                    if index == 2:
                        list_lessons_type.append("(ЛАБОРАТОРНАЯ)")
                    if index == 3:
                        list_lessons_type.append("(ПРАКТИКА)")
                    if index == 4:
                        list_lessons_type.append("(ДРУГОЕ)")
            except:
                pass
            index += 1
        if last_num_of_lessons == len(list_lessons):
            list_lessons.append("None")
            list_lessons_type.append("(None)")
    for index in range(len(list_lessons)):
        result += f"{list_lessons_time[index]}\t{list_lessons[index]}\t{list_lessons_type[index]}\n"
    return result
