
import json
import logging
import os
from typing import Any, Tuple

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from torch.utils.data import DataLoader, Dataset


def GenerateKeyPair(private_key_path: str,  public_key_path: str, symmetric_key_path: str) -> None:
    """Эта функция генерирует пару ключей(ассиметричный и симметричный) гибридной системы, а после сохроняет их в файлы.

    Args:
        private_key_path (str): путь до секретного ключа
        public_key_path (str): путь до общедоступного ключа
        symmetric_key_path (str): путь до симмитричного ключа
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    with open(public_key_path, 'wb') as f_p, open(private_key_path, 'wb') as f_c:
        f_p.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
        f_c.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                            format=serialization.PrivateFormat.TraditionalOpenSSL,
                                            encryption_algorithm=serialization.NoEncryption()))

    symmetric_key = os.urandom(16)
    ciphertext = public_key.encrypt(symmetric_key, padding.OAEP(mgf=padding.MGF1(
        algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    with open(symmetric_key_path, "wb") as f:
        f.write(ciphertext)


def EncryptData(initial_file_path: str, private_key_path: str, encrypted_symmetric_key_path: str, encrypted_file_path: str) -> None:
    """Эта функция шифрует данные используя симмитричный и ассиметричные ключи, а так же сохраняет результат по указыному пути

    Args:
        initial_file_path (str): путь до шифруемых данных
        private_key_path (str): путь до приватного ключа
        encrypted_symmetric_key_path (str): путь до зашифрованного симмитричного ключа
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
    cipher = Cipher(algorithms.SM4(symmetric_key), modes.CBC(
        iv))
    encryptor = cipher.encryptor()
    padder = sym_padding.PKCS7(128).padder()
    with open(initial_file_path, "rb") as f_in, open(encrypted_file_path, "wb") as f_out:
        f_out.write(iv)
        while chunk := f_in.read(128):
            padded_chunk = padder.update(chunk)
            f_out.write(encryptor.update(padded_chunk))

        f_out.write(encryptor.update(padder.finalize()))
        f_out.write(encryptor.finalize())


