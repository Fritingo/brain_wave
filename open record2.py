import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
from matplotlib.widgets import CheckButtons


record = np.load('record.npy')

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(211)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

x = np.arange(0, len(record[1]), 1)
y1 = record[1]
y2 = record[2]
y3 = record[3]
y4 = record[4]
y5 = record[5]
y6 = record[6]
y7 = record[7]
y8 = record[8]
y9 = record[9]
y10 = record[10]
y11 = record[11]
y12 = record[12]
y13 = record[13]
y14 = record[14]
y15 = record[15]
y = record[0]

ax.plot(x,y,'-')
ax.plot(x, y1, '-')
ax.plot(x,y2,'-')
ax.plot(x,y3,'-')
ax.plot(x,y4,'-')
ax.plot(x,y5,'-')
ax.plot(x,y6,'-')
ax.plot(x,y7,'-')
ax.plot(x,y8,'-')
ax.plot(x,y9,'-')
ax.plot(x,y10,'-')
ax.plot(x,y11,'-')
ax.plot(x,y12,'-')
ax.plot(x,y13,'-')
ax.plot(x,y14,'-')
ax.plot(x,y15,'-')




ax.set_title('Brain_wave')

ax2 = fig.add_subplot(212)
line, = ax2.plot(x,y,'-')
line1, = ax2.plot(x,y1,'-')
line2, = ax2.plot(x, y2,'-')
line3, = ax2.plot(x,y3,'-')
line4, = ax2.plot(x,y4,'-')
line5, = ax2.plot(x,y5,'-')
line6, = ax2.plot(x,y6,'-')
line7, = ax2.plot(x,y7,'-')
line8, = ax2.plot(x,y8,'-')
line9, = ax2.plot(x,y9,'-')
line10, = ax2.plot(x,y10,'-')
line11, = ax2.plot(x,y11,'-')
line12, = ax2.plot(x,y12,'-')
line13, = ax2.plot(x,y13,'-')
line14, = ax2.plot(x,y14,'-')
line15, = ax2.plot(x,y15,'-')




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