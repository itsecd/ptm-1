import os
import serialisation_to_json as stj
import logging
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding


def decrypting(settings, pbar):

    """
    Текст дешифруется и записывается в файл по заданному пути

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
    enc_sym_key = stj.deserialisation_from_json(settings['encrypred_symmetric_key'])
    sym_key = d_private_key.decrypt(enc_sym_key,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
    iv = stj.deserialisation_from_json(settings['initial_vector'])
    pbar.update(1)
    pbar.set_description('decrypting the text and saving it')
    cipher = Cipher(algorithms.SM4(sym_key), modes.CBC(iv))
    unpadder = sym_padding.PKCS7(128).unpadder()
    decryptor = cipher.decryptor()



    try:
        with open(settings['encrypted_file'], 'rb') as f, open(settings['decrypted_file'], 'wb') as f2:
            while chunk := f.read(128):
                decrypted_chunk = decryptor.update(chunk)
                f2.write(unpadder.update(decrypted_chunk))
            f2.write(unpadder.update(decryptor.finalize()))
            f2.write(unpadder.finalize())
    except FileNotFoundError:
        logging.error(f"{settings['encrypted_file']} not found") if os.path.isfile(settings['decrypted_file']) else logging.error(f"{settings['decrypted_file']} not found")



    pbar.update(1)