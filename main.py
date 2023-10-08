import os
import requests
import time
import random
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)  AppleWebKit/537.36 (KHTML, like Gecko)"
                  "Chrome/39.0.2171.95 Safari/537.36"}
MAX_QOUTES = 1000
RATING = [1.5, 2.5, 3.5, 4.5, 5]


def main():
    if not os.path.isdir("Dataset"):
        os.mkdir("Dataset")
        os.chdir("Dataset")
        for i in range(1, 6):
            if not os.path.isdir(str(i)):
                os.mkdir(str(i))
    url = "https://www.livelib.ru/reviews"
    second_url = "https://www.livelib.ru"
    number_elem = 3300
    number_page = 125
    quotes_1 = 76
    quotes_2 = 108
    quotes_3 = 314
    quotes_4 = 824
    quotes_5 = 998
    while number_elem < 5000:
        response = requests.get(url, HEADERS)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "lxml")
        items = soup.find_all(class_="footer-card__link", href=True)
        href = []
        for item in items:
            href.append(item.get("href"))
        print(href)
        time.sleep(random.randint(10, 15))
        for i in range(len(href)):
            sec_response = requests.get(second_url + href[i])
            sec_response.encoding = "utf-8"
            sec_soup = BeautifulSoup(sec_response.text, "lxml")
            quotes = sec_soup.find_all(class_="lenta-card__mymark")
            names = sec_soup.find_all(class_="lenta-card__book-title")
            texts = sec_soup.find_all(
                "div", {"id": "lenta-card__text-review-full"})
            authors = sec_soup.find_all(class_="lenta-card__author")
            new_quotes = []
            for quote in quotes:
                new_quotes.append(
                    str((quote.text.replace(" ", "")).replace("\n", "")))
            min_length = min(len(authors), len(names), len(texts), len(new_quotes))
            if min_length == 0:
                continue
            print(i, min_length, len(authors), len(names), len(texts), new_quotes)
            rating = float(new_quotes[0])
            if RATING[3] <= rating <= RATING[4]:
                quotes_5 = quotes_5 + 1
                if quotes_5 >= MAX_QOUTES:
                    continue
                file_name = str(quotes_5).zfill(4)
                with open("dataset/" + "5" + "/" + file_name + ".txt", "w+", encoding="utf-8") as file:
                    file.write("Оценка: " + str(rating) + "\n" + "Название: " + names[0].text + "\n" + "Автор книги: " +
                               authors[0].text + '\n' + "Рецензия:" + "\n" + texts[0].text)
                number_elem = number_elem + 1
            elif RATING[2] <= rating < RATING[3]:
                quotes_4 = quotes_4 + 1
                if quotes_4 >= MAX_QOUTES:
                    continue
                file_name = str(quotes_4).zfill(4)
                with open("dataset/" + "4" + "/" + file_name + ".txt", "w+", encoding="utf-8") as file:
                    file.write("Оценка: " + str(rating) + "\n" + "Название: " + names[0].text + "\n" + "Автор книги: " +
                               authors[0].text + "\n" + "Рецензия:" + "\n" + texts[0].text)
                number_elem = number_elem + 1
            elif RATING[1] <= rating < RATING[2]:
                quotes_3 = quotes_3 + 1
                if quotes_3 >= MAX_QOUTES:
                    continue
                file_name = str(quotes_3).zfill(4)
                with open("dataset/" + "3" + "/" + file_name + ".txt", "w+", encoding="utf-8") as file:
                    file.write("Оценка: " + str(rating) + "\n" + "Название: " + names[0].text + "\n" + "Автор книги: " +
                               authors[0].text + "\n" + "Рецензия:" + "\n" + texts[0].text)
                number_elem = number_elem + 1
            elif RATING[0] <= rating < RATING[1]:
                quotes_2 = quotes_2 + 1
                if quotes_2 >= MAX_QOUTES:
                    continue
                file_name = str(quotes_2).zfill(4)
                with open("dataset/" + "2" + "/" + file_name + ".txt", "w+", encoding="utf-8") as file:
                    file.write("Оценка: " + str(rating) + "\n" + "Название: " + names[0].text + "\n" + "Автор книги: " +
                               authors[0].text + "\n" + "Рецензия:" + "\n" + texts[0].text)
                number_elem = number_elem + 1
            else:
                quotes_1 = quotes_1 + 1
                if quotes_1 >= MAX_QOUTES:
                    continue
                file_name = str(quotes_1).zfill(4)
                with open("dataset/" + "1" + '/' + file_name + ".txt", "w+", encoding="utf-8") as file:
                    file.write("Оценка: " + str(rating) + "\n" + "Название: " + names[0].text + "\n" + "Автор книги: " +
                               authors[0].text + "\n" + "Рецензия:" + "\n" + texts[0].text)
                number_elem = number_elem + 1
        number_page = number_page + 1
        url = "https://www.livelib.ru/reviews" + \
            "~" + str(number_page) + "#reviews"


if __name__ == "__main__":
    main()
