import glob
import os
import random

import cv2
import matplotlib.pyplot as plt
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image
from sklearn.model_selection import train_test_split
from torchvision import transforms

from CNN import ConvNet

TRAIN_PATH = 'E:\dataset\\train'
TEST_PATH = 'E:\dataset\\test'
VAL_PATH = 'E:\dataset\\val'
LEARNING_RATE = 0.001
BATCH_SIZE = 10
EPOCHS = 10
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
MODEL = ConvNet().to(DEVICE)
MODEL.train()
OPTIMIZER = torch.optim.Adam(MODEL.parameters(), lr=LEARNING_RATE)


class dataset(torch.utils.data.Dataset):
    def __init__(self,file_list,transform=None):
        self.file_list = file_list
        self.transform = transform
        
    def __len__(self):
        self.filelength = len(self.file_list)
        return self.filelength
    
    def __getitem__(self,idx):
        img_path = self.file_list[idx]
        img = Image.open(img_path)
        img_transformed = self.transform(img)
        label = img_path.split('\\')[-1].split('.')[0]
        if label == 'polarbears':
            label = 1
        elif label == 'brownbears':
            label = 0
        return img_transformed,label


def create_df(file_path = 'dataset.csv'):
    '''
    Создаёт датафрейм из исходного файла.
    Аргументы:
        file_path: путь исходного файла
    Возвращаемое значение:
        df: полученный датафрейм
    '''

    df = pd.read_csv(file_path, sep = ' ')
    df = df.rename(columns={'Absolute_way': 'absolute_way'})
    df = df.rename(columns={'Class': 'class_img'})
    return df


def load_train(df: pd.core.frame.DataFrame, path: str, i: int) -> None:
    '''
    Загружает i-ую картинку из датафрейма по заданному пути path.
    Ключевые аргументы:
        df(pd.core.frame.DataFrame): датафрейм с картинками 
        path(str): путь загрузки картинок
        i(int): номер картинки
    '''

    image_path = df.absolute_way[i]
    image = cv2.imread(image_path)
    cv2.imwrite(os.path.join(path, f'{df.class_img[i]}.{i}.jpg'), image)


def load_test(df: pd.core.frame.DataFrame, path: str, i: int) -> None:
    '''
    Загружает i-ую картинку из датафрейма по заданному пути path.
    Ключевые аргументы:
        df(pd.core.frame.DataFrame): датафрейм с картинками 
        path(str): путь загрузки картинок
        i(int): номер картинки
    '''

    image_path = df.absolute_way[i]
    image = cv2.imread(image_path)
    if i - 840 > 104: 
        i = i - 1785
    else:
        i = i -840
    cv2.imwrite(os.path.join(path, f'{i}.jpg'), image)


def data_preparation():
    '''
    Производит подготовку данных для обучения.
    Возвращаемое значение:
        train_loader, test_loader, val_loader: кортеж из подготовленных выборок
    '''

    torch.manual_seed(1234)
    if DEVICE =='cuda':
        torch.cuda.manual_seed_all(1234)
    train_list = glob.glob(os.path.join(TRAIN_PATH,'*.jpg'))
    test_list = glob.glob(os.path.join(TEST_PATH, '*.jpg'))
    train_list, val_list = train_test_split(train_list, test_size=0.1)
    train_transforms =  transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.RandomResizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
        ])
    val_transforms = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.RandomResizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
        ])
    test_transforms = transforms.Compose([   
        transforms.Resize((224, 224)),
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor()
        ])
    train_data = dataset(train_list, transform=train_transforms)
    test_data = dataset(test_list, transform=test_transforms)
    val_data = dataset(val_list, transform=val_transforms)
    train_loader = torch.utils.data.DataLoader(dataset = train_data, batch_size=BATCH_SIZE, shuffle=True )
    test_loader = torch.utils.data.DataLoader(dataset = test_data, batch_size=BATCH_SIZE, shuffle=True)
    val_loader = torch.utils.data.DataLoader(dataset = val_data, batch_size=BATCH_SIZE, shuffle=True)
    return train_loader, test_loader, val_loader


def train_loop (train_loader, val_loader, epochs):
    '''
    Цикл обучения модели.
    Аргументы:
        train_loader: обучаемая выборка
        val_loader: проверочная выборка
        epochs: количество эпох
    '''

    val_loss_list = []
    val_accuracy_list = []
    loss_list = []
    accuracy_list = []
    for epoch in range(epochs):
        epoch_loss = 0
        epoch_accuracy = 0
        for data, label in train_loader:
            data = data.to(DEVICE)
            label = label.to(DEVICE)
            output = MODEL(data)
            loss = nn.CrossEntropyLoss(output, label)
            OPTIMIZER.zero_grad()
            loss.backward()
            OPTIMIZER.step()
            acc = ((output.argmax(dim=1) == label).float().mean())
            epoch_accuracy += acc/len(train_loader)
            epoch_loss += loss/len(train_loader)
        loss_list.append(epoch_loss.item())
        accuracy_list.append(epoch_accuracy.item())
        print('Epoch : {}, train accuracy : {}, train loss : {}'.format(epoch+1, epoch_accuracy,epoch_loss))
        with torch.no_grad():
            epoch_val_accuracy=0
            epoch_val_loss =0
            for data, label in val_loader:
                data = data.to(DEVICE)
                label = label.to(DEVICE)
                val_output = MODEL(data)
                val_loss = nn.CrossEntropyLoss(val_output,label)
                acc = ((val_output.argmax(dim=1) == label).float().mean())
                epoch_val_accuracy += acc/ len(val_loader)
                epoch_val_loss += val_loss/ len(val_loader)
            val_loss_list.append(epoch_val_loss.item())
            val_accuracy_list.append(epoch_val_accuracy.item())
            print('Epoch : {}, val_accuracy : {}, val_loss : {}'.format(epoch+1, epoch_val_accuracy,epoch_val_loss))
    

