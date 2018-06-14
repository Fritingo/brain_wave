import time
from emotiv import Emotiv
import gevent
import matplotlib.pyplot as plt
import numpy as np

headset = Emotiv(False)

record = np.zeros((16, 1))
record = record.tolist()
plt.ion()
fig, ax = plt.subplots(nrows=4, ncols=4)


def fun():
    plot_num = 0
    for row in ax:
        for col in row:
            for i, v in enumerate(headset.sensors):
                if i == plot_num:
                    record[i].append(headset.sensors[v]['value'])
                    col.cla()
                    col.plot(record[i][-50:-1])

            plot_num = plot_num + 1
    # np.save('record.npy', record)
    # record = np.array(record)
    plt.draw()
    plt.pause(0.03)


while True:
    packet = headset.dequeue()
    if packet is not None:
        fun()
        # print(packet.sensors)
    gevent.sleep(0)
