import pandas as pd
import csv
import os
import matplotlib.pyplot as plt
import random
import cv2


def create_histogram(df: pd.DataFrame, mark_class: int) -> None:
    """ Создание гистограммы по метке класса и ее вывод
        :arg :
            df (pd.DataFrame) : массив данных
            mark_class (int) : метка класса
    """
    path_image_list = filter_dataframe_mark_class(df, "Num_class", mark_class)
    i = random.randint(0, len(path_image_list))
    path_way = path_image_list.iloc[i, 0]
    img = cv2.imread(path_way)
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])

    plt.ylabel('Number of pixels')
    plt.xlabel('Pixel value')
    plt.title('Histogram')
    plt.show()


def read_csv(name_of_csv: str, num_of_columns: int):
    """ Чтение csv файла по колонкам
        :arg :
            name_of_csv (str) : название csv файла
            num_of_columns (int) : номер колонки
        :return
            list of lists
    """
    with open(name_of_csv, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        read_list = []
        for row in reader:
            if num_of_columns == 1:
                share_list = row[0].split(';')
                read_list.append(share_list[0])
            else:
                share_list = row[0].split(';')
                read_list.append(share_list[2])
    return read_list


def filter_dataframe_mark_class(df: pd.DataFrame, column: str, value: int) -> pd.DataFrame:
    """Фильтрация по метке класса
        :arg :
            df (pd.DataFrame) : массив данных
            column (str) : название колонки
            value (int) : метка класса
        :return: df (pd.DataFrame) : массив данных
    """
    df = df[df[column] == value]
    print(df)
    # save dataframe to csv file
    df.to_csv("filter_dataframe_mark_class.csv", sep='\t', encoding='utf-8')
    return df


def filter_dataframe_wight_and_height_and_mark(df: pd.DataFrame, column1: str, column2: str, column3: str, value1: int,
                                               value2: int, value3: int) -> pd.DataFrame:
    """ Фильтрация по ширине, высоте и метке класса
        :arg:
            df (pd.DataFrame) : массив данных
            column1 (str) : название колонки 1
            column2 (str) : название колонки 2
            column3 (str) : название колонки 3
            value1 (int) : граница фильтрации 1
            value2 (int) : граница фильтрации 2
            value3 (int) : граница фильтрации 3
        :return:
            df (pd.DataFrame) : массив данных
    """
    df = df[(df[column1] <= value1) & (df[column2] <= value2) & (df[column3] == value3)]
    print(df)
    # save dataframe to csv file
    df.to_csv("filter_dataframe_wight_and_height.csv", sep='\t', encoding='utf-8')
    return df


def group_dataframe_pixel(df: pd.DataFrame) -> pd.DataFrame:
    """Группировка по количеству пикселей
        :arg:
            df (pd.DataFrame) : массив данных
        :return:
            df (pd.DataFrame) : массив данных
    """
    # copy dataframe
    df1 = df.copy()
    # rename column
    df1.rename(columns={'Number_of_pixels': 'Min_pixel'}, inplace=True)
    # copy column
    df1['Max_pixel'] = df1['Min_pixel']
    df1['Mean_pixel'] = df1['Min_pixel']

    # group dataframe by column
    df1 = df1.groupby(['Class']).agg({'Min_pixel': 'min', 'Max_pixel': 'max', 'Mean_pixel': 'mean'})
    print(df1)

    df1.to_csv("group_dataframe_pixel.csv", sep='\t', encoding='utf-8')


def create_dataframe(path_of_csv: str) -> pd.DataFrame:
    """Создание dataframe из csv файла
        :arg:
            path_of_csv (str): путь к файлу csv
        :return:
            df (pd.DataFrame) : массив данных
    """
    list_abs_way = read_csv(path_of_csv, 1)
    list_name_class = read_csv(path_of_csv, 3)
    list_mark = ["Num_class"]
    list_image_width = ["Image_width"]
    list_image_height = ["Image_hight"]
    list_image_depth = ["Number_of_chanel"]
    list_image_pix = ["Number_of_pixels"]
    for row in list_name_class:
        if row == "tiger":
            list_mark.append("0")
        if row == "leopard":
            list_mark.append("1")

    for row in list_abs_way:
        if row == "Absolute way":
            continue
        else:
            image = plt.imread(row)
            list_image_width.append(image.shape[0])
            list_image_height.append(image.shape[1])
            list_image_depth.append(image.shape[2])
            list_image_pix.append(image.size)

    for i in range(1, len(list_abs_way)):
        try:
            list_abs_way[i] = os.path.abspath(list_abs_way[i])
        except:
            pass

    data = {
        list_abs_way[0]: list_abs_way[1:],
        list_name_class[0]: list_name_class[1:],
        list_mark[0]: list_mark[1:],
        list_image_width[0]: list_image_width[1:],
        list_image_height[0]: list_image_height[1:],
        list_image_depth[0]: list_image_depth[1:],
        list_image_pix[0]: list_image_pix[1:]
    }
    df = pd.DataFrame(data)
    return df


class Encryptor:
    def cryptWord(self, word) -> str:
        """Шифрование слова
              :arg:
              word (str) : слово
              :return:
              new_word (str) : зашифрованное слово
          """
        if " " not in word:
            new_word = "";
            for i in range(len(word)):
                char_value = ord(word[i])
                new_word += chr(char_value + 2)

            return new_word

        raise ValueError()

    def cryptWordToNumbers(self, word) -> str:
        """Шифрование слова в числа
            :arg:
            word (str) : слово
            :return:
            new_word (str) : зашифрованное слово
        """
        if " " in word:
            raise ValueError()

        new_word = "";
        for i in range(len(word)):
            char_value = ord(word[i])
            new_word += str(char_value + 2)

        return new_word

    def cryptWordWithCharsToReplace(self, word, chars_to_replace) -> str:
        """ Шифрование слова с заменой символов
            :arg:
            word (str) : слово
            chars_to_replace (list) : список символов для замены
            :return:
            new_word (str) : зашифрованное слово
        """
        if " " in word:
            raise ValueError()
        result = list(word)
        for i in range(len(word)):
            for j in range(len(chars_to_replace)):
                if chars_to_replace[j] == word[i]:
                    char_value = ord(word[i])
                    result[i] = chr(char_value + 2)
        return "".join(result)

    def cryptSentence(self, sentence) -> str:
        """ Шифрование предложения
            :arg:
            sentence (str) : предложение
            :return:
            new_word (str) : зашифрованное предложение
        """
        new_word = "";
        for i in range(len(sentence)):
            char_value = ord(sentence[i])
            new_word += chr(char_value + 2)

        return new_word

    def getWords(self, sentence) -> list:
        """ Получение списка слов из предложения
            :arg:
            sentence (str) : предложение
            :return:
            words (list) : список слов
        """
        return sentence.split()

    def printWords(self, sentence):
        words = self.getWords(sentence)
        for word in words:
            print("<%s>" % word)
