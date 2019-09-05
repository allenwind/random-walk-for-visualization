import psutil
import numpy as np
import matplotlib.pyplot as plt

plt.ion()

data = []
r = psutil.disk_io_counters()
data.append(list(r))
fields = r._fields
while True:
    r = list(psutil.disk_io_counters())
    data.append(list(r))
    plt.plot(np.array(data, dtype=np.float32))
    plt.pause(1)

plt.ioff()
plt.show()
