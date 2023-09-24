import os
import logging
import serialisation_to_json as stj
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key

def generating_keys(settings: dict, pbar)->None:
    """
    Генерируются ключи и записываются в файл по указанному пути

    Args:
        settings (dict): пути к файлам
        pbar: информация о процессе выпонения
    """
    key = os.urandom(16)
    stj.serialisation_to_json(settings['symmetric_key'],key)
    print(key)
    keys = rsa.generate_privateKey(
    public_exponent=65537,
    key_size=2048)
    private_key = keys
    public_key = keys.public_key()
    pbar.update(1)
    pbar.set_description('writing asymmetric keys')

    try:
        with open(settings['public_key'], 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo))
    except FileNotFoundError:
        logging.error(f"{settings['public_key']} not found")

    pbar.set_description('writing private key') 

    try:
        with open(settings['private_key'], 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()))
    except FileNotFoundError:
        logging.error(f"{settings['private_key']} not found")

    sym_key = stj.deserialisation_from_json(settings['symmetric_key'])

    try:
        with open(settings['public_key'], 'rb') as pem_in:
            public_bytes = pem_in.read()
    except FileNotFoundError:
        logging.error(f"{settings['public_key']} not found")
    
    d_public_key = load_pem_public_key(public_bytes)
    c_sym_key = d_public_key.encrypt(sym_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
    pbar.set_description('saving symmetric key') 
    stj.serialisation_to_json(settings['encrypred_symmetric_key'], c_sym_key)
    pbar.update(1)