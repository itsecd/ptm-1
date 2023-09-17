import os

from annotation import Annotation


def creat_annotation(path: str, annotation: Annotation) -> None:
    """Creating an annotation for main dataset"""
    folders = []
    i=0
    for dirs, folder, files in os.walk(path):
        if i==0:
            folders = folder
        else:
            for file in files:
                annotation.add_line(dirs,file,folders[i-1])
        i+=1 


if __name__ == "__main__":
    path_main = 'C:/Users/user/Desktop/dataset_copy' 
    annotation_main = Annotation("task1_csv.csv")
    creat_annotation(path_main, annotation_main)        