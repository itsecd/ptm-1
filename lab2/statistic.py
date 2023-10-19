import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pymystem3 import Mystem
from data_iter import MyIter


def create_hist(mark: str, path_bad: str, path_good: str) -> plt:
    """
    Функция считывает использование слов в обзорах и возвращает столбичную диаграмму
    :param mark: Тип обзора
    :param path_good: Путь к датасету положительных обзоров
    :param path_bad: Путь к датасету отрицательных обзоров
    :return: гистограмма
    """
    keys = []
    vals = []
    if mark == "good":
        fl = open(path_good, "r")
        for i in fl.readlines():
            key, val = i.strip().split(":")
            val = int(val)
            if val > 800:
                keys.append(key)
                vals.append(val)
    else:
        fl = open(path_bad, "r")
        for i in fl.readlines():
            key, val = i.strip().split(":")
            keys.append(key)
            vals.append(val)
    position = np.arange(len(vals))
    fig, ax = plt.subplots()
    ax.bar(position, vals)
    ax.set_xticks(position)
    ax.set_xticklabels(keys)
    fig.set_figwidth(1000)
    fig.set_figheight(1000)
    return fig


def lemmatize_and_count(df: pd, mark: str, ing: str) -> None:
    """
    Функция производит токенизацию и лемматизацию обзоров из датафрейма по заданной метке и записывает полученную
    информацию в файл
    :param df: Датафрейм с обзорами
    :param mark: Тип обзора
    :param ing: Название папки для сохранения информации
    :return:
    """
    words = {}
    df_new = filter_by_mark(df, mark)
    lemmatizer = Mystem()
    text = df_new["rev_text"]
    text = list(text)
    for sent in text:
        sent_lemmas = lemmatizer.lemmatize(sent)
        print(sent_lemmas)
        for word in sent_lemmas:
            if word not in words and (len(word) >= 3 or word == "я"):
                words[word] = 1
            if word in words:
                words[word] += 1
        print(words)
    path = "".join([ing, ".txt"])
    f = open(path, "a")
    for word in words:
        f.write(word + ": " + str(words[word]) + "\n")
    f.close()


def filter_by_mark(df: pd, mark: str) -> pd:
    """
    Функция создает новый датафрейм в котором присутствуют только обзоры соответствующего типа
    :param df: старый датафрейм
    :param mark: тип обзора
    :return: новый датафрейм
    """
    return df[df["rev_type"] == mark]


def filter_by_number(df: pd, w_num: int) -> pd:
    """
    Функция фильтрует датафрейм по количеству слов в обзоре, возвращает новый датафрейм, в котором присутствую
    обзоры только с соответствующим количеством слов
    :param df: старый датафрейм
    :param w_num: количество слов
    :return: новый датафрейм
    """
    return df[df["word_num"] <= w_num]


def read_all_data(path_good: str, path_bad: str) -> pd:
    """
    С использованием класса итератора из предыдущей работы записывает обзоры в датафрейм.
    :param path_bad: Путь к датасету с отрицательными обзорами
    :param path_good: Путь к датасету с положительными обзорами
    :return: новый датафрейм
    """
    rev_types = []
    rev_text = []
    word_num = []
    it_good = MyIter("good", path_good)
    it_bad = MyIter("bad", path_bad)
    for data in it_good:
        rev_types.append("good")
        f = open(data, "r")
        txt = f.read()
        word_num.append(len(txt.split()))
        rev_text.append(txt)
        f.close()
    for data in it_bad:
        rev_types.append("bad")
        f = open(data, "r")
        txt = f.read()
        word_num.append(len(txt.split()))
        rev_text.append(txt)
        f.close()
    dt = pd.DataFrame(
        {
            "rev_type": rev_types,
            "rev_text": rev_text,
            "word_num": word_num
        }
    )
    return dt
