import cv2
import pandas as pd
from typing import Any, Tuple
import torch
import torch.nn as nn
import torchvision
from torch.utils.data import Dataset


class CustomImageDataset(Dataset):
    def __init__(self, path_to_annotation_file: str, transform: Any=None, target_transform: Any=None) -> None:
        self.path_to_annotation_file = path_to_annotation_file
        self.dataset_info = pd.read_csv(path_to_annotation_file, sep=';', header=1)
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
    device = torch.device("cuda:0") if torch.cuda.is_available() else torch.device("cpu")
    model = CNN().to(device)
    custom_transforms = torchvision.transforms.Compose([torchvision.transforms.ToTensor(),
                                                        torchvision.transforms.Resize((224, 224)),
                                                        torchvision.transforms.Normalize(
                                                            (0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])
    train_dataset = CustomImageDataset('annotation.csv', custom_transforms)
    print('end')


if __name__ == "__main__":
    main()