def DecryptData(encrypted_file_path: str, private_key_path: str, encrypted_symmetric_key_path: str, decrypted_file_path: str) -> None:
    """эта функция дешифрует данные используя симметричный и ассиметричные ключи, а так же сохраняет результат по указыному пути

    Args:
        encrypted_file_path (str): путь до зашифрованных данных
        private_key_path (str): путь до секретного ключа
        encrypted_symmetric_key_path (str): путь до зашифрованного симмитричного ключа
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
        cipher = Cipher(algorithms.SM4(symmetric_key),
                        modes.CBC(iv))
        decryptor = cipher.decryptor()
        unpadder = sym_padding.PKCS7(128).unpadder()
        with open(decrypted_file_path, "wb") as f_out:
            while chunk := f_in.read(128):
                decrypted_chunk = decryptor.update(chunk)
                f_out.write(unpadder.update(decrypted_chunk))

            f_out.write(unpadder.update(decryptor.finalize()))
            f_out.write(unpadder.finalize())


class CustomImageDataset(Dataset):
    def __init__(self, path_to_annotation_file: str, transform: Any = None, target_transform: Any = None) -> None:
        self.path_to_annotation_file = path_to_annotation_file
        self.dataset_info = pd.read_csv(path_to_annotation_file, delimiter=';')
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self) -> int:
        return len(self.dataset_info)

    def __getitem__(self, index: int) -> Tuple[torch.tensor, int]:
        path_to_image = self.dataset_info.iloc[index, 0]
        image = cv2.cvtColor(cv2.imread(path_to_image), cv2.COLOR_BGR2RGB)
        label = self.dataset_info.iloc[index, 1]

        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_Transform(label)

        return image, label


class CNN(nn.Module):
    def __init__(self) -> None:
        super(CNN, self).__init__()
        self.conv_1 = nn.Conv2d(3, 16, kernel_size=3, padding=0, stride=2)
        self.conv_2 = nn.Conv2d(16, 32, kernel_size=3, padding=0, stride=2)
        self.conv_3 = nn.Conv2d(32, 64, kernel_size=3, padding=0, stride=2)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.1)
        self.max_pool = nn.MaxPool2d(2)
        self.fc_1 = nn.Linear(576, 10)
        self.fc_2 = nn.Linear(10, 1)

    def forward(self, x: torch.tensor) -> torch.tensor:
        output = self.relu(self.conv_1(x))
        output = self.max_pool(output)
        output = self.relu(self.conv_2(output))
        output = self.max_pool(output)
        output = self.relu(self.conv_3(output))
        output = self.max_pool(output)
        output = torch.nn.Flatten()(output)
        output = self.relu(self.fc_1(output))
        output = torch.nn.Sigmoid()(self.fc_2(output))
        return output


def main():
    device = torch.device(
        "cuda:0") if torch.cuda.is_available() else torch.device("cpu")
    model = CNN().to(device)
    torch.cuda.is_available()
    custom_transforms = torchvision.transforms.Compose([torchvision.transforms.ToTensor(),
                                                        torchvision.transforms.Resize(
                                                            (224, 224)),
                                                        torchvision.transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])
    train_dataset = CustomImageDataset(
        'annotation_train.csv', custom_transforms)
    test_dataset = CustomImageDataset('annotation_test.csv', custom_transforms)
    val_dataset = CustomImageDataset('annotation_val.csv', custom_transforms)
    train_dataloader = DataLoader(train_dataset, batch_size=4, shuffle=True)
    test_dataloader = DataLoader(test_dataset, batch_size=4, shuffle=False)
    val_dataloader = DataLoader(val_dataset, batch_size=4, shuffle=False)
    optimizer = optim.Adam(params=model.parameters(), lr=0.001)
    criterion = nn.BCELoss()
    epochs = 9
    accuracy_values = []
    loss_values = []
    accuracy_val_values = []
    loss_val_values = []
    for epoch in range(epochs):
        model.train()
        epoch_loss = 0
        epoch_accuracy = 0
        epoch_val_accuracy = 0
        epoch_val_loss = 0
        for data, label in train_dataloader:
            data = data.to(device)
            label = label.to(device)
            output = model(data)
            loss = criterion(output, label.unsqueeze(dim=1).to(torch.float))
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            acc = np.array(([1 if (1 if output[j][0].detach() >= 0.5 else 0) == int(
                label[j]) else 0 for j in range(label.shape[0])])).mean()
            epoch_accuracy += acc / len(train_dataloader)
            epoch_loss += loss / len(train_dataloader)
        accuracy_values.append(epoch_accuracy)
        loss_values.append(epoch_loss)
        print('Epoch : {}, train accuracy : {}, train loss : {}'.format(
            epoch + 1, epoch_accuracy, epoch_loss))
        model.eval()
        for data, label in val_dataloader:
            data = data.to(device)
            label = label.to(device)
            output = model(data)
            loss_val = criterion(
                output, label.unsqueeze(dim=1).to(torch.float))
            acc_val = np.array(([1 if (1 if output[j][0].detach() >= 0.5 else 0) == int(
                label[j]) else 0 for j in range(label.shape[0])])).mean()
            epoch_val_accuracy += acc_val / len(val_dataloader)
            epoch_val_loss += loss_val / len(val_dataloader)
        accuracy_val_values.append(epoch_val_accuracy)
        loss_val_values.append(epoch_val_loss)
        print('Epoch : {}, val accuracy : {}, val loss : {}'.format(
            epoch + 1, epoch_val_accuracy, epoch_val_loss))
    plt.figure(1, figsize=(15, 5))
    plt.title('Train accuracy')
    plt.plot(range(len(accuracy_values)), accuracy_values, color="green")
    plt.legend(["Acchukarevacy"])
    plt.figure(2, figsize=(15, 5))
    plt.title('Train loss')
    plt.plot(range(len(accuracy_values)), [float(value.detach())
             for value in loss_values], color="blue")
    plt.legend(["Loss"])
    plt.figure(3, figsize=(15, 5))
    plt.title('valid accuracy')
    plt.plot(range(len(accuracy_val_values)),
             accuracy_val_values, color="green")
    plt.legend(["Accuracy"])
    plt.figure(4, figsize=(15, 5))
    plt.title('valid loss')
    plt.plot(range(len(accuracy_val_values)), [float(value.detach())
             for value in loss_val_values], color="blue")
    plt.legend(["Loss"])
    plt.show()
    model.eval()
    test_loss = 0
    test_accuracy = 0
    for data, label in test_dataloader:
        data = data.to(device)
        label = label.to(device)
        output = model(data)
        acc = np.array(([1 if (1 if output[j][0].detach() >= 0.5 else 0) == int(
            label[j]) else 0 for j in range(4)])).mean()
        test_accuracy += acc / len(test_dataloader)
        test_loss += float(loss.detach()) / len(test_dataloader)
    print('test_accuracy=', test_accuracy, ' ', 'test_loss=', test_loss)
    print('end')
    settings = {
        'initial_file': 'file\initial_file.txt',
        'encrypted_file': 'file\encrypted_file.txt',
        'decrypted_file': 'file\decrypted_file.txt',
        'symmetric_key': 'key\symmetric_key.txt',
        'public_key': 'key\public\key.pem',
        'secret_key': 'key\secret\key.pem'
    }
    while True:
        answ = input(
            'Hello\nDo you have a set of instructions\n(Y)es\(N)o\n')
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
            GenerateKeyPair(
                settings['secret_key'], settings['public_key'], settings['symmetric_key'])
            logging.info('The keys have been created\n')
        elif answ.lower() == 'E':
            EncryptData(settings['initial_file'], settings['secret_key'],
                         settings['symmetric_key'], settings['encrypted_file'])
            logging.info('Data is encrypted\n')
        elif answ.lower() == 'D':
            DecryptData(settings['encrypted_file'], settings['secret_key'],
                         settings['symmetric_key'], settings['decrypted_file'])
            logging.info('Data Decryped\n')
        else:
            logging.info('Program completed\n')
            break
    with open('settings.json', 'w') as fp:
        json.dump(settings, fp)


if __name__ == "__main__":
    main()
