import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(1000, 2)
w = np.cumsum(x, axis=0)

plt.ion()

for i in range(len(w)-1):
    x1 = w[i]
    x2 = w[i+1]
    plt.scatter(*x2, color="blue")
    plt.plot([x1[0], x2[0]], [x1[1], x2[1]], color="blue")
    plt.pause(0.01)

plt.ioff()
plt.show()
