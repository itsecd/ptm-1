import os
import sys
import shutil
import csv
import PyQt5.QtWidgets

from PyQt5.QtGui import QPixmap, QIcon
from random import randint


def get_csv(file: 'csv.writer', path: str) -> None:
    """
    Записывает в csv-файл названия всех изображений из директории path
    :param file: файл с расширением .csv
    :param path: путь до файла
    :return: None
    """
    for i in os.listdir(path):
        if i.find(".jpg") != -1:
            file.writerow({
             "Absolute path": f"{path}/{i}",
             "Relative path": f"{os.path.relpath(f'{path}/{i}', start='../..')}",
             "Class label": f"{os.path.basename(path)}"
            })


def create_csv(name: str) -> 'csv.writer':
    """
    Создает файл с расширением .csv с именем name, записывает в него заголовок
    :param name: имя csv-файла
    :return: csv-файл с записанным заголовком
    """
    file = open(f"{name}.csv", "a+")
    columns = ["Absolute path", "Relative path", "Class label"]
    created_csv = csv.DictWriter(file, lineterminator="\r", fieldnames=columns)
    created_csv.writeheader()
    return created_csv


def task1(filename: str, path: str) -> None:
    """
    Формирует csv-файл собранного датасета.
    :param filename: имя csv-файла
    :param path: путь до директории с изображениями
    :return: None
    """
    if os.path.isfile(f"{filename}.csv"):
        os.remove(f"{filename}.csv")
    file = create_csv(filename)
    get_csv(file, f"{path}/cat")
    get_csv(file, f"{path}/dog")


a = create_csv("annotation")
get_csv(a, "C:\\Users\\Professional\\PycharmProjects\\Lab_4-app_prog-Python\\dataset\\cat")
get_csv(a, "C:\\Users\\Professional\\PycharmProjects\\Lab_4-app_prog-Python\\dataset\\dog")


def dataset_copy(class_label: str, source: str, destination: str) -> None:
    """
    Копирует датасет в другую директорию.
    :param class_label: метка класса
    :param source: директория, из которой копируют файлы
    :param destination: директория, куда копируют файлы
    :return: None
    """
    source = f"{source}/{class_label}"
    for i in os.listdir(source):
        shutil.copy(f"{source}\\{i}", f"{destination}\\{class_label}_{i}")


def get_csv(destination: str) -> None:
    """
    Принимает путь к новой директории, записывает информацию по фото из этой директории в csv-файл.
    :param destination: путь к новой директории
    :return: None
    """
    os.chdir(destination)
    if os.path.isfile("annotation.csv"):
        os.remove("annotation.csv")
    csv_file = create_csv('annotation')
    for i in os.listdir(destination):
        if i.find(".jpg") != -1:
            class_label = (i.split("_"))[0]
            csv_file.writerow({
                "Absolute path": f"{os.path.abspath(i)}",
                "Relative path": f"{os.path.relpath(i, start='..')}",
                "Class label": class_label
            })


