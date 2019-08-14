import numpy as np
import matplotlib.pyplot as plt
import imageio

x = np.random.normal(size=(1000, 2))
rw = np.cumsum(x, axis=0) / 50

fig, ax = plt.subplots(figsize=(10,5))
ln, = plt.plot([], [], color="blue")

def init():
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    return ln,

def update(i):
    x1 = rw[:i+1, 0]
    y1 = rw[:i+1, 1]

    ln.set_data(x1, y1)
    #ax.set_xlim(-1+x1[-1], 1+x1[-1])
    #ax.set_ylim(-1+y1[-1], 1+y1[-1])

    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype="uint8")
    h, w = fig.canvas.get_width_height()
    image = image.reshape((h, w*3))
    return image

imageio.mimsave("test.gif", [update(i) for i in range(1, 10)], fps=1)

