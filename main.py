import os
import shutil
import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}
URL = "https://yandex.ru/images/"
DIR = "dataset"


def save_image(image_url: str, keyword: str, index: int) -> None:
    """
    Сохраняет изображение в рабочую директорию

    :param image_url: URL-ссылка на изображение
    :param keyword: название подкатолога для изображений
    (в соответствии с поисковым запросом)
    :param index: числовой индекс (название) изображения
    """
    response = requests.get(f"https:{image_url}")
    file = os.path.join(DIR, keyword, f"{index:04d}.jpg")
    with open(file, "wb") as img:
        img.write(response.content)


def check_dir() -> None:
    """
    Проверяет существование рабочей директории,
    если отсутствует - создает
    """
    try:
        if not os.path.isdir(DIR):
            os.mkdir(DIR)
        else:
            shutil.rmtree(DIR)
            os.mkdir(DIR)
    except OSError as err:
        print(f"Error! {err}")


def parse_images(keyword: str) -> None:
    """
    Парсит изображения по заданному поисковому запросу и обращается
    к функциисохранения изображения, в конце выводит список ссылок на
    сохраненные изображения

    :param keyword: поисковый запрос
    """
    index = 1
    page = 0
    response = requests.get(f"{URL}search?p={page}&text={keyword}&lr=51&rpt=image",
                            HEADERS)
    html = BeautifulSoup(response.content, "html.parser")
    image_log = []
    images = html.findAll("img")
    try:
        os.mkdir(os.path.join(DIR, keyword))
    except PermissionError as err:
        print(f"Error! {err}")
    for img in images:
        image_url = img.get("src")
        image_log.append([image_url])
        if image_url != "":
            save_image(image_url, keyword, index)
            index += 1
        if index > 999:
            break
        page += 1
    print("Saved images: ")
    print(image_log)


if __name__ == "__main__":
    check_dir()
    parse_images("rose")
    parse_images("tulip")
