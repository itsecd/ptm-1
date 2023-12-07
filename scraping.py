import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import cv2
import shutil
import math


def scraping(url:str,count:int):
    if not os.path.isdir("temp"):
        os.mkdir("temp")
    if not os.path.isdir("temp/" + url):
        os.mkdir("temp/" + url)
    url_full="https://yandex.ru/images/search?text=" + url
    driver=webdriver.Chrome(executable_path="C:/Users/user/Desktop/1lab/chromedriver.exe")
    array=[]
    try:
        driver.get(url=url_full)
        time.sleep(5)
        for i in range(math.ceil(count/300)):
            for i in range(10):
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                time.sleep(5)
            button=driver.find_element("class name","more__button")
            time.sleep(5)
            button.click()
            time.sleep(2)
        html=driver.page_source
        time.sleep(5)
        soup=BeautifulSoup(html,"lxml")
        resp_0=soup.find("div",class_="serp-list")
        index=0
        for i in range(count):
            str_0=str(i)
            str_1="serp-item_pos_" + str_0
            resp_1=resp_0.find("div",class_=str_1)
            resp_2=resp_1.find("div",class_="serp-item__preview")
            resp_3=resp_2.find("a",class_="serp-item__link")
            url_img=resp_3.find("img",class_="serp-item__thumb justifier__thumb").get("src")
            if not url_img in array:
                array.append(url_img)  
                img=requests.get("https:" + array[i]).content
                a=str(index)
                ul="temp/" + url + "/" + a.zfill(4) +".jpg"
                with open(ul,"wb") as handler:
                    handler.write(img)
                index += 1
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    jpg(url,count)
    shutil.rmtree("temp")


def jpg(url:str,count:int):
    if not os.path.isdir("dataset"):
        os.mkdir("dataset")
    if not os.path.isdir("dataset/" + url):
        os.mkdir("dataset/" + url)
    for i in range(count):
        a=str(i)
        filename=str("temp/" + url + "/" + a.zfill(4) +".jpg")
        image=cv2.imread(filename)
        filewrite=str("dataset/" + url + "/" + a.zfill(4) +".jpg")
        cv2.imwrite(filewrite,image)

        
if __name__ =="__main__":
    scraping("dog",100)