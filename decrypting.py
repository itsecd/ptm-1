import os
import serialisation_to_json
import logging
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding


def dg(settings, pbar):


    try:
        with open(settings['privatekey'], 'rb') as pemin:
            privatebytes = pemin.read()
    except FileNotFoundError:
        logging.error(f"{settings['privatekey']} not found")

    dprivatekey = load_pem_private_key(privatebytes, password=None,)
    encsymkey = serialisation_to_json.deserialisation_from_json(settings['encrypredsymmetrickey'])
    symkey = dprivatekey.decrypt(encsymkey,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
    iv = serialisation_to_json.deserialisation_from_json(settings['initialvector'])
    pbar.update(1)
    pbar.set_description('decrypting the text and saving it')
    cipher = Cipher(algorithms.SM4(symkey), modes.CBC(iv))
    unpadder = sym_padding.PKCS7(128).unpadder()
    decryptor = cipher.decryptor()



    try:
        with open(settings['encryptedfile'], 'rb') as f, open(settings['decryptedfile'], 'wb') as f2:
            while chunk := f.read(128):
                decryptedchunk = decryptor.update(chunk)
                f2.write(unpadder.update(decryptedchunk))
            f2.write(unpadder.update(decryptor.finalize()))
            f2.write(unpadder.finalize())
    except FileNotFoundError:
        logging.error(f"{settings['encryptedfile']} not found") if os.path.isfile(settings['decryptedfile']) else logging.error(f"{settings['decryptedfile']} not found")



    pbar.update(1)