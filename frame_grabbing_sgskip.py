"""
==============
Frame grabbing
==============

Use a MovieWriter directly to grab individual frames and write them to a
file.  This avoids any event loop integration, and thus works even with the Agg
backend.  This is not recommended for use in an interactive setting.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
from matplotlib.animation import ImageMagickFileWriter

# Fixing random state for reproducibility
np.random.seed(19680801)

w = np.random.normal(size=(100, 2))
rw = np.cumsum(w, axis=0)

metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='Movie support!')
writer = ImageMagickFileWriter(fps=15, metadata=metadata)

fig = plt.figure()
l, = plt.plot([], [])

plt.xlim(-5, 5)
plt.ylim(-5, 5)

with writer.saving(fig, "test.gif", 100):
    for i in range(1, 1000):
        x1 = rw[:i+1, 0]
        y1 = rw[:i+1, 1]
        l.set_data(x1, y1)
        writer.grab_frame()
