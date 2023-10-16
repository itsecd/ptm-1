import os
import shutil
import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}
URL = "https://yandex.ru/images/"


def save_image(image_url: str, name: str, i: int) -> None:
    """
    Сохраняет изображение в рабочую директорию

    :param image_url: URL-ссылка на изображение
    :param name: название изображения
    :param i: числовой индекс изображения
    """
    req = requests.get(f"https:{image_url}")
    file = os.path.join(f"dataset/{name}/{i:04d}.jpg")
    with open(file, "wb") as saver:
        saver.write(req.content)


def check_folder() -> None:
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
        print(f"Возникла ошибка!!{err}")


def get_images_url(name: str) -> None:
    """
    Парсит изображения по заданным параметрам и обращается к функции сохранения изображения

    :param name: название изображения
    """
    i = 1
    page = 0
    request = requests.get(f"{URL}search?p={page}&text={name}&lr=51&rpt=image", HEADERS)
    html = BeautifulSoup(request.content, "html.parser")
    data = []
    searcher = html.findAll("img")
    try:
        os.mkdir(f"dataset/{name}")
    except PermissionError:
        print("Unable to create a directory")
    for event in searcher:
        image_url = event.get("src")
        data.append([image_url])
        if image_url != "":
            save_image(image_url, name, i)
            i += 1
        if i > 999:
            break
        page += 1
    print("Images save: ")
    print(data)


if __name__ == "__main__":
    check_folder()
    get_images_url("rose")
    get_images_url("tulip")
