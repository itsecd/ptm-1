# This is a sample Python script.
import os
from bs4 import BeautifulSoup
import requests
import time
import random

# подключаем библиотеки

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'}


def main():
    print("heum")
    if not os.path.isdir("Dataset"):
        os.mkdir("Dataset")
        os.chdir("Dataset")
        for i in range(1, 6):
            if not os.path.isdir(str(i)):
                os.mkdir(str(i))
        # Создаем папку датасет если ее нет, переходим в нее, и также создаем 5 папок если их еще нет
    url = 'https://www.livelib.ru/reviews'
    second_url = 'https://www.livelib.ru'
    number_elem = 3300
    
    number_page = 125
    quotes_1 = 76
    quotes_2 = 108
    quotes_3 = 314
    quotes_4 = 824
    quotes_5 = 998  # Задаем переменные для счета, а также инициализируем нужные ссылки не нули потому что после бана
    # нужно начинать не с начала
    while number_elem < 5000:
        response = requests.get(url, headers)  # Собственно записываем в переменную нтмл текст.после используем его
        response.encoding = "utf-8"
        # print(response.text)
        soup = BeautifulSoup(response.text, 'lxml')
        items = soup.find_all(class_="footer-card__link", href=True)
        href = []
        for item in items:
            href.append(item.get('href'))
        print(href)
        # Заходим на страницу и парсим все ссылки на полные отзывы.
        time.sleep(random.randint(10, 15))
        for i in range(len(href)):
            sec_response = requests.get(second_url + href[i])
            sec_response.encoding = "utf-8"
            sec_soup = BeautifulSoup(sec_response.text, 'lxml')
            quotes = sec_soup.find_all(class_="lenta-card__mymark")  # ищем все что нам надо и записываем это
            names = sec_soup.find_all(class_="lenta-card__book-title")
            texts = sec_soup.find_all("div", {"id": "lenta-card__text-review-full"})
            authors = sec_soup.find_all(class_="lenta-card__author")
            new_quotes = []
            for quote in quotes:
                new_quotes.append(str((quote.text.replace(" ", "")).replace("\n", "")))
            # заходим на в каждый отзыв и берем оттуда все нужные данные
            # print(str(len(new_quotes)) + " " + str(len(names))+" "+str(len(texts))+" "+str(len(authors)))
            # количество найденных данных Используется не количество найденных ссылок а мин значение из найденых
            # элементов, так ка бывает что отзыв без оценки или автора..
            y = min(len(authors), len(names), len(texts), len(new_quotes))
            if y == 0:
                continue
            print(i, y, len(authors), len(names), len(texts), new_quotes)
            x = float(new_quotes[0])
            # Сортируем отзывы по оценкам и записываем в txt файл, W+ запись и чтение(модификатор)
            if 4.5 <= x <= 5:
                quotes_5 = quotes_5 + 1
                if quotes_5 >= 1000:
                    continue
                namefile = str(quotes_5).zfill(4)
                with open("dataset/" + "5" + '/' + namefile + '.txt', 'w+', encoding="utf-8") as file:
                    file.write('Оценка: ' + str(x) + '\n' + 'Название: ' + names[0].text + '\n' + 'Автор книги: ' +
                               authors[0].text + '\n' + 'Рецензия:' + '\n' + texts[0].text)
                number_elem = number_elem + 1
            elif 3.5 <= x < 4.5:
                quotes_4 = quotes_4 + 1
                if quotes_4 >= 1000:
                    continue
                namefile = str(quotes_4).zfill(4)
                with open("dataset/" + "4" + '/' + namefile + '.txt', 'w+', encoding="utf-8") as file:
                    file.write('Оценка: ' + str(x) + '\n' + 'Название: ' + names[0].text + '\n' + 'Автор книги: ' +
                               authors[0].text + '\n' + 'Рецензия:' + '\n' + texts[0].text)
                number_elem = number_elem + 1
            elif 2.5 <= x < 3.5:
                quotes_3 = quotes_3 + 1
                if quotes_3 >= 1000:
                    continue
                namefile = str(quotes_3).zfill(4)
                with open("dataset/" + "3" + '/' + namefile + '.txt', 'w+', encoding="utf-8") as file:
                    file.write('Оценка: ' + str(x) + '\n' + 'Название: ' + names[0].text + '\n' + 'Автор книги: ' +
                               authors[0].text + '\n' + 'Рецензия:' + '\n' + texts[0].text)
                number_elem = number_elem + 1
            elif 1.5 <= x < 2.5:
                quotes_2 = quotes_2 + 1
                if quotes_2 >= 1000:
                    continue
                namefile = str(quotes_2).zfill(4)
                with open("dataset/" + "2" + '/' + namefile + '.txt', 'w+', encoding="utf-8") as file:
                    file.write('Оценка: ' + str(x) + '\n' + 'Название: ' + names[0].text + '\n' + 'Автор книги: ' +
                               authors[0].text + '\n' + 'Рецензия:' + '\n' + texts[0].text)
                number_elem = number_elem + 1
            else:
                quotes_1 = quotes_1 + 1
                if quotes_1 >= 1000:
                    continue
                namefile = str(quotes_1).zfill(4)
                with open("dataset/" + "1" + '/' + namefile + '.txt', 'w+', encoding="utf-8") as file:
                    file.write('Оценка: ' + str(x) + '\n' + 'Название: ' + names[0].text + '\n' + 'Автор книги: ' +
                               authors[0].text + '\n' + 'Рецензия:' + '\n' + texts[0].text)
                number_elem = number_elem + 1
            #time.sleep(random.randint(55, 60))
            # прибавляем счетчик
            # #режим ждуна шоб не забанило
        number_page = number_page + 1  # Инкрементируем счетчик страниц и перелистываем страничку, после все заново
        url = 'https://www.livelib.ru/reviews' + '~' + str(number_page) + '#reviews'
        # И так 5000 раз :)


if __name__ == "__main__":  # запуск мейна
    main()