import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.random.normal(size=(1000, 2))
w = np.cumsum(x, axis=0) / 50

fig, ax = plt.subplots()
ln, = plt.plot([], [], color="blue")

def init():
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    return ln,

def update(i):
    x1 = w[:i+1, 0]
    y1 = w[:i+1, 1]

    ln.set_data(x1, y1)
    #x.set_xlim(-1+x1[-1], 1+x1[-1])
    #ax.set_ylim(-1+y1[-1], 1+y1[-1])
    return ln, ax

an = FuncAnimation(fig, update, frames=np.arange(1, 1000), interval=1, init_func=init, blit=True)
# an.save("test.gif", dpi=80, writer="imagemagick")

plt.show()
