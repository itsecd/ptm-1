import codecs
import requests
from bs4 import BeautifulSoup


def find_good(url: str, pages: int, count_good: int, save_path: str) -> int:
    """
    Функция записывает положительные отзывы со страницы фильма на сайте кинопоиск в датасет.
    :param url: Ссылка на страницу фильма
    :param pages: количество страниц с отзывами на фильм
    :param count_good: текущее значение счетчика записанных отзывов
    :param save_path: папка, в которую сохраняются обзоры
    :return:новое значение счетчика
    """
    for page in range(1, pages+1):
        print(page)
        url1 = url + f"/{page}/"
        r = requests.get(url1)
        soup = BeautifulSoup(r.text, "lxml")
        film_name = soup.find("a", class_="breadcrumbs__link")
        sources = soup.findAll("div", class_="response good")
        for src in sources:
            rev = src.find("span", class_="_reachbanner_").text
            if count_good < 10:
                name = str(count_good).zfill(4)
                file = codecs.open(u'' + save_path + name + ".txt", "w", "utf-8")
                file.write(film_name.text + "\n")
                file.write(rev)
                file.close()
                count_good += 1
            elif 10 <= count_good < 100:
                name = str(count_good).zfill(4)
                file = codecs.open(u'' + save_path + name + ".txt", "w", "utf-8")
                file.write(film_name.text + "\n")
                file.write(rev)
                file.close()
                count_good += 1
            elif 100 <= count_good <= 999:
                name = str(count_good).zfill(4)
                file = codecs.open(u'' + save_path + name + ".txt", "w", "utf-8")
                file.write(film_name.text + "\n")
                file.write(rev)
                file.close()
                count_good += 1
    return count_good


def find_bad(url: str, pages: int, count_bad: int, save_path: str) -> int:
    """
    Функция записывает отрицательные отзывы со страницы фильма на сайте кинопоиск в датасет.
    :param url: Ссылка на страницу фильма
    :param pages: количество страниц с отзывами на фильм
    :param count_bad: текущее значение счетчика записанных отзывов
    :param save_path: папка в которую сохраняются обзоры
    :return: новое значение счетчика
    """
    for page in range(1, pages+1):
        print(page)
        url1 = url + f"/{page}/"
        r = requests.get(url1)
        soup = BeautifulSoup(r.text, "lxml")
        film_name = soup.find("a", class_="breadcrumbs__link")
        sources = soup.findAll("div", class_="response bad")
        for src in sources:
            rev = src.find("span", class_="_reachbanner_").text
            if count_bad < 10:
                name = str(count_bad).zfill(4)
                file = codecs.open(u'' + save_path + name + ".txt", "w", "utf-8")
                file.write(film_name.text + "\n")
                file.write(rev)
                file.close()
                count_bad += 1
            elif 10 <= count_bad < 100:
                name = str(count_bad).zfill(4)
                file = codecs.open(u'' + save_path + name + ".txt", "w", "utf-8")
                file.write(film_name.text + "\n")
                file.write(rev)
                file.close()
                count_bad += 1
            elif 100 <= count_bad <= 999:
                name = str(count_bad).zfill(4)
                file = codecs.open(u'' + save_path + name + ".txt", "w", "utf-8")
                file.write(film_name.text + "\n")
                file.write(rev)
                file.close()
                count_bad += 1
    return count_bad
