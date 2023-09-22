
import json
import logging
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

SETTINGS = {'initial_file': 'file\initial_file.txt', 'encrypted_file': 'file\encrypted_file.txt', 'decrypted_file': 'file\decrypted_file.txt',
            'symmetric_key': 'key\symmetric_key.txt', 'public_key': 'key\public\key.pem', 'secret_key': 'key\secret\key.pem'}


def generate_keyPair(private_key_path: str,  public_key_path: str, symmetric_key_path: str) -> None:
    """Эта функция генерирует пару ключей(ассиметричный и симметричный) гибридной системы, а после сохраняет их в файлы.

    Args:
        private_key_path (str): путь до секретного ключан
        public_key_path (str): путь до общедоступного ключа
        symmetric_key_path (str): путь до симметричного ключа
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    with open(public_key_path, 'wb') as f_p, open(private_key_path, 'wb') as f_c:
        f_p.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                  format=serialization.PublicFormat.SubjectPublicKeyInfo))
        f_c.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                  format=serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm=serialization.NoEncryption()))
    symmetric_key = os.urandom(16)
    cipher_text = public_key.encrypt(symmetric_key, padding.OAEP(mgf=padding.MGF1(
        algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    with open(symmetric_key_path, "wb") as f:
        f.write(cipher_text)


def encrypt_data(initial_file_path: str, private_key_path: str, encrypted_symmetric_key_path: str, encrypted_file_path: str) -> None:
    """Эта функция шифрует данные используя симметричный и ассиметричные ключи, а так же сохраняет результат по указыному пути

    Args:
        initial_file_path (str): путь до шифруемых данных
        private_key_path (str): путь до приватного ключа
        encrypted_symmetric_key_path (str): путь до зашифрованного симметричного ключа
        encrypted_file_path (str): путь куда шифруются данных
    """
    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(), password=None)
    with open(encrypted_symmetric_key_path, "rb") as f:
        encrypted_symmetric_key = f.read()
    symmetric_key = private_key.decrypt(encrypted_symmetric_key, padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    iv = os.urandom(16)
    cipher = Cipher(algorithms.SM4(symmetric_key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    padder = sym_padding.PKCS7(128).padder()
    with open(initial_file_path, "rb") as f_in, open(encrypted_file_path, "wb") as f_out:
        f_out.write(iv)
        while chunk := f_in.read(128):
            padded_chunk = padder.update(chunk)
            f_out.write(encryptor.update(padded_chunk))

        f_out.write(encryptor.update(padder.finalize()))
        f_out.write(encryptor.finalize())


def decrypt_data(encrypted_file_path: str, private_key_path: str, encrypted_symmetric_key_path: str, decrypted_file_path: str) -> None:
    """эта функция дешифрует данные используя симметричный и ассиметричные ключи, а так же сохраняет результат по указыному пути

    Args:
        encrypted_file_path (str): путь до зашифрованных данных
        private_key_path (str): путь до секретного ключа
        encrypted_symmetric_key_path (str): путь до зашифрованного симметричного ключа
        decrypted_file_path (str): путь куда дешифруются данные
    """
    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(), password=None, backend=default_backend())
    with open(encrypted_symmetric_key_path, "rb") as f:
        encrypted_symmetric_key = f.read()
    symmetric_key = private_key.decrypt(encrypted_symmetric_key, padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    with open(encrypted_file_path, "rb") as f_in, open(decrypted_file_path, "wb") as f_out:
        iv = f_in.read(16)
        cipher = Cipher(algorithms.SM4(symmetric_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        unpadder = sym_padding.PKCS7(128).unpadder()
        with open(decrypted_file_path, "wb") as f_out:
            while chunk := f_in.read(128):
                decrypted_chunk = decryptor.update(chunk)
                f_out.write(unpadder.update(decrypted_chunk))

            f_out.write(unpadder.update(decryptor.finalize()))
            f_out.write(unpadder.finalize())


def main():
    while True:
        answ = input('Hello\nDo you have a set of instructions\n(Y)es\(N)o\n')
        if answ.lower() == 'Y':
            with open('settings.json') as json_file:
                json_data = json.load(json_file)
            settings = json_data
            break
        else:
            break
    while True:
        answ = input(
            'What do you want to do\nenter first letter\n(G)Key generation\n(E)Encrypt data\n(D)Decrypt data\nExit the program - 1\n')
        if answ.lower() == 'G':
            generate_keyPair(
                settings['secret_key'], settings['public_key'], settings['symmetric_key'])
            logging.info('The keys have been created\n')
        elif answ.lower() == 'E':
            encrypt_data(settings['initial_file'], settings['secret_key'],
                         settings['symmetric_key'], settings['encrypted_file'])
            logging.info('Data is encrypted\n')
        elif answ.lower() == 'D':
            decrypt_data(settings['encrypted_file'], settings['secret_key'],
                         settings['symmetric_key'], settings['decrypted_file'])
            logging.info('Data Decryped\n')
        else:
            logging.info('Program completed\n')
            break
    with open('settings.json', 'w') as fp:
        json.dump(settings, fp)


if __name__ == "__main__":
    main()
