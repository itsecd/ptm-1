import glob
import os
import subprocess
import sys
import time
import requests
from pathlib import Path
from shutil import copyfile
from mutagen.flac import FLAC, Picture


class ZvukDown:
    def __init__(self):
        self.verify = True
        self.headers = {}
        pass

    def read_token(self) -> None:
        """
        Считывает токен из файла и записывает в headers для дальнейшего
        использования
        """
        with open("token.txt", "r", encoding="utf8") as file:
            token = file.read()
            if len(token) != 32:
                raise Exception("Wrong token length")
            self.headers = {"x-auth-token": token}

    def save_token(self, login: str, password: str) -> None:
        """
        Отправляет запрос сервису от имени пользователя, вычленяет
        из ответа токен, сохраняет его в token.txt и записывает в
        headers для дальнейшего использования

        :param login: логин
        :param password: пароль
        """
        url = "https://zvuk.com/api/tiny/login/email"
        params = {
            "register": "true"
        }
        data = {
            "email": login,
            "password": password,
        }
        resp = requests.post(url, params=params, data=data,
                             verify=self.verify)
        resp.raise_for_status()
        enc_resp = resp.json(strict=False)
        if "result" in enc_resp:
            if "token" in enc_resp["result"]:
                with open("token.txt", "w", encoding="utf8") as file:
                    token = enc_resp["result"]["token"]
                    file.write(token)
                    if len(token) != 32:
                        raise Exception("Wrong token length")
                    self.headers = {"x-auth-token": token}

    @staticmethod
    def __ntfs(filename):
        """
        Редактирует имя создаваемых файлов в случае их несоответствия
        шаблону

        :param filename: старое имя файла
        :return: новое имя файла
        """
        for ch in ["<", ">", "@", "%", "!", "+", ":", '"', "/", "\\", "|",
                   "?", "*"]:
            if ch in filename:
                filename = filename.replace(ch, " ")
        filename = " ".join(filename.split())
        filename = filename.replace(" .flac", ".flac")
        return filename

    @staticmethod
    def __launch(args: str) -> str:
        """
        Запускает стороннюю пргорамму, компрессирующую обложку
        релиза

        :param args: путь к файлу с обложкой
        """
        try:
            pipe = subprocess.Popen(args, creationflags=0x08000000, stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            output, err = pipe.communicate()
            pipe.wait()
            if pipe.returncode != 0:
                print(args + "\n")
                print(output + "\n")
                print(err)
                raise Exception("Unable to launch")
            return output
        except FileNotFoundError:
            return "Install pingo and imagemagick!"

    @staticmethod
    def __to_str(data: set) -> str:
        """
        Преобразует изначальное множество данных в строку

        :param data: множество данных
        :return: строка с данными
        """
        if isinstance(data, int):
            return str(data)
        if not isinstance(data, str):
            data = [str(int) for int in data]
            data = ",".join(data)
            data = str(data.strip("[]"))
        return data

    def __get_copyright(self, label_ids: set) -> dict:
        """
        Отправляет запрос сервису от имени пользователя, в полученном
        ответе находит необходимые данные о правообладателе и выдает их
        в виде словаря

        :param label_ids: id правообладателей
        :return: словарь с наименованиями правообладателей
        """
        label_ids = self.__to_str(label_ids)
        url = f"https://zvuk.com/api/tiny/labels"
        params = {
            "ids": label_ids
        }
        resp = requests.get(url, params=params, verify=self.verify)
        resp.raise_for_status()
        enc_resp = resp.json(strict=False)
        info = {}
        for index in enc_resp["result"]["labels"].values():
            info[index["id"]] = index["title"]
        return info

    def __get_tracks_metadata(self, track_ids: set) -> dict:
        """
        Отправляет запрос сервису от имени пользователя, в полученном
        ответе находит необходимые метаданные трека и выдает их
        в виде словаря

        :param track_ids: id треков
        :return: словарь с метаданными треков
        """
        track_ids = self.__to_str(track_ids)
        params = {
            "ids": track_ids
        }
        url = "https://zvuk.com/api/tiny/tracks"
        resp = requests.get(url, params=params,
                            headers=self.headers, verify=self.verify)
        resp.raise_for_status()
        enc_resp = resp.json(strict=False)
        info = {}
        for index in enc_resp["result"]["tracks"].values():
            if index["has_flac"]:
                author = index["credits"]
                name = index["title"]
                album = index["release_title"]
                release_id = index["release_id"]
                track_id = index["id"]
                if index["genres"]:
                    genre = ", ".join(index["genres"])
                else:
                    genre = ""
                number = index["position"]
                image = index["image"]["src"].replace(r"&size={size}&ext=jpg", "")
                info[track_id] = {"author": author, "name": name,
                                  "album": album, "release_id": release_id,
                                  "track_id": track_id, "genre": genre,
                                  "number": number, "image": image}
            else:
                if index["highest_quality"] != "flac":
                    raise Exception(
                        "has_flac, but highest_quality is not flac,"
                        " token is invalid")
                raise Exception(f"Skipping track {index['title']}, no flac")
        return info

    def __get_tracks_link(self, track_ids: set) -> dict:
        """
        Отправляет запросы сервису от имени пользователя, в полученных
        ответых находит ссылки на flac версии треков и выдает их
        в виде словаря: id - ссылка

        :param track_ids: id треков
        :return: словарь ссылок на треки из релиза
        """
        links = {}
        index = 0
        for track in track_ids:
            url = "https://zvuk.com/api/tiny/track/stream"
            params = {
                "id": track,
                "quality": "flac"
            }
            resp = requests.get(url, params=params,
                                headers=self.headers, verify=self.verify)
            enc_resp = resp.json(strict=False)
            links[track] = enc_resp["result"]["stream"]
            if links[track] != 0:
                index += 1
                print(index, ": ", track, "- ", enc_resp["result"]["stream"])
            time.sleep(3)
        return links

    def __get_releases_info(self, release_ids: set) -> dict:
        """
        Отправляет запрос сервису от имени пользователя, в полученном
        ответе находит необходимые метаданные релиза и выдает их
        в виде словаря

        :param release_ids: id релизов
        :return: словарь метаданных релиза
        """
        release_ids = self.__to_str(release_ids)
        info = {}
        url = "https://zvuk.com/api/tiny/releases"
        params = {
            "ids": release_ids
        }
        resp = requests.get(url, params=params,
                         headers=self.headers, verify=self.verify)
        resp.raise_for_status()
        enc_resp = resp.json(strict=False)
        labels = set()
        for index in enc_resp["result"]["releases"].values():
            labels.add(index["label_id"])
        labels_info = self.__get_copyright(labels)
        for index in enc_resp["result"]["releases"].values():
            info[index["id"]] = {"track_ids": index["track_ids"],
                             "tracktotal": len(index["track_ids"]),
                             "copyright": labels_info[index["label_id"]],
                             "date": index["date"], "album": index["title"],
                             "author": index["credits"]}
        return info

    def __download_image(self, release_id: str, image_link: str) -> dict:
        """
        Отправляет запрос сервису от имени пользователя, из ответа
        выгружает изображение (обложку релиза), анализирует его размер
        и компресирует при необходимости, возвращая пути дву версий
        изображдения в виде словаря

        :param release_id: id релизов
        :param image_link: ссылка на обложку релиза
        :return: словарь с путями к 2 версиям обложки
        """
        pic = Path(f"temp_{release_id}.jpg")
        comp_pic = Path(f"temp_{release_id}_comp.jpg")
        if not pic.is_file():
            resp = requests.get(image_link, allow_redirects=True,
                                verify=self.verify)
            open(pic, "wb").write(resp.content)
            print(self.__launch(f"pingo -sa -notime -strip {pic}"))
            if os.path.getsize(pic) > 2 * 1000 * 1000:
                print(self.__launch(f"magick convert {pic} "
                                    f"-define jpeg:extent=1MB {comp_pic}"))
                print(self.__launch(f"pingo -sa -notime -strip {comp_pic}"))
            else:
                copyfile(pic, comp_pic)
        return {"original": pic, "compressed": comp_pic}

    def __save_track(self, url: str, metadata, releases, single) -> None:
        """
        Скачивает трек, записывая в его метаданные ранее полученную
        информацию о релизе и о треке

        :param url: ссылка на трек
        :param metadata: метаданные трека
        :param releases: метаданные релиза
        :param single: сингл/не сингл
        """
        pic = self.__download_image(metadata["release_id"], metadata["image"])
        if not single and releases["tracktotal"] != 1:
            folder = f"{releases['author']} - {releases['album']}" \
                     f" ({str(releases['date'])[0:4]})"
            folder = self.__ntfs(folder)
            if not os.path.exists(folder):
                os.makedirs(folder)
                copyfile(pic["original"], os.path.join(folder, "cover.jpg"))
            pic = pic["compressed"]
            filename = f"{metadata['number']:02d} - {metadata['name']}.flac"
        else:
            pic = pic["original"]
            folder = ""
            filename = f"{metadata['author']} - {metadata['name']}.flac"
        filename = self.__ntfs(filename)
        filename = os.path.join(folder, filename)
        resp = requests.get(url, allow_redirects=True, verify=self.verify)
        open(filename, "wb").write(resp.content)
        audio = FLAC(filename)
        audio["ARTIST"] = metadata["author"]
        audio["TITLE"] = metadata["name"]
        audio["ALBUM"] = metadata["album"]
        audio["TRACKNUMBER"] = str(metadata["number"])
        audio["TRACKTOTAL"] = str(releases["tracktotal"])
        audio["GENRE"] = metadata["genre"]
        audio["COPYRIGHT"] = releases["copyright"]
        audio["DATE"] = str(releases["date"])
        audio["YEAR"] = str(releases["date"])[0:4]
        audio["RELEASE_ID"] = str(metadata["release_id"])
        audio["TRACK_ID"] = str(metadata["track_id"])
        cover_art = Picture()
        cover_art.data = open(pic, "rb").read()
        cover_art.type = 3
        cover_art.mime = "image/jpeg"
        audio.add_picture(cover_art)
        print(audio.pprint() + "\n")
        audio.save()
        time.sleep(1)

    def download_tracks(self, track_ids: set, single: bool = False, releases: dict = "") -> None:
        """
        Формирует словари мета метаданных треков и ссылок на них,
        после чего поочередно скачивает треки

        :param track_ids: id треков
        :param single: флаг сингловости
        :param releases: метаданные релиза
        """
        metadata = self.__get_tracks_metadata(track_ids)
        link = self.__get_tracks_link(track_ids)
        if len(metadata) != len(link):
            raise Exception("metadata != link")
        if not releases:
            release_ids = set()
            for index in metadata.values():
                release_ids.add(index["release_id"])
            releases = self.__get_releases_info(release_ids)
        for key in metadata.keys():
            self.__save_track(link[key], metadata[key],
                              releases[metadata[key]["release_id"]], single)

    def download_albums(self, release_ids: set) -> None:
        """
        Формирует множество id треков, содержащихся в заданных релизах
        и скачивает их

        :param release_ids: id альбомов
        """
        track_ids = set()
        releases = self.__get_releases_info(release_ids)
        for index in releases.values():
            track_ids.add(index["track_ids"])
        self.download_tracks(track_ids, releases=releases)


if __name__ == "__main__":
    release_list = set()
    track_list = set()
    obj = ZvukDown()
    if "login" in sys.argv:
        obj.save_token(sys.argv[2], sys.argv[3])
        print("Token saved!")
    else:
        if "debug" in sys.argv:
            obj.verify = False
        for i in sys.argv:
            if "release" in i:
                release_list.add(int(i.strip("https://sber-zvuk.com/release/")))
            elif "track" in i:
                track_list.add(int(i.strip("https://sber-zvuk.com/track/")))
        obj.read_token()
        if release_list:
            obj.download_albums(release_list)
        if track_list:
            obj.download_tracks(track_list, True)
        list(map(os.remove, glob.glob("temp*.jpg")))
