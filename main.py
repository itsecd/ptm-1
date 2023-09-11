import time
import pandas as pd
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel


class Book:
    """
    Класс, представляющий книгу
    """
    def __init__(self, title, author, publication_year, isbn, genre, pages):
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

    def __str__(self):
        '''
        Возвращает строковое представление книги
        :return:
        '''
        return f"{self.title} by {self.author} ({self.publication_year})"

    def get_summary(self):
        '''
        Возвращает краткое описание книги
        :return:
        '''
        return f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.publication_year}"

class Library:
    """
    Класс, представляющий библиотеку
    """
    def __init__(self):
        """
        Создает новую библиотеку
        """
        self.books = []

    def add_book(self, book):
        """
        Добавляет книгу в библиотеку
        :param book:
        :return:
        """
        self.books.append(book)

    def find_books_by_author(self, author):
        '''
        Возвращает список книг, написанных указанным автором
        :param author:
        :return:
        '''
        return [book for book in self.books if book.author == author]

    def find_books_published_after(self, year):
        '''
        Возвращает список книг, выпущенных после указанного года
        '''
        return [book for book in self.books if book.publication_year > year]

    def get_total_pages(self):
        """
        Возвращает общее количество страниц в библиотеке
        :return:
        """
        return sum([book.pages for book in self.books])

    def get_genres(self):
        """
        Возвращает список жанров
        :return:
        """
        return list(set([book.genre for book in self.books]))


def CREAT3E_sample_():
    БИБЛИОТЕКА = Library()
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
    БИБЛИОТЕКА.add_book(book1)
    БИБЛИОТЕКА.add_book(book2)
    БИБЛИОТЕКА.add_book(book3)
    БИБЛИОТЕКА.add_book(book4)
    БИБЛИОТЕКА.add_book(book5)
    БИБЛИОТЕКА.add_book(book6)
    return БИБЛИОТЕКА

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Библиотека 2.0')
    window.resize(600, 400)
    БИБЛИОТЕКА = CREAT3E_sample_()
    layout = QVBoxLayout()
    author_label = QLabel("Books by John. T:")
    layout.addWidget(author_label)

    for book in БИБЛИОТЕКА.find_books_by_author("John. T"):
        book_label = QLabel(
            str(book))
        layout.addWidget(book_label)

    year_label = (
        QLabel("Books published after 1950:"))
    layout.addWidget(year_label)
    for book in БИБЛИОТЕКА.find_books_published_after(1950):
        book_label = QLabel(str(book))
        layout.addWidget(book_label)
    total_pages_label = QLabel(f"Total Pages in Library: {БИБЛИОТЕКА.get_total_pages()}")
    layout.addWidget(total_pages_label)

    genres_label = QLabel(f"Genres in Library: {', '.join(БИБЛИОТЕКА.get_genres())}")
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
