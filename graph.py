import matplotlib.pyplot as plt


def show_plt(cores: list, times: list):
    plt.plot(cores, times)
    plt.xlabel("ядра, шт")
    plt.ylabel("Время, сек")
    plt.show()
