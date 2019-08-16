import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.random.randn(1000, 3)
w = np.cumsum(x, axis=0)

plt.ion()
fig= plt.figure(figsize=(8, 8))
# plt.axis("off")
for i in range(len(w)-1):
    x1 = w[i]
    x2 = w[i+1]
    x = [x1[0], x2[0]]
    y = [x1[1], x2[1]]
    z = [x1[2], x2[2]]

    ax = fig.gca(projection='3d')
    ax.scatter(x2[0], x2[1], x2[2], color="blue")
    ax.plot(x, y, z, color='blue')
    ax.grid(False)
    plt.pause(0.01)

plt.ioff()
plt.show()
