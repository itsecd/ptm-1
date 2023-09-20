import os
import random
import string
import time

import cv2
import numpy as np
import requests

from bs4 import BeautifulSoup
from tqdm import tqdm

DOG_PATH = "C:/Users/User/nuck figgers/dataset/dog"
CAT_PATH = "C:/Users/User/nuck figgers/dataset/cat"


def get_images(count_images: int, path: str, type_name: str, indexs: int = None) -> None or int:
    """Photo parsing function

    Args:
        count_images (int): Counter of parsed photos
        path (str): Path to the folder to save the photo
        type_name (str): Type of image for parsing
        indexs (int, optional): Index of not uploaded photos. Defaults to None.

    Returns:
        None or int: Index of missing photos

    """
    
    if not os.path.exists("C:/Users/User/nuck figgers/dataset"):
        os.mkdir("C:/Users/User/nuck figgers/dataset")
    if not os.path.exists(path):
        os.mkdir(path)
    count = 0
    for i in tqdm(range(1, 99), desc="Страница "):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.sample(letters, 7))
        _headers = {
            "User-Agent": rand_string
        }
        if not type_name == "cat":
            url = f"https://yandex.ru/images/search?p={i}&text=dog& \
                    uinfo=sw-1920-sh-1080-ww-912-wh-881-pd-1.100000 \
                    023841858-wp-16x9_2560x1440&lr=51&rpt=image"
        else:
            url = f"https://yandex.ru/images/search?p={i}&text=cat& \
                    uinfo=sw-1920-sh-1080-ww-878-wh-924-pd-1-wp-16x \
                    9_1920x1080&lr=51&rpt=image"
        req = requests.get(url, headers=_headers)
        soup = BeautifulSoup(req.text, "html.parser")
        src_list = []
        for link in soup.find_all("img", class_="justifier__thumb"):
            src_list.append(link.get("src"))
        for img_url in tqdm(src_list, desc="Скчивание картинок "):
            if img_url.find("n=13") != -1:
                try:
                    source = "https:" + img_url
                    picture = requests.get(source)
                    if indexs != None:
                        name_file = str(indexs[count])
                    else:
                        name_file = str(count)
                    with open(os.path.join(path,
                              f"{name_file.zfill(4)}.jpg"),
                              "wb") as out:
                        out.write(picture.content)
                        out.close()
                    time.sleep(0.5)
                    count += 1
                    if(count == count_images):
                        return i
                except Exception:
                    if indexs[count] == IndexError:
                        return None
                    print("Error in: \n", count)


def is_similar(image1, image2) -> bool:
    """Photo comparison function

    Args:
        image1 : First foto
        image2 : Second foto

    Returns:
        bool: True or False

    """
    
    return image1.shape == image2.shape and not(
        np.bitwise_xor(image1, image2).any())


def check_images(path: str) -> list:
    """A function that goes through photos and compares them

    Args:
        path (str): Path to the folder to save the photo

    Returns:
        list: List with indexes of all copies
    """
    
    images = []
    images2 = []
    for file_name in os.listdir(path):
        images.append((cv2.imread(os.path.join(path, file_name)),
                      os.path.join(path, file_name)))
        images2.append((cv2.imread(os.path.join(path, file_name)),
                        os.path.join(path, file_name)))
    indexs = []
    for im, fname in tqdm(images):
        for im2, fname2 in images2:
            if(fname == fname2):
                continue
            if is_similar(im, im2):
                print(fname, fname2)
                temp = fname2.replace(f"{path}\\", "")
                temp = temp.replace(".jpg", "")
                indexs.append(int(temp))
                try:
                    os.remove(fname2)
                except Exception as e:
                    print(e)
                    pass
    return indexs


def main():
    """Main function"""
    
    count_find = 1250
    get_images(count_find, DOG_PATH, "dog")
    print("Пауза")
    for sec in tqdm(range(1, 121), ):
        time.sleep(1)
    get_images(count_find, CAT_PATH, "cat")
    indexs = check_images(DOG_PATH)
    get_images(count_find, DOG_PATH, "dog", indexs)
    print("Пауза")
    for sec in tqdm(range(1, 121), ):
        time.sleep(1)
    indexs = check_images(CAT_PATH)
    get_images(count_find, CAT_PATH, "cat", indexs)


if __name__ == "__main__":
    main()
