import time
import sys
from PIL.Image import Image
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from pandas import DataFrame


class Book:
    """
    Класс, представляющий книгу
    """
    def __init__(self, title: str, author: str, publication_year: int, isbn: str, genre: str, pages: int) -> None:
        """
        Создает новую книгу
        :param title:
        :param author:
        :param publication_year:
        :param isbn:
        :param genre:
        :param pages:
        """
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn
        self.genre = genre
        self.pages = pages

    def __str__(self) -> str:
        '''
        Возвращает строковое представление книги
        :return:
        '''
        return f"{self.title} by {self.author} ({self.publication_year})"

    def get_summary(self) -> str:
        '''
        Возвращает краткое описание книги
        :return:
        '''
        return f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.publication_year}"

class Library:
    """
    Класс, представляющий библиотеку
    """
    def __init__(self) -> None:
        """
        Создает новую библиотеку
        """
        self.books = []

    def add_book(self, book: Book) -> None:
        """
        Добавляет книгу в библиотеку
        :param book:
        :return:
        """
        self.books.append(book)

    def find_books_by_author(self, author: str) -> list:
        '''
        Возвращает список книг, написанных указанным автором
        :param author:
        :return:
        '''
        return [book for book in self.books if book.author == author]

    def find_books_published_after(self, year: int) -> list:
        '''
        Возвращает список книг, выпущенных после указанного года
        :param year:
        '''
        return [book for book in self.books if book.publication_year > year]

    def find_books_by_isbn(self, isbn: str) -> list:
        '''
        Возвращает список книг, по isbn
        :param isbn:
        '''
        return [book for book in self.books if book.isbn == isbn]

    def find_books_by_genre(self, genre: str) -> list:
        '''
        Возвращает список книг, по жанру
        :param genre:
        '''
        return [book for book in self.books if book.genre == genre]

    def find_books_by_pages(self, pages: str) -> list:
        '''
        Возвращает список книг, по страницам
        :param pages:
        '''
        return [book for book in self.books if book.pages == pages]

    def find_books_by_title(self, title: str):
        '''
        Возвращает список книг, выпущенных после указанного года
        :param title:
        '''
        return [book for book in self.books if book.title == title]

    def get_total_pages(self) -> int:
        """
        Возвращает общее количество страниц в библиотеке
        :return:
        """
        return sum([book.pages for book in self.books])

    def get_genres(self) -> list:
        """
        Возвращает список жанров
        :return:
        """
        return list(set([book.genre for book in self.books]))

class Universal_file_reading:
    """
    Класс, представляющий универсальное чтение файлов
    """
    def __init__(self, filename: str) -> None:
        """
        Создает новый файл
        :param filename:
        """
        self.filename = filename

    def read_file(self) -> str:
        """
        Чтение файла
        :return:
        """
        with open(self.filename, 'r') as file:
            return file.read()

    def read_lines(self) -> list:
        """
        Чтение файла построчно
        :return:
        """
        with open(self.filename, 'r') as file:
            return file.readlines()

    def read_json(self) -> dict:
        """
        Чтение JSON файла
        :return:
        """
        import json
        with open(self.filename, 'r') as file:
            return json.load(file)

    def read_csv(self) -> list:
        """
        Чтение CSV файла
        :return:
        """
        import csv
        with open(self.filename, 'r') as file:
            return csv.reader(file)

    def read_excel(self) -> DataFrame:
        """
        Чтение Excel файла
        :return:
        """
        import pandas as pd
        return pd.read_excel(self.filename)

    def read_sql(self) -> DataFrame:
        '''
        Чтение SQL файла
        :return:
        '''
        import sqlite3
        import pandas as pd
        with sqlite3.connect(self.filename) as connection:
            return pd.read_sql_query("SELECT * FROM table", connection)

    def read_xml(self) -> list:
        '''
        Чтение XML файла
        :return:
        '''
        import xml.etree.ElementTree as ET
        tree = ET.parse(self.filename)
        root = tree.getroot()
        return root

    def read_yaml(self) -> list:
        '''
        Чтение YAML файла
        :return:
        '''
        import yaml
        with open(self.filename, 'r') as file:
            return yaml.load(file, Loader=yaml.FullLoader)

    def read_pickle(self) -> list:
        """
        Чтение Pickle файла
        :return:
        """
        import pickle
        with open(self.filename, 'rb') as file:
            return pickle.load(file)

    def read_word(self) -> list:
        """
        Чтение Word файла
        :return:
        """
        import docx
        return docx.Document(self.filename)

    def read_image(self) -> Image:
        """
        Чтение изображения
        :return:
        """
        from PIL import Image
        return Image.open(self.filename)


def create_sample_library() -> Library:
    library = Library()
    book1 = Book(
        "THE BOOK 1",
        "John. T",
        1995,
        "8274827611",
        "Fiction",
        220)
    book2 = Book(
        "THE BOOK 2",
        "L.L. Horsev",
        "до н эры!!!",
        "9876543210",
        "Fiction",
        280)
    book3 = Book(
        "NOU NAME",
        "G.G. Irooskf",
        2020,
        "5432109876",
        "Dystopian",
        320)
    book4 = Book(
        "OKAY BOOK",
        "T.T. Orlov",
        2006,
        "5442449876",
        "Detective",
        250)
    book5 = Book(
        "TAYLER",
        "-",
        2010,
        "8787319875",
        "Detective",
        500)
    book6 = Book(
        "TAYLER2",
        "-",
        2014,
        "8799319875",
        "Detective",
        650)
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)
    library.add_book(book6)
    return library

def main() -> None:
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Библиотека 2.0')
    window.resize(600, 400)
    library = create_sample_library()
    layout = QVBoxLayout()
    author_label = QLabel("Books by John. T:")
    layout.addWidget(author_label)

    for book in library.find_books_by_author("John. T"):
        book_label = QLabel(
            str(book))
        layout.addWidget(book_label)

    year_label = (
        QLabel("Books published after 1950:"))
    layout.addWidget(year_label)
    for book in library.find_books_published_after(1950):
        book_label = QLabel(str(book))
        layout.addWidget(book_label)
    total_pages_label = QLabel(f"Total Pages in Library: {library.get_total_pages()}")
    layout.addWidget(total_pages_label)

    genres_label = QLabel(f"Genres in Library: {', '.join(library.get_genres())}")
    layout.addWidget(genres_label)

    for i in range(10):
        dummy_label = QLabel(f"Dummy Label {i}")
        layout.addWidget(dummy_label)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    time.sleep(1)
    main()
    time.sleep(1)
