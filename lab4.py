import csv
import cv2
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd


def class_filter(dataframe: pd.DataFrame, class_mark: int)-> pd.DataFrame:
    """сортирует по классы

    Args:
        dataframe (pd.DataFrame): датафрейм
        class_mark (int): метка класса

    Returns:
        pd.DataFrame: отсортированный датафрейм
    """
    res = pd.DataFrame(dataframe[dataframe.class_mark == class_mark])
    return res


def size_filter(dataframe: pd.DataFrame, class_mark: int,  max_hight:int, max_width: int)-> pd.DataFrame:
    """сортирует по классу и размеру изображения

    Args:
        dataframe (pd.DataFrame): датафрейм
        class_mark (int): метка класса

    Returns:
        pd.DataFrame: отсортированный датафрейм
    """
    res = pd.DataFrame(dataframe[dataframe.class_mark == class_mark]
                       [dataframe.hight <= max_hight][dataframe.width <= max_width])
    return res


def create_histogram(dataframe: pd.DataFrame, class_mark:int) -> dict[str, object]:
    """функция принимает датафрейм и метку класса, возвращает словарь гистограммы и цвета

    Args:
        dataframe (pd.DataFrame): датафрейм
        class_mark (int): метка класса
    Returns:
        dict[str, object]: словарь гистограммы и цвета
    """
    if (class_mark == 0):
        class_name = "rose"
    else:
        class_name = "tilip"

    rand_index = random.randint(0, 1020)
    filtrated_dataframe = class_filter(dataframe, class_mark)
    "data['name'].loc[data.index[1]]"
    path_to_image = filtrated_dataframe["absolute_way"].loc[filtrated_dataframe.index[rand_index]]
    image = cv2.imdecode(np.fromfile(
        path_to_image, dtype=np.uint8), cv2.IMREAD_COLOR)
    cv2.imshow(f"Изображение {class_name}:{path_to_image}", image)
    cv2.waitKey(0)
    full_histr = {}
    colors = ("b", "g", "r")
    for i in range(3):
        histr = cv2.calcHist([image], [i], None, [256], [0, 256])
        full_histr[f"{colors[i]}"] = histr
    return full_histr


def draw_histogram(full_histr:dict[str, object])-> None:
    """рисует гистограмму

    Args:
        full_histr (dict[str, object]): словарь гистограммы и цвета
    """
    plt.xlabel('Интенсивность')
    plt.ylabel('Количество пикселей')
    plt.title(
        'Гистограмма количества пикселей для каждого рассматриваемого значения интенсивности')
    plt.legend(['blue', 'green', 'red'])
    for item in full_histr.items():
        plt.plot(item[1], color=item[0])
        plt.xlim([0, 256])
    plt.show()


def create()-> None:
    """функция где ведется основная работа
    """
    filename = "annotation.csv"
    class_mark = []
    class_name = []
    absolute_way = []
    with open(filename, encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            if row[2] == "rose":
                class_mark.append(0)
            else:
                class_mark.append(1)

            class_name.append(row[2])
            absolute_way.append(row[0])

    dataframe = pd.DataFrame(
        {
            class_name[0]: pd.array(class_name[1:]),
            absolute_way[0]:  pd.array(absolute_way[1:]),
        }
    )

    dataframe = dataframe.rename(
        columns={class_name[0]: "class_name",
                 absolute_way[0]: "absolute_way"}
    )

    dataframe["class_mark"] = pd.array(class_mark[1:])

    hight = []
    width = []
    depth = []

    for path in absolute_way:
        try:
            image = cv2.imdecode(np.fromfile(
                path, dtype=np.uint8), cv2.IMREAD_COLOR)
            hight.append(image.shape[0])
            width.append(image.shape[1])
            depth.append(image.shape[2])
        except:
            pass

    dataframe["hight"] = pd.Series(hight)
    dataframe["width"] = pd.Series(width)
    dataframe["depth"] = pd.Series(depth)

    print("\n Images hight statistic: \n")
    print(dataframe["hight"]. describe())

    print("\n Images width statistic: \n")
    print(dataframe["width"]. describe())

    print("\n Images depth statistic: \n")
    print(dataframe["depth"]. describe())

    print("\n Filtrated dataframe(class): \n")
    print(class_filter(dataframe, 0))

    print("\n Filtrated dataframe(size and class): \n")
    print(size_filter(dataframe, 1, 400, 400))

    number_of_pixels = []

    for path in absolute_way:
        try:
            image = cv2.imdecode(np.fromfile(
                path, dtype=np.uint8), cv2.IMREAD_COLOR)
            number_of_pixels.append(image.size)
        except:
            pass

    dataframe["number_of_pixels"] = pd.Series(number_of_pixels)

    print(" \n Minimum number of pixels: \n ")
    print(dataframe.groupby("class_mark").number_of_pixels.min())

    print(" \n Maximum number of pixels: \n ")
    print(dataframe.groupby("class_mark").number_of_pixels.max())

    print(" \n The average value of the number of pixels: \n ")
    print(dataframe.groupby("class_mark").number_of_pixels.mean())

    print(dataframe.columns)
    print(dataframe)

    draw_histogram(create_histogram(dataframe, 0))


def main():
    print("start")
    pd.set_option("display.max_colwidth", None)
    create()
    print("finish")


if __name__ == "__main__":
    main()