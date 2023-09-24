import os
import serialisation_to_json
import logging
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding


 

def eg(settings, pbar):

    try:
        with open(settings['privatekey'], 'rb') as pemin:
            privatebytes = pemin.read()
    except FileNotFoundError:
        logging.error(f"{settings['privatekey']} not found")

    dk = load_pem_private_key(privatebytes, password=None,)
    enck = serialisation_to_json.deserialisation_from_json(settings['encrypredsymmetrickey'])
    symkey = dk.decrypt(enck,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
    pbar.update(1)
    pbar.set_description('encrypting and saving the text')
    iv = os.urandom(16)
    serialisation_to_json.serialisation_to_json(settings['initialvector'], iv)
    c = Cipher(algorithms.SM4(symkey), modes.CBC(iv))
    encryptor = c.encryptor()

    try:
        with open(settings['initial_file'], 'rb') as f:
            inn = f.read()
    except FileNotFoundError:
        logging.error(f"{settings['initial_file']} not found")

    p = sym_padding.PKCS7(128).padder()

    try:
        with open(settings['initial_file'], 'rb') as f, open(settings['encrypted_file'], 'wb') as f2:
            while chunk := f.read(128):
                Pad_dedCh = padder.update(chunk)
                encText = encryptor.update(Pad_dedCh)
                f2.write(encText)
            f2.write( encryptor.update(padder.finalize()))
            f2.write(encryptor.finalize())
    except FileNotFoundError:
        logging.error(f"{settings['initial_file']} not found") if os.path.isfile(settings['encrypted_file']) else logging.error(f"{settings['encrypted_file']} not found")

    pbar.update(1)