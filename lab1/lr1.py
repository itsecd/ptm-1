from bs4 import BeautifulSoup
import requests
from time import sleep
import codecs


def find_good(url, pages, count_good):
    for page in range(1, pages+1):
        print(page)
        url1 = url + f"/{page}/"
        delay_value = 30 + 2 * page
        sleep(delay_value)
        r = requests.get(url1)
        soup = BeautifulSoup(r.text, "lxml")
        film_name = soup.find("a", class_="breadcrumbs__link")
        sources = soup.findAll("div", class_="response good")
        for src in sources:
            rev = src.find("span", class_="_reachbanner_").text
            if count_good < 10:
                name = str(count_good).zfill(4)
                file = codecs.open(u'' + "dataset/good/" + name + ".txt", "w", "utf-8")
                file.write(film_name.text + "\n")
                file.write(rev)
                file.close()
                count_good += 1
            elif 10 <= count_good < 100:
                name = str(count_good).zfill(4)
                file = codecs.open(u'' + "dataset/good/" + name + ".txt", "w", "utf-8")
                file.write(film_name.text + "\n")
                file.write(rev)
                file.close()
                count_good += 1
            elif 100 <= count_good <= 999:
                name = str(count_good).zfill(4)
                file = codecs.open(u'' + "dataset/good/" + name + ".txt", "w", "utf-8")
                file.write(film_name.text + "\n")
                file.write(rev)
                file.close()
                count_good += 1
    return count_good


def find_bad(url, pages, count_bad):
    for page in range(1, pages+1):
        print(page)
        url1 = url + f"/{page}/"
        delay_value = 30 + 2 * page
        sleep(delay_value)
        r = requests.get(url1)
        soup = BeautifulSoup(r.text, "lxml")
        film_name = soup.find("a", class_="breadcrumbs__link")
        sources = soup.findAll("div", class_="response bad")
        for src in sources:
            rev = src.find("span", class_="_reachbanner_").text
            if count_bad < 10:
                name = str(count_bad).zfill(4)
                file = codecs.open(u'' + "dataset/bad/" + name + ".txt", "w", "utf-8")
                file.write(film_name.text + "\n")
                file.write(rev)
                file.close()
                count_bad += 1
            elif 10 <= count_bad < 100:
                name = str(count_bad).zfill(4)
                file = codecs.open(u'' + "dataset/bad/" + name + ".txt", "w", "utf-8")
                file.write(film_name.text + "\n")
                file.write(rev)
                file.close()
                count_bad += 1
            elif 100 <= count_bad <= 999:
                name = str(count_bad).zfill(4)
                file = codecs.open(u'' + "dataset/bad/" + name + ".txt", "w", "utf-8")
                file.write(film_name.text + "\n")
                file.write(rev)
                file.close()
                count_bad += 1
    return count_bad
