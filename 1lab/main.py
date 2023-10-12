import os
import time
from bs4 import BeautifulSoup
import cv2
import requests
from selenium import webdriver


def parse_photo(label="tiger") -> None:
    """Function parses and saves photos

    Args:
        label (str): name photo
    """
    if not os.path.isdir("dataset"):
        os.mkdir("dataset")
    if not os.path.isdir("dataset/" + label):
        os.mkdir("dataset/" + label)
    url = "https://yandex.ru/images/search?text=" + label
    driver = webdriver.Firefox()
    data = []
    try:
        driver.get(url)
        time.sleep(5)
        for i in range(2):
            for j in range(10):
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                time.sleep(2)
            button = driver.find_element(by="xpath", value="/html/body/div[4]/div[2]/div/div[2]/a")
            time.sleep(5)
            button.click()
            time.sleep(5)
        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")
        resp_0 = soup.find("div", class_="serp-list")
        for i in range(20):
            tag = "serp-item_pos_" + str(i)
            resp_1 = resp_0.find("div", class_=tag)
            resp_2 = resp_1.find("div", class_="serp-item__preview")
            resp_3 = resp_2.find("a")
            url_img = resp_3.find("img").get("src")
            if not url_img in data:
                data.append(url_img)
                image = requests.get("https:" + data[i]).content
                path_to_image = "dataset/" + label + "/" + str(i).zfill(4) + ".jpg"
                with open(path_to_image, "wb") as handler:
                    handler.write(image)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def create_jpg_format(label="tiger", count_photo=20) -> None:
    """Function resaves the image as jpg
    
    Args:
        label (str): name folder
    """
    if not os.path.isdir("dataset1"):
        os.mkdir("dataset1")
    if not os.path.isdir("dataset1/" + label):
        os.mkdir("dataset1/" + label)
    for i in range(count_photo):
        filename = str("dataset/" + label + "/" + str(i).zfill(4) + ".jpg")
        image = cv2.imread(filename)
        filewrite = str("dataset1/" + label + "/" + str(i).zfill(4) + ".jpg")
        cv2.imwrite(filewrite, image)


if __name__ == "__main__":
    parse_photo()
    create_jpg_format()