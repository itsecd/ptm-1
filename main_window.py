from tkinter import filedialog
from tkinter import *
from PIL import Image
import threading
import create_csv_file
import create_second_dataset
import create_third_dataset
import Iterator


zebra_picture_path = Iterator.Iterator("zebra")
horse_picture_path = Iterator.Iterator("bay horse")


def get_picture(path: str) -> None:
    '''Функция принимает путь к картинке и открывает эту картинку'''
    sample = Image.open(path)
    sample.show()


def csv_file(path: str) -> None:
    '''Функция принимает путь к датасету и создает csv файл'''
    destination = filedialog.askopenfilename()
    create_csv_file.create_annotation_file(path + "/zebra", destination)
    create_csv_file.create_annotation_file(path + "/bay_horse", destination)


def create_dataset(path: str, flag: bool) -> None:
    '''Функция принимает путь к датасету и метку и создает нужный датасет в зависимости от метки'''
    dataset_path = filedialog.askdirectory()
    if flag:
        create_second_dataset.create_dataset(path + "/zebra", dataset_path)
        create_second_dataset.create_dataset(path + "/bay_horse", dataset_path)
    else:
        create_third_dataset.create_dataset(path + "/zebra", dataset_path)
        create_third_dataset.create_dataset(path + "/bay_horse", dataset_path)
    annotations_path = filedialog.askopenfile()
    create_csv_file.create_annotation_file(annotations_path)

    
def start1() -> None:
    '''Создает кнопку "анотация"'''
    threading.Thread(target=csv_file, args=(file, )).start()


def start2() -> None:
    '''Созадет кнопку "первый датасет"'''
    threading.Thread(target=create_dataset, args=(file ,True, )).start()


def start3() -> None:
    '''Создает кнопку "второй датасет"'''
    threading.Thread(target=create_dataset, args=(file ,False, )).start()


def start4() -> None:
    '''Кнопка "следующая лошадь"'''
    threading.Thread(target=get_picture, args=(next(horse_picture_path), )).start()
    
    
def start5() -> None:
    '''Кнопка "следующая зебра"'''
    threading.Thread(target=get_picture, args=(next(zebra_picture_path), )).start()
    

if __name__ == "__main__":
    app = Tk()
    app.title("Лабораторная работа по прикладному программированию")

    start = Label(app, text="select main dataset", font=("Arial Bold", 20))
    start.grid(column=0, row=0)
    file = filedialog.askdirectory()
    start.destroy()

    btn1 = Button(app, text="create annotation", width=100, height=5, command=start1)
    btn1.grid(column=5, row=5)

    btn2 = Button(app, text="create first dataset", width=100, height=5, command=start2)
    btn2.grid(column=5, row=6)
    btn3 = Button(app, text="create second dataset", width=100, height=5, command=start3)
    btn3.grid(column=5, row=7)

    btn4 = Button(app, text="next horse", width=100, height=5, command=start4)
    btn4.grid(column=5,row=8)
    btn5 = Button(app, text="next zebra", width=100, height=5, command=start5)
    btn5.grid(column=5,row=9)


    app.mainloop()