import os
import serialisation_to_json as stj
import logging
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding

def encrypting(settings: dict, pbar)->None:
    """
    Текст шифруется симметричным шифрованием и зашифрованный текст записывается в файл по заданному пути

    Args:
        settings (dict): пути к файлам
        pbar: информация о процессе выпонения
    """
    try:
        with open(settings['private_key'], 'rb') as pem_in:
            private_bytes = pem_in.read()
    except FileNotFoundError:
        logging.error(f"{settings['private_key']} not found")

    d_private_key = load_pem_private_key(private_bytes, password=None,)
    enc_sym_key = serialisation_to_json.deserialisation_from_json(settings['encrypred_symmetric_key'])
    sym_key = d_private_key.decrypt(enc_sym_key,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
    pbar.update(1)
    pbar.set_description('encrypting and saving the text')
    iv = os.urandom(16)
    stj.serialisation_to_json(settings['initial_vector'], iv)
    cipher = Cipher(algorithms.SM4(sym_key), modes.CBC(iv))
    encryptor = cipher.encryptor()

    try:
        with open(settings['initial_file'], 'rb') as f:
            initial_text = f.read()
    except FileNotFoundError:
        logging.error(f"{settings['initial_file']} not found")

    padder = sym_padding.PKCS7(128).padder()

    try:
        with open(settings['initial_file'], 'rb') as f, open(settings['encrypted_file'], 'wb') as f2:
            while chunk := f.read(128):
                padded_chunk = padder.update(chunk)
                enc_text = encryptor.update(padded_chunk)
                f2.write(enc_text)
            f2.write( encryptor.update(padder.finalize()))
            f2.write(encryptor.finalize())
    except FileNotFoundError:
        logging.error(f"{settings['initial_file']} not found") if os.path.isfile(settings['encrypted_file']) else logging.error(f"{settings['encrypted_file']} not found")

    pbar.update(1)