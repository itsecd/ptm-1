import os
import string
import random
import time
import requests
from bs4 import BeautifulSoup
import cv2
import numpy as np
from tqdm import tqdm


zebra_path = "C://Users/79376/python/dataset/zebra"
dataset_path ="C://Users/79376/python/dataset"
bay_horse_path = "C://Users/79376/python/dataset/bay_horse"


def get_data_zebra(count_imgs: int) -> None:
    '''Парсит картинки с зебрами'''
    if not os.path.exists(dataset_path):
        os.mkdir(dataset_path)   
    if not os.path.exists(zebra_path):
        os.mkdir(zebra_path)

    count = 0

    for i in range(0,999):
        
        letters = string.ascii_lowercase
        rand_string = ''.join(random.sample(letters, 10))
        
        _headers = {
            "User-Agent": rand_string
        }
        
        url = f"https://yandex.ru/images/search?p={i}&text=zebra&uinfo=sw-1920-sh-1080-ww-912-wh-881-pd-1.100000023841858-wp-16x9_2560x1440&lr=51&rpt=image"
        req = requests.get(url, headers = _headers)
  
        soup = BeautifulSoup(req.text, "html.parser")

        src_list = []
        
        try:
            for link in soup.find_all("img", class_ = "justifier__thumb"):
                src_list.append(link.get("src"))
            print("Картинки успешно сканированы")
        
        except Exception:
            print("Нет картинок")
        
        for img_url in src_list:
            if img_url.find("n=13") != -1:
                try:
                    print("Картинка", count)
                    source = "https:" + img_url
                    picture = requests.get(source)
                    
                    name_file = str(count)
                          
                    out = open(zebra_path + '/' + name_file.zfill(4) + '.jpg', 'wb') 
                    out.write(picture.content)
                    out.close()
                    
                    time.sleep(0.25)
                    
                    count += 1
                    if(count == count_imgs):
                        return
                    
                except Exception:
                    print("Error in: ", count)


def get_data_bay_horse(count_imgs: int) -> None:
    '''Парсит картинки с лошадьми'''
    if not os.path.exists(dataset_path):
        os.mkdir(dataset_path)   
    if not os.path.exists(bay_horse_path):
        os.mkdir(bay_horse_path)
        
    count = 0
    
    for i in range(0,999):
        
        letters = string.ascii_lowercase
        rand_string = ''.join(random.sample(letters, 10))
        _headers = {
            "user-agent":rand_string
        } 
        
        url = f"https://yandex.ru/images/search?p={i}&text=bay_horse&uinfo=sw-1920-sh-1080-ww-878-wh-924-pd-1-wp-16x9_1920x1080&lr=51&rpt=image"
        req = requests.get(url, headers = _headers)
  
        soup = BeautifulSoup(req.text, "html.parser")

        src_list = []
        
        try:
            
            for link in soup.find_all("img", class_ = "justifier__thumb"):
                src_list.append(link.get("src"))
            print("Картинки успешно сканированы")
        
        except Exception:
            print("Нет картинок")
         
        for img_url in src_list:
            if img_url.find("n=13") != -1:
                try:
                    print("Картинка", count)
                    source = "https:" + img_url
                    picture = requests.get(source)
                    
                    name_file = str(count)
                          
                    out = open(bay_horse_path + '/' + name_file.zfill(4) + '.jpg', 'wb') 
                    out.write(picture.content)
                    out.close()
                    
                    time.sleep(0.25)
                    
                    count += 1
                    if(count == count_imgs):
                        return
                    
                except Exception:
                    print("Error in: ", count)


def is_similar(image1: np.ndarray, image2: np.ndarray) -> bool:
    '''Проверяет две картинки на повторение'''
    return image1.shape == image2.shape and not(np.bitwise_xor(image1,image2).any())


def check_images(path: str, count: int) ->int:
    '''Проверяет датасет на повторяющиеся картинки'''
    c = count
    images = []
    for filename1 in os.listdir(path):
        images.append((cv2.imread(os.path.join(path, filename1)), os.path.join(path, filename1)))
    
    for im, fname in tqdm(images):
        for im2, fname2 in images:
            if(fname == fname2):
                continue
            if is_similar(im,im2):
                print(fname, fname2)
                os.remove(fname2)
                c -= 1
    return count-c


count_find = 1100

get_data_zebra(count_find)

get_data_bay_horse(count_find)

new_count=check_images(zebra_path,count_find)
get_data_bay_horse(new_count)
new_count=check_images(bay_horse_path,count_find)
get_data_zebra(new_count)

