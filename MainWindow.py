import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from task1 import create_csv_annotation
from task2 import create_copy_dataset
from task3 import create_randomname_file
from task5 import IteratorTask1


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        """This function was created automatically by qtdesigner.
        Fields are being initialized here"""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #22222e")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 480, 270))
        self.frame.setStyleSheet("background-color: rgb(251, 91, 93);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(110, 60, 251, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(
            r"C:\Users\Leon\OneDrive\Рабочий стол\img\cat.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.PathToDataset = QtWidgets.QLineEdit(self.centralwidget)
        self.PathToDataset.setGeometry(QtCore.QRect(60, 280, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PathToDataset.setFont(font)
        self.PathToDataset.setStyleSheet("background-color: #22222e;\n"
                                         "border: 2px solid #f66867;\n"
                                         "border-radius: 30px;\n"
                                         "color: white;")
        self.PathToDataset.setAlignment(QtCore.Qt.AlignCenter)
        self.PathToDataset.setObjectName("PathToDataset")
        self.NextRose = QtWidgets.QPushButton(self.centralwidget)
        self.NextRose.setGeometry(QtCore.QRect(30, 360, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.NextRose.setFont(font)
        self.NextRose.setStyleSheet("QPushButton{\n"
                                    "color:white;\n"
                                    "background-color: #fb5b5d;\n"
                                    "border-radius: 10;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed{\n"
                                    "    background-color:#fa4244;\n"
                                    "}\n"
                                    "")
        self.NextRose.setObjectName("NextRose")
        self.NextTulip = QtWidgets.QPushButton(self.centralwidget)
        self.NextTulip.setGeometry(QtCore.QRect(280, 360, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.NextTulip.setFont(font)
        self.NextTulip.setStyleSheet("QPushButton{\n"
                                     "color:white;\n"
                                     "background-color: #fb5b5d;\n"
                                     "border-radius: 10;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed{\n"
                                     "    background-color:#fa4244;\n"
                                     "}\n"
                                     "")
        self.NextTulip.setObjectName("NextTulip")
        self.CreateAnnotation = QtWidgets.QPushButton(self.centralwidget)
        self.CreateAnnotation.setGeometry(QtCore.QRect(110, 420, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.CreateAnnotation.setFont(font)
        self.CreateAnnotation.setStyleSheet("QPushButton{\n"
                                            "color:white;\n"
                                            "background-color: #fb5b5d;\n"
                                            "border-radius: 10;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed{\n"
                                            "    background-color:#fa4244;\n"
                                            "}\n"
                                            "")
        self.CreateAnnotation.setObjectName("CreateAnnotation")
        self.PathToDirOfDataset = QtWidgets.QLineEdit(self.centralwidget)
        self.PathToDirOfDataset.setGeometry(QtCore.QRect(60, 480, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PathToDirOfDataset.setFont(font)
        self.PathToDirOfDataset.setStyleSheet("background-color: #22222e;\n"
                                              "border: 2px solid #f66867;\n"
                                              "border-radius: 30px;\n"
                                              "color: white;")
        self.PathToDirOfDataset.setAlignment(QtCore.Qt.AlignCenter)
        self.PathToDirOfDataset.setObjectName("PathToDirOfDataset")
        self.Task1 = QtWidgets.QPushButton(self.centralwidget)
        self.Task1.setGeometry(QtCore.QRect(30, 560, 121, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.Task1.setFont(font)
        self.Task1.setStyleSheet("QPushButton{\n"
                                 "color:white;\n"
                                 "background-color: #fb5b5d;\n"
                                 "border-radius: 10;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed{\n"
                                 "    background-color:#fa4244;\n"
                                 "}\n"
                                 "")
        self.Task1.setObjectName("Task1")
        self.Task2 = QtWidgets.QPushButton(self.centralwidget)
        self.Task2.setGeometry(QtCore.QRect(180, 560, 131, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.Task2.setFont(font)
        self.Task2.setStyleSheet("QPushButton{\n"
                                 "color:white;\n"
                                 "background-color: #fb5b5d;\n"
                                 "border-radius: 10;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed{\n"
                                 "    background-color:#fa4244;\n"
                                 "}\n"
                                 "")
        self.Task2.setObjectName("Task2")
        self.Task3 = QtWidgets.QPushButton(self.centralwidget)
        self.Task3.setGeometry(QtCore.QRect(330, 560, 131, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.Task3.setFont(font)
        self.Task3.setStyleSheet("QPushButton{\n"
                                 "color:white;\n"
                                 "background-color: #fb5b5d;\n"
                                 "border-radius: 10;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed{\n"
                                 "    background-color:#fa4244;\n"
                                 "}\n"
                                 "")
        self.Task3.setObjectName("Task3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.__iterator_rose = IteratorTask1()
        self.__iterator_tulip = IteratorTask1()
        self.add_functions()

    def retranslateUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        """This function gives names to elements of buttons, labels etc,
        which was created in setupUI function"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "DATASET Creator"))
        self.PathToDataset.setText(_translate(
            "MainWindow", "Path to  dataset"))
        self.NextRose.setText(_translate("MainWindow", "Next rose"))
        self.NextTulip.setText(_translate("MainWindow", "Next tulip"))
        self.CreateAnnotation.setText(
            _translate("MainWindow", "Create annotation"))
        self.PathToDirOfDataset.setText(_translate(
            "MainWindow", "Path to dir of dataset"))
        self.Task1.setText(_translate("MainWindow", "Task1"))
        self.Task2.setText(_translate("MainWindow", "Task2"))
        self.Task3.setText(_translate("MainWindow", "Task3"))

    def add_functions(self) -> None:
        """This function adds an event handler."""
        self.CreateAnnotation.clicked.connect(self.create_annotation)
        self.NextRose.clicked.connect(self.next_rose)
        self.NextTulip.clicked.connect(self.next_tulip)
        self.Task1.clicked.connect(self.task1_exec)
        self.Task2.clicked.connect(self.task2_exec)
        self.Task3.clicked.connect(self.task3_exec)

    def next_rose(self) -> None:
        """This function is Iterator.
        It displays the next image of rose on the screen untill the end.
        After that it begins with start."""
        if self.__iterator_rose.path == "":
            path = self.PathToDataset.text()
            if os.path.isdir(path):
                self.__iterator_rose.path_init(os.path.join(path, "rose"))
                self.__iterator_rose.file_names_init()
                self.__iterator_rose.limit_init()
                self.label_2.setPixmap(QtGui.QPixmap(
                    self.__iterator_rose.__next__()))
            else:
                self.ErrorMessage()
        else:
            try:
                self.label_2.setPixmap(QtGui.QPixmap(
                    self.__iterator_rose.__next__()))
            except:
                self.ErrorMessage3()
                self.__iterator_rose.clear()

    def next_tulip(self) -> None:
        """This function is Iterator.
        It displays the next image of tulip on the screen untill the end.
        After that it begins with start."""
        if self.__iterator_tulip.path == "":
            path = self.PathToDataset.text()
            if os.path.isdir(path):
                self.__iterator_tulip.path_init(os.path.join(path, "rose"))
                self.__iterator_tulip.file_names_init()
                self.__iterator_tulip.limit_init()
                self.label_2.setPixmap(QtGui.QPixmap(
                    self.__iterator_tulip.__next__()))
            else:
                self.ErrorMessage()
        else:
            try:
                self.label_2.setPixmap(QtGui.QPixmap(
                    self.__iterator_tulip.__next__()))
            except:
                self.ErrorMessage3()
                self.__iterator_tulip.clear()

    def create_annotation(self) -> None:
        """This function creates csv file with abs path of class of dataset."""
        path_to_dataset = self.PathToDataset.text()
        if os.path.isdir(path_to_dataset):
            try:
                create_csv_annotation(
                    path_to_dataset.split("\\")[-1], "annotation.csv")
            except:
                self.ErrorMessage2()

        else:
            self.ErrorMessage()

    def ErrorMessage(self) -> None:
        """This function displays error message that dir does not exist."""
        error = QMessageBox()
        error.setWindowTitle("Error")
        error.setText(
            "Dir with that path does not exist.\nChange it and try again.")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()

    def ErrorMessage2(self) -> None:
        """This function displays error message that dir does not contain."""
        error = QMessageBox()
        error.setWindowTitle("Error")
        error.setText(
            "This dir doesn't contain dataset's objects.\nChange it and try again.")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()

    def ErrorMessage3(self) -> None:
        """This function displays error message that pictures are over."""
        error = QMessageBox()
        error.setWindowTitle("Error")
        error.setText("Pictures are over.\nThey will start anew.")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()

    def task1_exec(self) -> None:
        """This function execute task 1 form second lab."""
        path = self.PathToDirOfDataset.text()
        if os.path.isdir(path):
            try:
                create_csv_annotation(path.split(
                    "\\")[-1], "annotation_task1.csv")
            except:
                self.ErrorMessage2()
        else:
            self.ErrorMessage()

    def task2_exec(self) -> None:
        """This function execute task 2 form second lab."""
        path = self.PathToDirOfDataset.text()
        if os.path.isdir(path):
            try:
                create_copy_dataset(path.split(
                    "\\")[-1], "dataset_task2", "annotation_task2.csv")
            except:
                self.ErrorMessage2()
        else:
            self.ErrorMessage()

    def task3_exec(self) -> None:
        """This function execute task 3 form second lab."""
        path = self.PathToDirOfDataset.text()
        if os.path.isdir(path):
            try:
                create_randomname_file(
                    "annotation_task3.csv", "dataset_task3", path.split("\\")[-1])
            except:
                self.ErrorMessage2()
        else:
            self.ErrorMessage()


if __name__ == "__main__":
    print('start')
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
