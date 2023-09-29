"""

Module for encryption using various methods and the Encryptor class.
The module provides different encryption methods for securing data.
 It includes the Encryptor class, which allows for easy encryption and decryption using a chosen method.

"""


import datetime

import scorer
from scorer import IceCream


def Print_Sales_Forecasts():
    names = ["Steve", "Julie", "Francis"]
    now = datetime.datetime.now()
    print(f"Forecast at time {now}")
    for name in names:
        if name == "Steve":
            scorer.flavour = IceCream.Strawberry
        else:
            scorer.update_selection()
        score = scorer.get_sales_forecast()
        print(f"{name} score: {score}")


class Encryptor:
    def crypt_word(self, word) -> str:
        """Шифрование слова
            :arg:
            word (str) : слово
            :return:
            new_word (str) : зашифрованное слово
          """
        if " " not in word:
            new_word = ""
            for i in range(len(word)):
                char_value = ord(word[i])
                new_word += chr(char_value + 2)
            return new_word
        raise ValueError()

    def crypt_word_to_numbers(self, word) -> str:
        """Шифрование слова в числа
            :arg:
            word (str) : слово
            :return:
            new_word (str) : зашифрованное слово
        """
        if " " in word:
            raise ValueError()
        new_word = ""
        for i in range(len(word)):
            char_value = ord(word[i])
            new_word += str(char_value + 2)
        return new_word

    def crypt_word_with_chars_to_replace(self, word, chars_to_replace) -> str:
        """ Шифрование слова с заменой символов
            :arg:
            word (str) : слово
            chars_to_replace (list) : список символов для замены
            :return:
            new_word (str) : зашифрованное слово
        """
        if " " in word:
            raise ValueError()
        result = list(word)
        for i in range(len(word)):
            for j in range(len(chars_to_replace)):
                if chars_to_replace[j] == word[i]:
                    char_value = ord(word[i])
                    result[i] = chr(char_value + 2)
        return "".join(result)

    def crypt_sentence(self, sentence) -> str:
        """ Шифрование предложения
            :arg:
            sentence (str) : предложение
            :return:
            new_word (str) : зашифрованное предложение
        """
        new_word = ""
        for i in range(len(sentence)):
            char_value = ord(sentence[i])
            new_word += chr(char_value + 2)
        return new_word

    def get_words(self, sentence) -> list:
        """ Получение списка слов из предложения
            :arg:
            sentence (str) : предложение
            :return:
            words (list) : список слов
        """
        return sentence.split()

    def print_words(self, sentence) -> None:
        """ Вывод слов из предложения
            :arg:
            sentence (str) : предложение
        """
        words = self.get_words(sentence)
        for word in words:
            print(word)
