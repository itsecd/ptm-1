import cv2
import os
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

def scraping(url):
    if not os.path.isdir("dataset"):
        os.mkdir("dataset")
    if not os.path.isdir("dataset/" + url):
        os.mkdir("dataset/" + url)
    url_full="https://yandex.ru/images/search?text=" + url
    driver=webdriver.Chrome(executable_path='C:/Users/user/Desktop/1lab/chromedriver.exe')
    array=[]
    try:
        driver.get(url=url_full)
        time.sleep(5)
        for i in range(4):
            for i in range(10):
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                time.sleep(2)
            button=driver.find_element("class name","more__button")
            time.sleep(5)
            button.click()
            time.sleep(5)
        html=driver.page_source
        time.sleep(5)
        soup=BeautifulSoup(html,'lxml')
        resp_0=soup.find("div",class_="serp-list")
        index=0
        for i in range(1100):
            str_0=str(i)
            str_1='serp-item_pos_' + str_0
            resp_1=resp_0.find("div",class_=str_1)
            resp_2=resp_1.find("div",class_="serp-item__preview")
            resp_3=resp_2.find("a",class_="serp-item__link")
            url_img=resp_3.find("img",class_="serp-item__thumb justifier__thumb").get("src")
            if not url_img in array:
                array.append(url_img)  
                print(array[i])
                img=requests.get('https:' + array[i]).content
                print(index)
                a=str(index)
                ul='dataset/' + url + '/' + a.zfill(4) +'.jpg'
                with open(ul,'wb') as handler:
                    handler.write(img)
                index += 1
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def jpg(url):
    if not os.path.isdir("dataset1"):
        os.mkdir("dataset1")
    if not os.path.isdir("dataset1/" + url):
        os.mkdir("dataset1/" + url)
    for i in range(1100):
        a=str(i)
        filename=str('dataset/' + url + '/' + a.zfill(4) +'.jpg')
        image=cv2.imread(filename)
        filewrite=str('dataset1/' + url + '/' + a.zfill(4) +'.jpg')
        cv2.imwrite(filewrite,image)


scraping("tiger")
jpg("leopard")
jpg("tiger")

