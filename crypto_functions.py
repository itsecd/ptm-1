from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes
import os


def encrypt(text_bytes: bytes, key_bytes: bytes) -> bytes:
    """
    функция шифрует текст с помощью ключа
    :param text_bytes: текст
    :param key_bytes: ключ
    :return: зашифрованный текст
    """
    padder = padding.ANSIX923(128).padder()
    padded_text = padder.update(text_bytes) + padder.finalize()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key_bytes), mode=modes.CBC(iv))
    encryptor = cipher.encryptor()
    encrypted_text = iv + encryptor.update(padded_text) + encryptor.finalize()
    return encrypted_text


def decrypt(encrypted_text: bytes, key_bytes: bytes) -> bytes:
    """
    функция шифрует зашифрованный текст с помощью ключа
    :param encrypted_text: зашифрованный текст
    :param key_bytes: ключ
    :return: расшифрованный текст
    """
    encrypted_text, iv = encrypted_text[16:], encrypted_text[:16]
    cipher = Cipher(algorithms.AES(key_bytes), mode=modes.CBC(iv))
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(encrypted_text) + decryptor.finalize()
    unpadder = padding.ANSIX923(128).unpadder()
    text = unpadder.update(decrypted_text) + unpadder.finalize()
    return text


def caesar_cipher(alf: str, alf_cipher: str, text: str) -> str:
    """
    функция реализует шифра цезаря
    :param alf: текущий алфавит текста
    :param alf_cipher: желаемый алфавит
    :param text: текст
    :return: текст с изменённым алфавитом
    """
    encoded_text = ""
    text = text.lower()
    for symbol in text:
        flag = False
        for j in range(len(alf)):
            if symbol == alf[j]:
                encoded_text += alf_cipher[j]
                flag = True
        if not flag:
            encoded_text += symbol
    return encoded_text
