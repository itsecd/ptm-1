import os
import logging
import serialisation_to_json as s2j
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key




def GK(settings, pbar):

    y = os.urandom(16)
    s2j.serialisation_to_json(settings['symmetric_key'],y)
    print(y)
    ys = rsa.generate_privateKey(
    publicExponent=65537,
    key_size=2048
    )
    private_key = ys
    publicKey = ys.public_key()
    pbar.update(1)
    pbar.set_description('writing asymmetric keys')

    try:
        with open(settings['public_key'], 'wb') as public_out:
            public_out.write(publicKey.public_bytes(encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo))
    except FileNotFoundError:
        logging.error(f"{settings['public_key']} not found")

    pbar.set_description('writing private key') 

    try:
        with open(settings['private_key'], 'wb') as j213:
            j213.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()))
    except FileNotFoundError:
        logging.error(f"{settings['private_key']} not found")

    P = s2j.deserialisation_from_json(settings['symmetric_key'])

    try:
        with open(settings['public_key'], 'rb') as pem_in:
            public_bytes = pem_in.read()
    except FileNotFoundError:
        logging.error(f"{settings['public_key']} not found")





    PkY = load_pem_public_key(public_bytes)
    cSkey = PkY.encrypt(P, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
    pbar.set_description('saving symmetric key') 
    s2j.serialisation_to_json(settings['encrypred_symmetric_key'], cSkey)
    pbar.update(1)