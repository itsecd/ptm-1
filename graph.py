import matplotlib.pyplot as plt
import Gen_num
from time import time



def show_plt(cores: list, times: list):
    plt.plot(cores, times)
    plt.xlabel("ядра, шт")
    plt.ylabel("Время, сек")
    plt.show()
