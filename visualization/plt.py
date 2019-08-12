import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def plt_figure_axes_axis():
    X = np.clip(np.random.randn(60, 60, 3), 0, 1)
    fig = plt.figure(figsize=(6.4, 4.8))
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.imshow(X)

    ax2.xaxis.set_ticks([])
    ax2.yaxis.set_ticks([])
    ax2.text(0.5, 0.5, "Random", ha="center", va="center", size=20, alpha=0.5)
    ax2.plot([0, 1], [0, 1])
    ax2.plot([0, 1], [0, 1])
    
    plt.show()

def plt_subplot():
    # 子图
    for i in range(1, 101):
        plt.subplot(10, 10, i)
        plt.xticks([])
        plt.yticks([])
        plt.text(0.5, 0.5, str(i), ha="center", va="center", size=20, alpha=0.5)
    plt.show()

def plt_axes():
    # 坐标系
    import matplotlib.gridspec as gridspec
    size = 10
    G = gridspec.GridSpec(size, size)
    for i in range(size):
        ax = plt.subplot(G[i, :size-i])
        ax.set_xticks([])
        ax.set_yticks([])
        ax.text(0.5, 0.5, str(i), ha="center", va="center", alpha=0.5)

    plt.show()

    for i in range(11, 1, -1):
        plt.axes([0, 0, i/10, i/10])
        plt.text(0.5, 0.5, i, size=20/i, ha="left", va="center", alpha=0.5)
    plt.show()

def plt_axis():
    # axis

if __name__ == "__main__":
    plt_axes()
