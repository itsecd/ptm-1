import sys
import os

from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QTextEdit, QGridLayout, QApplication, QHBoxLayout,
                             QRadioButton, QFileDialog, qApp, QDesktopWidget, QMessageBox, QTabWidget, QVBoxLayout, QMainWindow)
from PyQt5.QtGui import QIcon, QPixmap, QFont


from task1 import Iterator1_img, create_csv
from task2 import copy_dataset
from task3 import create_dir_copy_randNames, create_dir_copy_randNames_both


class Example(QWidget):
    def __init__(self) -> None:
        '''Constructor'''
        super().__init__()
        self.__main_btn = QPushButton("Choose dataset dir", self)
        self.__main_btn.clicked.connect(self.__inputPath)
        self.__iterator = Iterator1_img("test", "dataset")
        self.__pixmap = QPixmap('.jpg')
        self.__lable = QLabel(self)
        self.__name = "test"
        self.__path = "dataset"
        self.initUI()

    def initUI(self) -> None:
        '''support constructor function'''
        self.setWindowTitle('Lab3')
        self.setWindowIcon(QIcon('6112_Logo_git_prefinal.jpg'))
        layout = QVBoxLayout()
        self.setLayout(layout)
        tabs = QTabWidget()
        tabs.addTab(self.__generalTab(), "general")
        tabs.addTab(self.__show_image_tab(), "show image")
        tabs.addTab(self.__tasks_tab(), "tasksTab")
        self.__iterator.set_path(self.__path)
        layout.addWidget(tabs)
        self.setGeometry(300, 300, 350, 300)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.show()

    def __generalTab(self) -> QWidget:
        '''main window with hello-words and descripition what's going on'''
        custom_font = QFont()
        custom_font.setPixelSize(40)
        general_tab = QWidget()
        layout = QVBoxLayout()
        text = QVBoxLayout()
        line1 = QLabel("Hello there!")
        line1.setFont(custom_font)
        custom_font.setPixelSize(15)
        line2 = QLabel("At showImageTab you can view dataset's imgs\nAt tasksTab You can:\n - task1: create CSV file for dataset's classes\n - task2: copy dataset to new directory\n - task3: copy dataset with new names")
        line2.setFont(custom_font)
        text.addWidget(line1)
        text.addWidget(line2)
        layout.addLayout(text)
        layout.addWidget(self.__main_btn)
        general_tab.setLayout(layout)
        return general_tab

    def __show_image_tab(self) -> QWidget:
        '''image tab where user choose directory and see the img via _next_'''
        general_tab = QWidget()
        layout = QVBoxLayout()
        layout_button = QHBoxLayout()
        clear_btn = QPushButton("clear")
        clear_btn.clicked.connect(self.__clear_button)
        next_btn = QPushButton("next")
        next_btn.clicked.connect(self.__next_button)
        layout_button.addWidget(clear_btn)
        layout_button.addWidget(next_btn)
        self.__lable.setPixmap(self.__pixmap)
        layout.addWidget(self.__lable)
        self.resize(self.__pixmap.width(), self.__pixmap.height())
        layout.addLayout(layout_button)
        general_tab.setLayout(layout)
        return general_tab

    def __tasks_tab(self) -> QWidget:
        '''function generates tab with all buttons of prev lab'''
        general_tab = QWidget()
        layout = QVBoxLayout()
        layout = QVBoxLayout()
        task1 = QPushButton('task1')
        task1.clicked.connect(self.__task1)
        layout.addWidget(task1)
        task2 = QPushButton('task2')
        task2.clicked.connect(self.__task2)
        layout.addWidget(task2)
        task3_single = QPushButton('task3Single')
        task3_single.clicked.connect(self.__task3Single)
        task3_both = QPushButton('task3Both')
        task3_both.clicked.connect(self.__task3Both)
        layout.addWidget(task3_single)
        layout.addWidget(task3_both)
        layout.addSpacing(100)
        layout_radio_button = QHBoxLayout()
        radio_button = QRadioButton("zebra")
        radio_button.name = "zebra"
        radio_button.toggled.connect(self.__on_clicked)
        layout_radio_button.addWidget(radio_button)
        radio_button = QRadioButton("bay horse")
        radio_button.name = "bay horse"
        radio_button.toggled.connect(self.__on_clicked)
        layout_radio_button.addWidget(radio_button)
        radio_button = QRadioButton("test")
        radio_button.name = "test"
        radio_button.setChecked(True)
        radio_button.toggled.connect(self.__on_clicked)
        layout_radio_button.addWidget(radio_button)
        layout.addLayout(layout_radio_button)
        general_tab.setLayout(layout)
        return general_tab

    def __on_clicked(self) -> None:
        '''change class name'''
        radio_button = self.sender()
        if radio_button.isChecked():
            print("Class is %s" % (radio_button.name))
            self.__iterator.set_name(radio_button.name)
            self.__name = radio_button.name

    def __inputPath(self) -> None:
        '''service function'''
        print("input path")
        tmp = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if not "dataset" in tmp:
            print("error")
            QMessageBox.critical(
                self, "Wrong dir", "please choose dir with dataset", QMessageBox.Ok)
        else:
            print("prev dir is ", self.__path)
            self.__path = tmp
            print("new dir is ", self.__path)

    def __clear_button(self) -> None:
        '''toggle clear and start iteration again'''
        print("clear")
        self.__pixmap = QPixmap(".jpg")
        self.__lable.setPixmap(self.__pixmap)
        self.__iterator.clear()
        self.resize(300, 300)

    def __next_button(self) -> None:
        '''toggle next and operate with exception'''
        try:
            tmp = os.path.join(os.path.join(self.__iterator.path,
                                            self.__iterator.name), self.__iterator.__next__())
            self.__pixmap = QPixmap(
                f"{tmp}")
            self.__lable.setPixmap(self.__pixmap)
            print(tmp)
        except:
            self.__pixmap = QPixmap('blueLobster.jpg')
            self.__lable.setPixmap(self.__pixmap)
            reply = QMessageBox.question(self, 'End of img_class',
                                         "empry, clear?", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                self.__iterator.clear()
            print("Error")

    def __task1(self) -> None:
        '''function for task1'''
        print("done task1!")
        create_csv(self.__name, self.__path)

    def __task2(self) -> None:
        '''function for task2'''
        print("done task2!")
        copy_dataset(self.__name, self.__path, QFileDialog.getExistingDirectory(
            self, 'Select Folder'))

    def __task3Single(self) -> None:
        '''function for task3 for single class'''
        print("done task3 single!")
        create_dir_copy_randNames(
            self.__name, self.__path, QFileDialog.getExistingDirectory(self, 'Select Folder'))

    def __task3Both(self) -> None:
        '''function for task3 for both classes'''
        print("done task3 both!")
        create_dir_copy_randNames_both(
            'zebra', 'bay horse', self.__path, QFileDialog.getExistingDirectory(self, 'Select Folder'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