def show_results(epochs, loss_list, accuracy_list, val_loss_list, val_accuracy_list):
    '''
    Выводит результаты обучения на графиках.
    Аргументы:
        epochs: количество эпох
        loss_list: данные ошибок
        accuracy_list: данные точности 
        val_lost_list: данные ошибок валидационной выборки
        val_accuracy_list:данные точности валидационной выборки
    '''

    num_epochs = [i+1 for i in range(epochs)]
    fig = plt.figure(figsize=(30, 5))
    plt.title('Plots for train')
    plt.xlabel('Epochs')
    plt.ylabel('Value')
    fig.add_subplot(1,2,1)
    plt.plot(num_epochs, loss_list, 'ro', label = 'loss')
    plt.legend(loc=2, prop={'size': 20}) 
    fig.add_subplot(1,2,2)
    plt.plot(num_epochs, accuracy_list, 'go', label = 'accuracy')
    plt.legend(loc=2, prop={'size': 20}) 
    fig = plt.figure(figsize=(30, 5))
    plt.title('Plots for valid')
    plt.xlabel('Epochs')
    plt.ylabel('Value')
    fig.add_subplot(1,2,1)
    plt.plot(num_epochs, val_loss_list, 'ro', label = 'loss')
    plt.legend(loc=2, prop={'size': 20}) 
    fig.add_subplot(1,2,2)
    plt.plot(num_epochs, val_accuracy_list, 'go', label = 'accuracy')
    plt.legend(loc=2, prop={'size': 20}) 


def show_work(test_loader):
    '''
    Демонстрирует работу на тестовой выборке и выводит результат.
    Аргументы:
        test_loader: тестовая выборка
    '''

    polarbears_probs = []
    MODEL.eval()
    with torch.no_grad():
        for images, labels in test_loader:
            images = images.to(DEVICE)
            preds = MODEL(images)
            preds_list = F.softmax(preds, dim=1)[:, 1].tolist()
            polarbears_probs += list(zip(labels, preds_list))
    polarbears_probs.sort(key = lambda x : int(x[0]))  
    idx = list(map(lambda x: x[0],polarbears_probs))
    prob = list(map(lambda x: x[1],polarbears_probs))
    submission = pd.DataFrame({'id':idx,'label':prob})
    class_ = {0: 'brownbear', 1: 'polarbear'}
    _, axes = plt.subplots(2, 5, figsize=(20, 12), facecolor='w')
    for ax in axes.ravel():   
        i = random.choice(submission['id'].values)
        label = submission.loc[submission['id'] == i, 'label'].values[0]
        if label > 0.5:
            label = 1
        else:
            label = 0    
        img_path = os.path.join(TEST_PATH, f'{i}.jpg')
        img = Image.open(img_path)
        ax.set_title(class_[label])
        ax.imshow(img)


def save_and_test(test_loader, path = 'ConvNetModel.pth'):
    '''
    Сохраняет обученную модель нейронной сети и демонстрирует работу на тестовой выборке.
    Аргументы: 
        test_loader: тестовая выборка данных
        path: путь сохранения модели нейронки 
    '''
    
    torch.save(MODEL.state_dict(), path)
    loaded_model = ConvNet().to(DEVICE)
    loaded_model.load_state_dict(torch.load(path))
    loaded_model.eval()
    brownbears_probs = []
    with torch.no_grad():
        for images, labels in test_loader:
            images = images.to(DEVICE)
            preds = loaded_model(images)
            preds_list = F.softmax(preds, dim=1)[:, 1].tolist()
            brownbears_probs += list(zip(labels, preds_list))          
    idx = list(map(lambda x: x[0],brownbears_probs))
    prob = list(map(lambda x: x[1],brownbears_probs))
    submission = pd.DataFrame({'id':idx,'label':prob})
    class_ = {0: 'brownbear', 1: 'polarbear'}
    _, axes = plt.subplots(2, 5, figsize=(20, 12), facecolor='w')
    for ax in axes.ravel():  
        i = random.choice(submission['id'].values)
        label = submission.loc[submission['id'] == i, 'label'].values[0]
        if label > 0.5:
            label = 1
        else:
            label = 0
        img_path = os.path.join(TEST_PATH, f'{i}.jpg')
        img = Image.open(img_path)
        ax.set_title(class_[label])
        ax.imshow(img)
