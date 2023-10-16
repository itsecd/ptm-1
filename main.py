import os
import shutil
import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}
URL = "https://yandex.ru/images/"


def save_image(image_url: str, name: str, index: int) -> None:
    """
    Сохраняет изображение в рабочую директорию

    :param image_url: URL-ссылка на изображение
    :param name: название изображения
    :param index: числовой индекс изображения
    """
    response = requests.get(f"https:{image_url}")
    file = os.path.join(f"dataset/{name}/{index:04d}.jpg")
    with open(file, "wb") as img:
        img.write(response.content)


def check_dir() -> None:
    """
    Проверяет существование рабочей директории
    """
    try:
        if not os.path.isdir("dataset"):
            os.mkdir("dataset")
        else:
            shutil.rmtree("dataset")
            os.mkdir("dataset")
    except OSError as err:
        print(f"Error! {err}")


def parse_images(name: str) -> None:
    """
    Парсит изображения по заданным параметрам и обращается к функции
    сохранения изображения, в конце выводит список ссылок на сохраненные
    изображения

    :param name: название изображения
    """
    index = 1
    page = 0
    response = requests.get(f"{URL}search?p={page}&text={name}&lr=51&rpt=image",
                            HEADERS)
    html = BeautifulSoup(response.content, "html.parser")
    image_log = []
    images = html.findAll("img")
    try:
        os.mkdir(f"dataset/{name}")
    except PermissionError as err:
        print(f"Error! {err}")
    for img in images:
        image_url = img.get("src")
        image_log.append([image_url])
        if image_url != "":
            save_image(image_url, name, index)
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