def task2(src: str, destination: str) -> None:
    """
    Копирует датасет в другую директорию таким образом, чтобы имена файлов содержали имя класса и его порядковый номер.
    :param src: директория, из которой копируют файлы
    :param destination: директория, куда копируют файлы
    :return: None
    """
    if os.path.isdir(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    dataset_copy("cat", src, destination)
    dataset_copy("dog", src, destination)
    get_csv(destination)


def create_csv(name: str) -> 'csv.writer':
    """
    Создает csv-файл и устанавливает значения столбцов.
    :param name: имя csv-файла
    :return: csv.writer
    """
    file = open(f"{name}.csv", "a+")
    columns = ["Absolute path", "Relative path", "Class label"]
    created_csv = csv.DictWriter(file, lineterminator="\r", fieldnames=columns)
    created_csv.writeheader()
    return created_csv


if __name__ == "__main__":
    dirname = "dataset-task2"
    if not os.path.isdir(dirname):
        os.mkdir(dirname)
    else:
        shutil.rmtree(dirname)
        os.mkdir(dirname)
    dest = os.path.abspath(dirname)
    dataset_copy("cat", f"{os.getcwd()}/dataset", dest)
    dataset_copy("dog", f"{os.getcwd()}/dataset", dest)
    get_csv(dest)


def dataset_random(class_label: str, source: str, destination: str, file: '_csv.writer') -> None:
    """
    Создает копию датасета таким образом, чтобы каждый файл из исходного датасета получил случайный номер от 0 до 10000,
    и датасет представлял собой следующую структуру: dataset/номер.jpg.
    :param class_label: метка класса
    :param source: директория, из которой копируют файлы
    :param destination: директория, куда копируют файлы
    :param file: имя csv-файла
    :return: None
    """
    source = f"{source}/{class_label}"
    for i in os.listdir(source):
        if i.find('.jpg') != -1:
            name = randint(0, 10001)
            while os.path.isfile(f"{destination}/{name}.jpg"):
                name = randint(0, 10001)
            shutil.copy(f"{source}/{i}", f"{destination}/{name}.jpg")
            file.writerow({
                "Absolute path": f"{os.path.abspath(f'{destination}/{name}.jpg')}",
                "Relative path": f"{os.path.relpath(f'{destination}/{name}.jpg', start='..')}",
                "Class label": class_label
            })


def task3(source: str, destination: str) -> None:
    """
    Объединяет два исходных датасета в один, представляющий собой следующую структуру:
    dataset/номер.jpg.
    :param source: директория, из которой копируют файлы
    :param destination: директория, куда копируют файлы
    :return: None
    """
    if os.path.isdir(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    current = os.getcwd()
    os.chdir(destination)
    if os.path.isfile('annotation.csv'):
        os.remove('annotation.csv')
    file = create_csv('annotation')
    os.chdir(current)
    dataset_random("cat", source, destination, file)
    dataset_random("dog", source, destination, file)


if __name__ == "__main__":
    dirname = "dataset-task3"
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
    os.mkdir(dirname)
    dest = os.path.abspath(dirname)
    if os.path.isfile(f"{dirname}/annotation.csv"):
        os.remove(f"{dirname}/annotation.csv")
    os.chdir(dest)
    csv_file = create_csv('annotation')
    os.chdir("..")
    dataset_random("cat", f"{os.getcwd()}/dataset", dest, csv_file)
    dataset_random("dog", f"{os.getcwd()}/dataset", dest, csv_file)


class Iterator:
    """
    Итератор для обхода элементов датасета
    """
    def __init__(self: Iterator, path: str) -> Iterator:
        self.counter = 0
        self.data = []
        for i in os.listdir(f"{path}/"):
            self.data.append(os.path.abspath(f"{path}/{i}"))
        self.limit = len(self.data)

    def __iter__(self: Iterator):
        return self

    def __next__(self: Iterator) -> str:
        if self.counter < self.limit:
            i = self.counter
            self.counter += 1
            return self.data[i]
        else:
            raise StopIteration

    def get_limit(self: Iterator):
        return self.limit


if __name__ == "__main__":
    os.chdir("dataset")
    iterator = Iterator(f"{os.getcwd()}/cat")
    for i in range(0, iterator.get_limit()):
        print(next(iterator))


class MyWindow(QMainWindow):
    """
    Приложение на PyQT5
    """
    def __init__(self: MyWindow) -> None:
        super().__init__()
        self.setWindowIcon(QIcon('icon.jpeg'))
        self.folder_path = QFileDialog.getExistingDirectory(self, 'Select dataset folder')
        while not os.path.isdir(f"{self.folder_path}/cat") or not os.path.isdir(f"{self.folder_path}/dog"):
            self.folder_path = QFileDialog.getExistingDirectory(self, 'Select dataset folder')
        self.cat_iterator = Iterator(f"{self.folder_path}/cat")
        self.dog_iterator = Iterator(f"{self.folder_path}/dog")
        self.button_next_cat = QPushButton('Следующая кошка', self)
        self.button_next_dog = QPushButton('Следующая собака', self)
        self.button_task_1 = QPushButton('csv-файл', self)
        self.button_task_2 = QPushButton('Задание 2', self)
        self.button_task_3 = QPushButton('Задание 3', self)
        self.open_file = QAction('Open', self)
        self.map_cat = QLabel(self)
        self.map_dog = QLabel(self)
        self.grid = QGridLayout(self)
        self.menubar = self.menuBar()
        self.file_menu = self.menubar.addMenu('&File')
        self.init_ui()

    def init_ui(self: MyWindow) -> None:
        self.setGeometry(360, 190, 1200, 700)
        self.setWindowTitle("Lab3")
        self.map_cat.setPixmap(QPixmap(next(self.cat_iterator)))
        self.map_cat.setScaledContents(True)
        self.map_cat.setGeometry(5, 5, 590, 490)
        self.grid.addWidget(self.map_cat)
        self.map_dog.setPixmap(QPixmap(next(self.dog_iterator)))
        self.map_dog.setScaledContents(True)
        self.map_dog.setGeometry(605, 5, 590, 490)
        self.grid.addWidget(self.map_dog)
        self.button_next_cat.setGeometry(225, 515, 140, 40)
        self.button_next_cat.setToolTip("Переход к следующему изображению кошки из датасета")
        self.button_next_cat.clicked.connect(self.next_cat)
        self.button_next_dog.setGeometry(835, 515, 140, 40)
        self.button_next_dog.setToolTip("Переход к следующему изображению собаки из датасета")
        self.button_next_dog.clicked.connect(self.next_dog)
        self.button_task_1.setGeometry(15, 620, 140, 40)
        self.button_task_1.setToolTip("Создание файла-аннотации для текущего датасета")
        self.button_task_1.clicked.connect(self.b_task1)
        self.button_task_2.setGeometry(170, 620, 140, 40)
        self.button_task_2.setToolTip("Создание датасета с организацией файлов, согласно заданию 2 варианта 3")
        self.button_task_2.clicked.connect(self.b_task2)
        self.button_task_3.setGeometry(325, 620, 140, 40)
        self.button_task_3.setToolTip("Создание датасета с организацией файлов, согласно заданию 3 варианта 3")
        self.button_task_3.clicked.connect(self.b_task3)
        self.open_file.setShortcut('Ctrl+O')
        self.open_file.setStatusTip('Open new File')
        self.open_file.triggered.connect(self.show_dialog)
        self.file_menu.addAction(self.open_file)
        self.show()

    def next_cat(self: MyWindow) -> None:
        self.map_cat.setPixmap(QPixmap(next(self.cat_iterator)))

    def next_dog(self: MyWindow) -> None:
        self.map_dog.setPixmap(QPixmap(next(self.dog_iterator)))

    def b_task1(self: MyWindow) -> None:
        filename = QFileDialog.getSaveFileName(self, "Напишите название файла", filter=".csv")
        task1(filename[0], self.folder_path)

    def b_task2(self: MyWindow) -> None:
        directory = QFileDialog.getExistingDirectory(self, "Выберите новую директорию")
        task2(self.folder_path, directory)

    def b_task3(self: MyWindow) -> None:
        directory = QFileDialog.getExistingDirectory(self, "Выберите новую директорию")
        task3(self.folder_path, directory)

    def show_dialog(self: MyWindow) -> None:
        self.folder_path = QFileDialog.getExistingDirectory(self, 'Open file')
        while not os.path.isdir(f"{self.folder_path}/cat") or not os.path.isdir(f"{self.folder_path}/dog"):
            self.folder_path = QFileDialog.getExistingDirectory(self, 'Select dataset folder')


class CustomImageDataset(Dataset):
    """
    Класс датасета
    """

    def __init__(self: CustomImageDataset, path_to_annotation_file: str, transform: Any = None,
                 target_transform: Any = None) -> None:
        self.path_to_annotation_file = path_to_annotation_file
        self.dataset_info = pd.read_csv(path_to_annotation_file, header=None)
        self.dataset_info.drop(self.dataset_info.columns[[0]], axis=1, inplace=True)
        self.dataset_info.drop(index=0, axis=0, inplace=True)
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self: CustomImageDataset) -> int:
        return len(self.dataset_info)

    def __getitem__(self: CustomImageDataset, index: int) -> Tuple[torch.tensor, int]:
        path_to_image = self.dataset_info.iloc[index, 0]
        image = cv2.cvtColor(cv2.imread(path_to_image), cv2.COLOR_BGR2RGB)
        label = self.dataset_info.iloc[index, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_Transform(label)
        return image, label


class CNN(nn.Module):
    """
    Свёрточная нейронная сеть
    """
    def __init__(self: CNN) -> None:
        super(CNN, self).__init__()
        self.conv_1 = nn.Conv2d(3, 16, kernel_size=3, padding=0, stride=2)
        self.conv_2 = nn.Conv2d(16, 32, kernel_size=3, padding=0, stride=2)
        self.conv_3 = nn.Conv2d(32, 64, kernel_size=3, padding=0, stride=2)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.1)
        self.max_pool = nn.MaxPool2d(2)
        self.fc_1 = nn.Linear(576, 10)
        self.fc_2 = nn.Linear(10, 1)

    def forward(self: CNN, x: torch.tensor) -> torch.tensor:
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
