import os
import shutil
import random 

from annotation import Annotation


def random_copy(path_main: str, path: str, annotation: Annotation) -> None:
    """Copying dataset to another directory (dataset/номер.jpg) and creating an annotation"""
    if not os.path.isdir(path):
        try:
            os.mkdir(path)
        except OSError:
            print ("Создать директорию %s не удалось" % path)
    subfolders = os.listdir(path_main)
    for subfolder in subfolders:
        files=os.listdir(os.path.join(path_main,subfolder))
        for fname in files:
            shutil.copy(os.path.join(path_main,subfolder,fname),path)
            fname2 = f"{random.randint(0, 10000)}.jpg"
            while os.path.isdir(os.path.join(path, fname2)):
                fname2 = f"{random.randint(0, 10000)}.jpg"
            os.rename(os.path.join(path,fname),os.path.join(path, fname2))
            annotation.add_line(path,fname2,subfolder)


def copy_and_annotation(path_main: str, path: str, annotation: Annotation) -> None:
    """Copying dataset to another directory (dataset/class_0000.jpg) and creating an annotation"""
    if not os.path.isdir(path):
        try:
            os.mkdir(path)
        except OSError:
            print ("Создать директорию %s не удалось" % path)
    subfolders = os.listdir(path_main)
    for subfolder in subfolders:
        files=os.listdir(os.path.join(path_main,subfolder))
        for fname in files:
            shutil.copy(os.path.join(path_main,subfolder,fname),path)
            os.rename(os.path.join(path,fname),os.path.join(path, f"{subfolder}_{fname}"))
            annotation.add_line(path, f"{subfolder}_{fname}", subfolder)


if __name__ == "__main__":
    path_main = 'C:/Users/user/Desktop/dataset_copy' 
    path = 'C:/Users/user/Desktop/dataset1'
    annotation_main = Annotation("task2_csv.csv")
    copy_and_annotation(path_main,path,annotation_main)
    random_copy(path_main,path,annotation_main)