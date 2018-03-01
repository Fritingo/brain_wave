import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
from matplotlib.widgets import CheckButtons


record = np.load('record.npy')

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(211)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

x = np.arange(0, len(record[1]), 1)

ax.set_title('Brain_wave')
ax2 = fig.add_subplot(212)
y=[]
for i in range(16):
	y[i] = record[i]
	ax.plot(x,y[i],'-')
	ax2.plot(x,y[i],'-')


def onselect(xmin, xmax):

    indmin, indmax = np.searchsorted(x, (xmin, xmax))
    indmax = min(len(x) - 1, indmax)

    thisx = x[indmin:indmax]
    thisy = y[indmin:indmax]

    line.set_data(thisx, thisy)
    ax2.set_xlim(thisx[0], thisx[-1])

    ax2.set_ylim(thisy.min(), thisy.max())
    fig.canvas.draw()

# set useblit True on gtkagg for enhanced performance
span = SpanSelector(ax, onselect, 'horizontal', useblit=True,
                    rectprops=dict(alpha=0.5, facecolor='red'))


plt.show()