import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(100000)
w = np.cumsum(x)

plt.ion()

for i in range(len(w)-1):
    x1 = w[i]
    x2 = w[i+1]
    plt.plot([i, i+1], [x1, x2], color="blue")
    plt.pause(0.01)

plt.ioff()
plt.show()
