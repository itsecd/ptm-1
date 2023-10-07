from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QLineEdit
from PyQt5.QtGui import QPixmap
import sys
import os
import copy_
import rand
import write_csv
import iter

class Interface(QMainWindow):
    def __init__(self):
        super(Interface, self).__init__()

        self.setWindowTitle("ROSE and TULIP")
        self.move(700, 200)
        self.resize(600, 300)

        self.w_text = QLineEdit(self)
        self.w_text.move(10, 20)
        self.w_text.adjustSize()
        
        self.text = QtWidgets.QLabel("Введите путь к исходному датасету:", self)
        self.text.move(10, 0)
        # self.text.setAlignment(QtCore.Qt.AlignLeft)
        self.text.adjustSize()

        self.button1 = QtWidgets.QPushButton("Аннотация", self)
        self.button1.move(90, 200)
        self.button1.clicked.connect(self.click_csv)
        self.button1.adjustSize()

        self.button2 = QtWidgets.QPushButton("Копирование", self)
        self.button2.move(162, 200)
        self.button2.clicked.connect(self.click_copy)
        self.button2.adjustSize()

        self.button3 = QtWidgets.QPushButton("Копирование со случайными номерами", self)
        self.button3.move(234, 200)
        self.button3.clicked.connect(self.click_rand)
        self.button3.adjustSize()
        
        self.button4 = QtWidgets.QPushButton("Изображения", self)
        self.button4.move(435, 200)
        self.button4.clicked.connect(self.click_img)
        self.button4.adjustSize()
        
    def click_csv(self):
        if not self.w_text.text():
            self.w = New_Interface()
            self.w.new_path()
        elif not os.path.isdir(self.w_text.text()): 
            self.w = New_Interface()
            self.w.not_path()
        else:
            self.d_text, self.ok = QInputDialog.getText(self, "Аннотация", "Введите путь для сохранения:") 
            print(self.d_text)  
          
        directory = f"{self.w_text.text()} rose"
        write_csv.write_csv(directory, self.d_text, "rose")  
        directory = f"{self.w_text.text()} tulip" 
        write_csv.write_csv(directory, self.d_text, "tulip")   

    def click_copy(self):
        if not self.w_text.text():
            self.w = New_Interface()
            self.w.new_path()
            
        elif not os.path.isdir(self.w_text.text()): 
            self.w = New_Interface()
            self.w.not_path()
        else:
            self.d_text, self.ok = QInputDialog.getText(self, "Копирование", "Введите путь для копирования:")
            print(self.d_text)
            
            directory = f"{self.w_text.text()} rose"
            copy_.copy_dataset(directory, self.d_text, "rose")
            directory = f"{self.w_text.text()} tulip" 
            copy_.copy_dataset(directory, self.d_text, "tulip")
    
    def click_rand(self):
        if not self.w_text.text():
            self.w = New_Interface()
            self.w.new_path()
            
        elif not os.path.isdir(self.w_text.text()): 
            self.w = New_Interface()
            self.w.not_path()
            
        else:
            self.d_text, self.ok = QInputDialog.getText(self, "Копирование со случайными номерами", "Введите путь для копирования:")
            print(self.d_text)  
            
            directory = f"{self.w_text.text()} rose"
            rand.copy_dataset(directory, self.d_text, "rose")
            directory = f"{self.w_text.text()} tulip" 
            rand.copy_dataset(directory, self.d_text, "tulip")
   
    def click_img(self):
        self.w = New_Interface()
        self.w.img()
            
class New_Interface(QMainWindow):
    def __init__(self):
        super(New_Interface, self).__init__()
        self.label = QtWidgets.QLabel(self)
        self.setCentralWidget(self.label)
    
    def new_path(self):
        self.setWindowTitle("Предупреждение")
        self.move(700, 200)
        self.resize(300, 150)
        self.wtext = QtWidgets.QLabel("Введите путь к исходному датасету", self)
        self.wtext.move(55, 60)
        self.wtext.adjustSize()
        self.show()
    
    def not_path(self):
        self.setWindowTitle("Предупреждение")
        self.move(700, 200)
        self.resize(300, 150)
        self.wtext = QtWidgets.QLabel("Указанного датасета не существует", self)
        self.wtext.move(55, 60)
        self.wtext.adjustSize()
        self.show()   
    
    def img(self):
        self.setWindowTitle("Изображения")
        self.move(700, 200)
        self.resize(500, 400)
        
        self.button1 = QtWidgets.QPushButton("Следующая роза", self)
        self.button1.move(156, 360)
        self.button1.clicked.connect(self.click_rose)
        self.button1.adjustSize()

        self.button2 = QtWidgets.QPushButton("Следующий тюльпан", self)
        self.button2.move(250, 360)
        self.button2.clicked.connect(self.click_tulip)
        self.button2.adjustSize()
        
        self.rose = iter.Iterator("D:\Lab Python\dataset_2copy.csv", "rose")
        self.tulip = iter.Iterator("D:\Lab Python\dataset_2copy.csv", "tulip")
        
        self.show()
    
    def click_rose(self):
        self.pixmap = QPixmap(next(self.rose))
        self.label.setPixmap(self.pixmap)
        self.setCentralWidget(self.label) 
        self.label.resize(self.pixmap.width(), self.pixmap.height())
        self.show()
    
    def click_tulip(self):
        self.pixmap = QPixmap(next(self.tulip))
        self.label.setPixmap(self.pixmap)
        self.setCentralWidget(self.label) 
        self.label.resize(self.pixmap.width(), self.pixmap.height())
        self.show()
            
def create():
    app = QApplication(sys.argv)
    w = Interface()

    w.show()
    sys.exit(app.exec_())
    # D:\Lab Python\Lab_1\dataset\ 
    # D:\Lab Python\

create()
