import os
import re
import time

import cv2
import numpy as np
import requests
from bs4 import BeautifulSoup


def scraping(typename: str,indexs=None):
    """
    Загружает изображения в папку dataset + typename

            Параметры:
                    typename(str): название папки с изображениями
                    indexs: номер изображения   
    """

    if not os.path.exists("dataset"):
        os.mkdir("dataset")
    if not os.path.exists("dataset/" + typename):
        os.mkdir("dataset/" + typename)

    count = 0
    for i in range(0, 99):

        if typename != "cat":
            url = f"https://yandex.ru/images/search?p={i}&text=dog&uinfo=sw-1920-sh-1080-ww-912-wh-881-pd-1.100000023841858-wp-16x9_2560x1440&lr=51&rpt=image"
        else:
            url = f"https://yandex.ru/images/search?p={i}&text=cat&uinfo=sw-1920-sh-1080-ww-878-wh-924-pd-1-wp-16x9_1920x1080&lr=51&rpt=image"

        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        images = soup.find_all('img', class_="justifier__thumb")

        src_list = []

        for image in images:
            src_list.append(image.get("src"))

        for img in src_list:
            if img.find("n=13") != -1:
                try:
                    source = "https:" + img
                    picture = requests.get(source)
                    
                    if indexs != None:
                        name_file = str(indexs[count])
                    else:
                        name_file = str(count)
                        
                    out = open("dataset/"+ typename + "/" + name_file.zfill(4) + ".jpg", "wb")
                    out.write(picture.content)
                    out.close()

                    time.sleep(0.25)

                    count += 1

                except Exception as ex:
                    print(ex)
                    

def is_similar(image1: np.ndarray,image2: np.ndarray):
    """
    Возвращает булевское значение сравнения изображений

            Параметры:
                    image1(np.ndarray): Первое изображение
                    image2(np.ndarray): Второе изображение
    """

    return image1.shape == image2.shape and not(np.bitwise_xor(image1, image2).any())


def check_images(typename: str):
    """
    Возвращает отредактированный номер изображения

            Параметры:
                    typename(str): название папки с изображениями
    """
    
    path = "dataset/"+ typename

    images = []
    images2 = []
    for file_name in os.listdir(path):
        images.append((cv2.imread(os.path.join(path, file_name)),
                      os.path.join(path, file_name)))

        images2.append((cv2.imread(os.path.join(path, file_name)),
                        os.path.join(path, file_name)))

    indexs = []
    for im, fname in images:
        for im2, fname2 in images2:
            if(fname == fname2):
                continue

            if is_similar(im, im2):
                print(fname, fname2)

                try:
                    os.remove(fname)
                except Exception as e:
                    print(e)

                temp = fname.replace(f"{path}\\", "")
                temp = temp.replace(".jpg", "")
                indexs.append(int(temp))

                try:
                    images2.remove(fname)
                except Exception:
                    continue

    return indexs


def parser(typename: str):
    """
    Функция отредактированного заполнения папок с изображениями

            Параметры:
                    typename(str): название папки с изображениями
    """
    scraping(typename)

    indexs = check_images(typename)
    scraping(typename, indexs)