import os
import shutil


def copy_dataset(path: str,path_to:str) -> None:
    """Функция принимает путь к файлам: path и метку класса: label"""
    if not os.path.isdir(path_to):
        os.mkdir(path_to)
    info = os.listdir(path+"/")
    for i in info:
        info_data = os.listdir(path+"/" + i)
        for j in info_data:
            shutil.copy(
                os.path.join(path+"/"+i, j), os.path.join(path_to+"/", i + "_" + j)
            )


